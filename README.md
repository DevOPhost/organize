# organize-files

**[English](#english) · [Português](#português)**

---

<a name="english"></a>

A small command-line tool I built to stop wasting time manually organizing my Downloads folder.

`organize-files` scans a directory and moves files into folders based on their extensions. Images go to `images/`, PDFs and text files go to `docs/`, source files go to `code/`, compressed files go to `archives/`, and anything that does not match a known category goes to `misc/`.

It also includes a `--dry-run` mode, so you can preview everything before actually moving any files.

```bash
$ organize-files ~/Downloads --dry-run

organize-files v1.0.0

  dry-run mode — no files will be moved

Scanning /Users/you/Downloads

 file                     → destination   status
 ────────────────────────────────────────────────
 screenshot_2024.png       images         would move
 contract_draft.pdf        docs           would move
 notes.txt                 docs           would move
 setup.py                  code           would move
 backup.zip                archives       would move
 .DS_Store                 —              skipped

  5 files would move  ·  1 skipped

Run without --dry-run to apply the changes.
```

## Installation

Requires Python 3.10 or newer.

```bash
pip install git+https://github.com/DevOPhost/organize.git
```

## Usage

```bash
# organize the current directory
organize-files

# organize a specific folder
organize-files ~/Downloads

# preview the changes without moving anything
organize-files ~/Downloads --dry-run

# include hidden files such as .DS_Store and .gitkeep
organize-files ~/Downloads --include-hidden
```

## File categories

| Folder        | Extensions                                           |
| ------------- | ---------------------------------------------------- |
| `images`      | jpg, jpeg, png, gif, webp, svg, ico, bmp, tiff, heic |
| `videos`      | mp4, mov, avi, mkv, wmv, flv, webm, m4v              |
| `audio`       | mp3, wav, flac, aac, ogg, m4a, wma                   |
| `docs`        | pdf, doc, docx, txt, md, rtf                         |
| `sheets`      | xls, xlsx, csv, ods                                  |
| `slides`      | ppt, pptx, odp                                       |
| `code`        | py, js, ts, html, css, json, yaml, sh, sql, and more |
| `archives`    | zip, tar, gz, rar, 7z, bz2                           |
| `executables` | exe, dmg, pkg, deb, appimage                         |
| `fonts`       | ttf, otf, woff, woff2                                |
| `ebooks`      | epub, mobi, azw, azw3                                |
| `misc`        | everything else                                      |

## Behavior

A few things were intentionally kept simple:

* **It does not overwrite files.**
  If `images/photo.jpg` already exists, the incoming file becomes `photo (1).jpg`.

* **Hidden files are skipped by default.**
  Files like `.DS_Store`, `.gitkeep`, and `.env` stay untouched unless you use `--include-hidden`.

* **It is not recursive.**
  The tool only organizes files directly inside the target directory. It does not scan nested folders because I wanted it to be predictable and safe by default.

## Development

```bash
git clone https://github.com/DevOPhost/organize.git
cd organize

python -m venv .venv
source .venv/bin/activate

pip install -e ".[dev]"
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) if you want to open a pull request.

## License

MIT License. Use it, modify it, break it, improve it.

---

<a name="português"></a>

Uma ferramenta simples de linha de comando que eu criei para parar de perder tempo organizando a pasta de Downloads manualmente.

O `organize-files` varre um diretório e move os arquivos para pastas de acordo com suas extensões. Imagens vão para `images/`, PDFs e arquivos de texto vão para `docs/`, arquivos de código vão para `code/`, arquivos compactados vão para `archives/`, e qualquer coisa que não se encaixe em uma categoria conhecida vai para `misc/`.

Também existe o modo `--dry-run`, que permite visualizar tudo antes de mover qualquer arquivo de verdade.

```bash
$ organize-files ~/Downloads --dry-run

organize-files v1.0.0

  modo dry-run — nenhum arquivo será movido

Verificando /Users/voce/Downloads

 arquivo                  → destino       status
 ────────────────────────────────────────────────
 screenshot_2024.png       images         seria movido
 contrato_rascunho.pdf     docs           seria movido
 notas.txt                 docs           seria movido
 setup.py                  code           seria movido
 backup.zip                archives       seria movido
 .DS_Store                 —              ignorado

  5 arquivos seriam movidos  ·  1 ignorado

Execute sem --dry-run para aplicar as alterações.
```

## Instalação

Requer Python 3.10 ou superior.

```bash
pip install git+https://github.com/DevOPhost/organize.git
```

## Como usar

```bash
# organiza o diretório atual
organize-files

# organiza uma pasta específica
organize-files ~/Downloads

# visualiza as alterações sem mover nada
organize-files ~/Downloads --dry-run

# inclui arquivos ocultos como .DS_Store e .gitkeep
organize-files ~/Downloads --include-hidden
```

## Categorias de arquivos

| Pasta         | Extensões                                            |
| ------------- | ---------------------------------------------------- |
| `images`      | jpg, jpeg, png, gif, webp, svg, ico, bmp, tiff, heic |
| `videos`      | mp4, mov, avi, mkv, wmv, flv, webm, m4v              |
| `audio`       | mp3, wav, flac, aac, ogg, m4a, wma                   |
| `docs`        | pdf, doc, docx, txt, md, rtf                         |
| `sheets`      | xls, xlsx, csv, ods                                  |
| `slides`      | ppt, pptx, odp                                       |
| `code`        | py, js, ts, html, css, json, yaml, sh, sql, e mais   |
| `archives`    | zip, tar, gz, rar, 7z, bz2                           |
| `executables` | exe, dmg, pkg, deb, appimage                         |
| `fonts`       | ttf, otf, woff, woff2                                |
| `ebooks`      | epub, mobi, azw, azw3                                |
| `misc`        | qualquer outra coisa                                 |

## Comportamento

Algumas decisões foram mantidas de propósito para deixar a ferramenta simples e segura:

* **Não sobrescreve arquivos.**
  Se `images/foto.jpg` já existir, o novo arquivo será salvo como `foto (1).jpg`.

* **Arquivos ocultos são ignorados por padrão.**
  Arquivos como `.DS_Store`, `.gitkeep` e `.env` ficam onde estão, a menos que você use `--include-hidden`.

* **Não é recursivo.**
  A ferramenta organiza apenas os arquivos que estão diretamente dentro do diretório escolhido. Ela não entra em subpastas, justamente para evitar mexer em arquivos que você não apontou explicitamente.

## Desenvolvimento

```bash
git clone https://github.com/DevOPhost/organize.git
cd organize

python -m venv .venv
source .venv/bin/activate

pip install -e ".[dev]"
pytest
```

Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) se quiser abrir um pull request.

## Licença

Licença MIT. Use, modifique, quebre e melhore.
