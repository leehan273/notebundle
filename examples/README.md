# Notebundle Example

These files are just examples of Notebundle conversions meant to show you what the actual file structure looks like; there’s nothing special about them.

```
├── attachment-example.notebundle
│   ├── attachment-example.md
│   └── attachments
│       └── sample.svg
├── jsoncanvas-example.notebundle
│   ├── attachments
│   │   └── sample.svg
│   └── note.canvas
├── minimal-example-bundle-name.notebundle
│   └── minimal-example-bundle-name.md
├── minimal-example-note.notebundle
│   └── note.md
└── README.md
```

- `minimal-example` is an example showing the minimum requirements for a valid notebundle. In practice, however, there’s no benefit to converting a note with no attachments into a notebundle like this—unless the goal is to standardize the structure by managing all notes as notebundle.

- `jsoncanvas-example` was created in Obsidian, but because Obsidian (1.15.1) does not support relative paths in Canvas ([Obsidian forum post](https://forum.obsidian.md/t/relative-file-path-supportg/62838)), the file isn't portable.
