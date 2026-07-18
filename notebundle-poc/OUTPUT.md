# Output Example

PoC for Notebundle

## Operations

### Validation

### Case - Success

```bash
notebundle-poc validate example-files/notebundle-example.notebundle
```

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

#### Case - Failure

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

### Convert

- Markdown - Notebundle
- Markdown <- Markdown
- Textbundle - Notebundle
- Textbundle <- Notebundle


<!-- 
- markdown-to-notebundle
- notebundle-to-markdown
- textbundle-to-notebundle
- notebundle-to-textbundle -->

| COMMAND | Markdown | Notebundle | Textbundle
| - | - | - | - |
| markdown-to-notebundle | source | output | |
| notebundle-to-markdown | output | source |
| textbundle-to-notebundle | | output | source |
| notebundle-to-textbundle | | source | output |



### markdown-to-notebundle

```bash
notebundle-poc markdown-to-notebundle \
    example-files/markdown-example.md \
    output/notebundle-from-markdown.notebundle
```

```text
Markdown to Notebundle Result

Source: example-files/markdown-example.md
-----------------------------------------
markdown-example.md


Output: output/notebundle-from-markdown.notebundle
--------------------------------------------------
notebundle-from-markdown.notebundle
  - notebundle-from-markdown.md


Primary note: output/notebundle-from-markdown.notebundle/notebundle-from-markdown.md
```

## notebundle-to-markdown

```bash
notebundle-poc notebundle-to-markdown \
    example-files/notebundle-example.notebundle \
    output/markdown-dir-from-notebundle
```

```text
Notebundle to Markdown Result

Source: example-files/notebundle-example.notebundle
---------------------------------------------------
notebundle-example.notebundle
  - attachments
    - sample.svg
  - notebundle-example.md


Output: output/markdown-dir-from-notebundle
-------------------------------------------
markdown-dir-from-notebundle
  - attachments
    - sample.svg
  - notebundle-example.md
```

## textbundle-to-notebundle

```bash
notebundle-poc textbundle-to-notebundle \
    example-files/textbundle-example.textbundle \
    output/notebundle-from-textbundle.notebundle
```

```text
TextBundle to Notebundle Result

Source: example-files/textbundle-example.textbundle
---------------------------------------------------
textbundle-example.textbundle
  - assets
    - textbundle.png
  - info.json
  - text.markdown


Output: output/notebundle-from-textbundle.notebundle
----------------------------------------------------
notebundle-from-textbundle.notebundle
  - attachments
    - textbundle.png
  - notebundle-from-textbundle.md


Primary note: output/notebundle-from-textbundle.notebundle/notebundle-from-textbundle.md
Attachments dir: output/notebundle-from-textbundle.notebundle/attachments
```

## notebundle-to-textbundle

```bash
notebundle-poc notebundle-to-textbundle \
    example-files/notebundle-example.notebundle \
    output/textbundle-from-notebundle.textbundle
```

```text
Notebundle to TextBundle Result

Source: example-files/notebundle-example.notebundle
---------------------------------------------------
notebundle-example.notebundle
  - attachments
    - sample.svg
  - notebundle-example.md


Output: output/textbundle-from-notebundle.textbundle
----------------------------------------------------
textbundle-from-notebundle.textbundle
  - assets
    - sample.svg
  - info.json
  - text.md
```
