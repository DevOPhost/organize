import sys
from pathlib import Path

import click
from rich import box
from rich.console import Console
from rich.table import Table

from . import __version__
from .organizer import organize

console = Console()


def _print_header():
    console.print(f"\n[bold cyan]organize-files[/] [dim]v{__version__}[/]\n")


def _print_dry_run_warning():
    console.print(
        "[bold yellow]  dry-run mode[/] [dim]— nothing will actually move[/]\n"
    )


def _build_summary_table(moved, skipped, errors) -> Table:
    table = Table(box=box.SIMPLE, show_header=True, header_style="bold dim")
    table.add_column("file", style="white")
    table.add_column("→ destination", style="cyan")
    table.add_column("status", justify="right")

    for src, dst in moved:
        table.add_row(src.name, str(dst.parent.name), "[green]✓ moved[/]")

    for path in skipped:
        table.add_row(path.name, "—", "[dim]skipped[/]")

    for path, reason in errors:
        table.add_row(path.name, "—", f"[red]✗ {reason}[/]")

    return table


@click.command()
@click.argument("directory", default=".", type=click.Path(exists=True, file_okay=False))
@click.option("--dry-run", is_flag=True, help="Preview what would happen without moving anything.")
@click.option("--include-hidden", is_flag=True, help="Include hidden files (e.g. .DS_Store). Skipped by default.")
@click.version_option(__version__, "--version", "-v")
def main(directory: str, dry_run: bool, include_hidden: bool):
    """
    Organize files in DIRECTORY into subfolders by type.

    Defaults to the current directory if none is given.

    \b
    Examples:
      organize-files
      organize-files ~/Downloads
      organize-files ~/Downloads --dry-run
    """
    _print_header()

    if dry_run:
        _print_dry_run_warning()

    source = Path(directory).resolve()
    console.print(f"[dim]Scanning[/] {source}\n")

    try:
        result = organize(source, dry_run=dry_run, skip_hidden=not include_hidden)
    except (FileNotFoundError, NotADirectoryError) as exc:
        console.print(f"[red]Error:[/] {exc}")
        sys.exit(1)

    if result.total == 0:
        console.print("[dim]Nothing to organize. The folder is already empty.[/]")
        return

    if result.moved or result.skipped or result.errors:
        console.print(_build_summary_table(result.moved, result.skipped, result.errors))

    # summary line at the bottom
    parts = []
    if result.moved:
        verb = "would move" if dry_run else "moved"
        parts.append(f"[green]{len(result.moved)} files {verb}[/]")
    if result.skipped:
        parts.append(f"[dim]{len(result.skipped)} skipped[/]")
    if result.errors:
        parts.append(f"[red]{len(result.errors)} errors[/]")

    console.print("  " + "  ·  ".join(parts) + "\n")

    if dry_run and result.moved:
        console.print("[dim]Run without --dry-run to apply.[/]\n")
