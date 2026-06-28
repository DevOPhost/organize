# I kept adding to this list over time — feel free to extend it.
# The key is the target folder name, the value is the list of extensions that go there.
# Anything not listed ends up in 'misc'.

CATEGORIES: dict[str, list[str]] = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico", ".bmp", ".tiff", ".heic"],
    "videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm", ".m4v"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "docs": [".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf", ".md"],
    "sheets": [".xls", ".xlsx", ".ods", ".csv"],
    "slides": [".ppt", ".pptx", ".odp"],
    "code": [".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css", ".scss", ".json",
             ".yaml", ".yml", ".toml", ".sh", ".bash", ".zsh", ".sql", ".rb", ".go",
             ".rs", ".c", ".cpp", ".h", ".java", ".php", ".swift", ".kt"],
    "archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2", ".xz"],
    "executables": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".appimage"],
    "fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "ebooks": [".epub", ".mobi", ".azw", ".azw3"],
}


def get_category(extension: str) -> str:
    """Return the folder name for a given file extension."""
    ext = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "misc"
