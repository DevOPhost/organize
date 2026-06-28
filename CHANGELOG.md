# Changelog

## [1.0.0] — 2026-01-15

I built this because I was tired of manually sorting my
Downloads folder every other week. Ended up being useful enough to share.

### What's in it
- Organizes files by extension into typed subfolders (images, docs, code, etc.)
- `--dry-run` flag to preview without touching anything
- Conflict resolution: never overwrites existing files, appends `(1)`, `(2)`, etc.
- Hidden files (`.DS_Store`, `.gitkeep`, etc.) are skipped by default
- `--include-hidden` flag if you really want those moved too
