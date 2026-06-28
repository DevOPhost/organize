# Contributing

Thanks for wanting to help. A few things before you open a PR:

## Setup

```bash
git clone https://github.com/DevOPhost/organize.git
cd organize
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Running the tests

```bash
pytest
```

All tests need to pass before I'll merge anything. If you're adding a feature,
add tests for it too — I'll ask if you don't.

## A few ground rules

- Keep it scoped. This tool does one thing. PRs that add unrelated features
  (scheduling, cloud sync, etc.) are out of scope — I'm intentionally keeping
  this small and auditable.

- Don't break the `--dry-run` contract. Whatever you change, `--dry-run` must
  never write anything to disk. That's the one guarantee I want to keep forever.

- If you're adding a new file category to `categories.py`, just open the PR —
  those are easy to review and usually merged same day.

## Reporting bugs

Open an issue with the command you ran, your OS, and your Python version.
That's usually enough for me to reproduce it.
