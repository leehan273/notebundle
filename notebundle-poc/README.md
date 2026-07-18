# Notebundle PoC

This is a proof-of-concept CLI for Notebundle.

The goal of this PoC is to demonstrate a minimal automated logic for converting between Markdown, Notebundle, and TextBundle.

**This PoC never define a complete implementation for various workflow about Notebundle.**

## Supported operations

```text
validate                  Validate a Notebundle directory
markdown-to-notebundle    Convert a Markdown file to a Notebundle directory
notebundle-to-markdown    Convert a Notebundle directory to a regular directory
textbundle-to-notebundle  Convert a TextBundle directory to a Notebundle directory
notebundle-to-textbundle  Convert a Notebundle directory to a TextBundle directory
```

## Example files

This repository includes few sample files under `example-files/`.

```text
example-files
├── markdown-example.md
├── notebundle-example.notebundle
│   ├── attachments
│   │   └── sample.svg
│   └── notebundle-example.md
└── textbundle-example.textbundle
    ├── assets
    │   └── textbundle-logo.png
    ├── info.json
    └── text.markdown
```

Also include `invalid-notebundle-example.notebundle/` for invalid example of Notebundle. (Primary note filename doesn't match with bundle name)

```text
invalid-notebundle-example.notebundle
└── different-title.md
```

Each content of file doesn't have anything special.


## Validation

Validate a Notebundle directory:

```bash
notebundle-poc validate example-files/notebundle-example.notebundle
```

Example output:

```text
Validation Result

Valid: True

Path: example-files/notebundle-example.notebundle
-------------------------------------------------
notebundle-example.notebundle
  - attachments
    - sample.svg
  - notebundle-example.md
```

A valid Notebundle must satisfy the rules used by this PoC:

- The target must be a directory.
- The directory name must end with `.notebundle`.
- The root directory must contain exactly one primary note.
- The primary note must be named either `<bundle-name>.*` or `note.*`.
- If `attachments/` exists, it must be a directory.

Example failure:

```bash
notebundle-poc validate example-files/wrong-notebundle-example.notebundle
```

```text
Validation Result

Valid: False

Path: example-files/wrong-notebundle-example.notebundle
-------------------------------------------------------
wrong-notebundle-example.notebundle
  - different-title.md

Issues
------
- [error] Primary note is missing.
  A Notebundle must contain exactly one root-level primary note named `wrong-notebundle-example.*` or `note.*`.
```

## Conversions



| Command | Source | Output |
|---|---|---|
| `markdown-to-notebundle` | Markdown file | Notebundle (directory) |
| `notebundle-to-markdown` | Notebundle (directory) | Regular directory |
| `textbundle-to-notebundle` | TextBundle (directory) | Notebundle (directory) |
| `notebundle-to-textbundle` | Notebundle (directory) | TextBundle (directory) |

Check [OUTPUT.md](./OUTPUT.md) for conversion result example.

### Markdown to Notebundle

```bash
notebundle-poc markdown-to-notebundle \
  example-files/markdown-example.md \
  output/notebundle-from-markdown.notebundle
```

This creates:

```text
output/notebundle-from-markdown.notebundle/
└── notebundle-from-markdown.md
```

### Notebundle to Markdown directory

```bash
notebundle-poc notebundle-to-markdown \
  example-files/notebundle-example.notebundle \
  output/markdown-dir-from-notebundle
```

This copies the Notebundle contents into a regular directory:

```text
output/markdown-dir-from-notebundle/
├── attachments/
│   └── sample.svg
└── notebundle-example.md
```

### TextBundle to Notebundle

```bash
notebundle-poc textbundle-to-notebundle \
  example-files/textbundle-example.textbundle \
  output/notebundle-from-textbundle.notebundle
```

This converts TextBundle into the Notebundle layout:

```text
output/notebundle-from-textbundle.notebundle/
├── attachments/
│   └── textbundle.png
└── notebundle-from-textbundle.md
```

In this PoC, TextBundle `assets/` is copied to Notebundle `attachments/`.

### Notebundle to TextBundle

```bash
notebundle-poc notebundle-to-textbundle \
  example-files/notebundle-example.notebundle \
  output/textbundle-from-notebundle.textbundle
```

This creates:

```text
output/textbundle-from-notebundle.textbundle/
├── assets/
│   └── sample.svg
├── info.json
└── text.md
```

In this PoC, Notebundle `attachments/` is copied to TextBundle `assets/`.

## Limitations

This is a minimal PoC implementation.  
**Intended for demonstration, not production use.**

**This PoC never define a complete implementation for various workflow about Notebundle.**