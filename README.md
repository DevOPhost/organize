# organize-files

**[English](#english) · [Português](#português)**

---

<a name="english"></a>

I got tired of manually sorting my Downloads folder. So I built this.

It scans a directory and moves files into subfolders based on their extension —
images go to `images/`, PDFs to `docs/`, Python scripts to `code/`, and so on.
There's a `--dry-run` flag so you can see exactly what's going to happen before
anything actually moves.

```
$ organize-files ~/Downloads --dry-run

organize-files v1.0.0

  dry-run mode — nothing will actually move

Scanning /Users/you/Downloads

 file                     → destination   status
 ────────────────────────────────────────────────
 screenshot_2024.png       images         ✓ moved
 contract_draft.pdf        docs           ✓ moved
 notes.txt                 docs           ✓ moved
 setup.py                  code           ✓ moved
 backup.zip                archives       ✓ moved
 .DS_Store                 —              skipped

  5 files would move  ·  1 skipped

Run without --dry-run to apply.
```

## Install

Requires Python 3.10+.

```bash
pip install git+https://github.com/DevOPhost/organize.git
```

## Usage

```bash
# organize the current directory
organize-files

# organize a specific folder
organize-files ~/Downloads

# preview without moving anything
organize-files ~/Downloads --dry-run

# also move hidden files (.DS_Store, .gitkeep, etc.)
organize-files ~/Downloads --include-hidden
```

## How files get sorted

| Folder        | Extensions                                             |
|---------------|--------------------------------------------------------|
| `images`      | jpg, jpeg, png, gif, webp, svg, ico, bmp, tiff, heic  |
| `videos`      | mp4, mov, avi, mkv, wmv, flv, webm, m4v               |
| `audio`       | mp3, wav, flac, aac, ogg, m4a, wma                    |
| `docs`        | pdf, doc, docx, txt, md, rtf                          |
| `sheets`      | xls, xlsx, csv, ods                                   |
| `slides`      | ppt, pptx, odp                                        |
| `code`        | py, js, ts, html, css, json, yaml, sh, sql, and more  |
| `archives`    | zip, tar, gz, rar, 7z, bz2                            |
| `executables` | exe, dmg, pkg, deb, appimage                          |
| `fonts`       | ttf, otf, woff, woff2                                 |
| `ebooks`      | epub, mobi, azw, azw3                                 |
| `misc`        | anything else                                          |

A few things worth knowing:

- **No overwrites.** If `images/photo.jpg` already exists, the incoming file
  becomes `photo (1).jpg`. It never silently replaces anything.
- **Hidden files are skipped by default.** `.DS_Store`, `.gitkeep`, and friends
  stay where they are unless you pass `--include-hidden`.
- **Not recursive.** It only looks at files directly inside the target directory,
  not nested subfolders. I didn't want it touching things it wasn't explicitly
  pointed at.

## Development

```bash
git clone https://github.com/DevOPhost/organize.git
cd organize
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to open a PR.

## License

MIT — do whatever you want with it.

---

<a name="português"></a>

Cansei de organizar minha pasta de Downloads na mão. Então escrevi isso.

A ferramenta varre um diretório e move os arquivos para subpastas de acordo com
a extensão — imagens vão para `images/`, PDFs para `docs/`, scripts Python para
`code/`, e assim por diante. Tem uma flag `--dry-run` pra você ver exatamente o
que vai acontecer antes de qualquer coisa ser movida de verdade.

```
$ organize-files ~/Downloads --dry-run

organize-files v1.0.0

  dry-run mode — nothing will actually move

Scanning /Users/voce/Downloads

 arquivo                  → destino       status
 ────────────────────────────────────────────────
 screenshot_2024.png       images         ✓ moved
 contrato_rascunho.pdf     docs           ✓ moved
 notas.txt                 docs           ✓ moved
 setup.py                  code           ✓ moved
 backup.zip                archives       ✓ moved
 .DS_Store                 —              skipped

  5 arquivos seriam movidos  ·  1 ignorado

Run without --dry-run to apply.
```

## Instalação

Requer Python 3.10+.

```bash
pip install git+https://github.com/DevOPhost/organize.git
```

## Como usar

```bash
# organiza o diretório atual
organize-files

# organiza uma pasta específica
organize-files ~/Downloads

# visualiza sem mover nada
organize-files ~/Downloads --dry-run

# inclui arquivos ocultos (.DS_Store, .gitkeep, etc.)
organize-files ~/Downloads --include-hidden
```

## Como os arquivos são classificados

| Pasta         | Extensões                                              |
|---------------|--------------------------------------------------------|
| `images`      | jpg, jpeg, png, gif, webp, svg, ico, bmp, tiff, heic  |
| `videos`      | mp4, mov, avi, mkv, wmv, flv, webm, m4v               |
| `audio`       | mp3, wav, flac, aac, ogg, m4a, wma                    |
| `docs`        | pdf, doc, docx, txt, md, rtf                          |
| `sheets`      | xls, xlsx, csv, ods                                   |
| `slides`      | ppt, pptx, odp                                        |
| `code`        | py, js, ts, html, css, json, yaml, sh, sql, e mais    |
| `archives`    | zip, tar, gz, rar, 7z, bz2                            |
| `executables` | exe, dmg, pkg, deb, appimage                          |
| `fonts`       | ttf, otf, woff, woff2                                 |
| `ebooks`      | epub, mobi, azw, azw3                                 |
| `misc`        | qualquer outra coisa                                   |

Algumas coisas que vale saber:

- **Sem sobrescritas.** Se `images/foto.jpg` já existe, o arquivo que está
  chegando vira `foto (1).jpg`. Nunca substitui nada silenciosamente.
- **Arquivos ocultos são ignorados por padrão.** `.DS_Store`, `.gitkeep` e
  similares ficam onde estão, a menos que você passe `--include-hidden`.
- **Não é recursivo.** Só olha os arquivos diretamente dentro do diretório
  alvo, não subpastas. Não quis que a ferramenta tocasse em coisas que não
  foram explicitamente apontadas pra ela.

## Desenvolvimento

```bash
git clone https://github.com/DevOPhost/organize.git
cd organize
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Veja [CONTRIBUTING.md](CONTRIBUTING.md) se quiser abrir um PR.

## Licença

MIT — faz o que quiser.
