# Notebundle (WIP)

> A convention for treating note files, such as Markdown files, and their attachments as a single unit without relying on proprietary formats or specific software.

First, to be clear: **Notebundle is not a new file format that requires dedicated software.**

Notebundle is a slightly more formalized version (enough to be automated) of the conventional file management format used when writing and managing Markdown notes with attachments.

If you are familiar with [TextBundle](https://textbundle.org/), Notebundle can be understood as something between a standalone Markdown file and TextBundle: more integrated than Markdown alone, but less rigid than TextBundle.

**The goal of Notebundle is to help users retain control over their notes and manage them according to their own needs.**

Accordingly, Notebundle should neither require specific software nor impose so much structure that it restricts how users work with their notes.

> File over app is a philosophy: if you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. Use tools that give you this freedom.
>
> File over app is an appeal to tool makers: accept that all software is ephemeral, and give people ownership over their data.

— [File over app — Steph Ango](https://stephango.com/file-over-app)

Notebundle proposes a shared convention that allows personal scripts and software tools to interoperate while preserving as much freedom and compatibility with existing systems as possible.

## Notebundle Example

Let's assume there is a Markdown file named `my-note.md` that references a single image attachment.
It is an ordinary Markdown file with nothing special about its contents.

```markdown
# My Note

Lorem ipsum dolor sit amet

![Image](./attachments/image.png)
```

A typical notes directory might look like this:

```text
notes/
├── attachments/
│   ├── image.png
│   └── ...
├── note-1.md
├── note-2.md
├── note-3.md
└── my-note.md
```

This structure is common, but moving an individual note requires locating and moving all of its attachments as well. Those attachments may be mixed with files belonging to many other notes.

Some editors can update these links automatically, but problems can still occur: links may break after files are moved, and attachment filename collisions may require additional handling.

A single project-wide attachment directory, such as `all-attachments/`, can solve some of these problems. However, it also makes individual notes harder to extract from the project, and the shared directory may eventually become large and difficult to manage.

---

If the note from the previous example is reorganized as a Notebundle named `my-note.notebundle`, its structure looks like this:

```text
my-note.notebundle/
├── attachments/
│   └── image.png
└── my-note.md
```

(`my-note.notebundle` is still just an ordinary directory. The suffix does not require any special filesystem support.)

> To avoid repeating `my-note` in both the directory name and the content filename, the content file may instead be named `note.*`:
> 
> ```text
> my-note.notebundle/
> ├── attachments/
> │   └── image.png
> └── note.md
> ```

The content of the `my-note.notebundle/my-note.md` file does not need to be changed at all from the previous example.

Now, the `notes/` directory looks like this after converting only `my-note.md` to `my-note.notebundle`:

```text
notes/
├── attachments/
│   └── ...
├── note-1.md
├── note-2.md
├── note-3.md
└── my-note.notebundle/
    ├── attachments/
    │   └── image.png
    └── my-note.md
```

- You can now move or copy the entire `my-note.notebundle` directory as a single unit, keeping the note and its attachments together.
- Because it has the characteristic suffix `.notebundle`, you can immediately recognize in the file manager that the directory is intended to be treated as a single note rather than as an arbitrary nested directory.

In short, the Notebundle convention places each note and its local attachments in a dedicated directory with a `.notebundle` suffix.

Because a Notebundle is simply an ordinary directory structure, it does not tie users to any particular software. The note files themselves remain unchanged, so existing editors continue to work as before. At the same time, the shared structure is consistent enough to support automated conversion and management.

## Notebundle Specification (Recommendation)

- **The name of the Notebundle directory must end with `.notebundle`.**  

    Like an ordinary file extension, this suffix allows users and tools to distinguish a Notebundle from a regular directory.

- **It is assumed that there is only one primary note file within a Notebundle.**  

    Basically, a single Notebundle represents a single note.

- **The primary note file must either use the Notebundle directory's name without the `.notebundle` suffix or be named `note.*`.**  

    For example, if `lorem-ipsum.notebundle` contains a Markdown note, its primary note file must be named either `lorem-ipsum.md` or `note.md`.

- **Attachments to be bundled with the note should be placed in the `attachments/` directory.**  
    
    Files that should be moved or copied together with the note should be placed in the Notebundle's `attachments/` directory.

    However, there is no obligation to place all referenced files in the `attachments/` directory.

**The specification intentionally leaves strict constraints and detailed behavior undefined.**

The convention is intentionally loose, much like Markdown itself. Just as Markdown remains flexible enough to accommodate unusual syntax and content, Notebundle should remain flexible enough to support different workflows.

**Notebundle exists to help users manage their own notes according to their own needs.** The convention should never get in the way of users working directly with their files.

## Compatible Software

- Any file manager
- Any editor that works directly with files and directories

Because Notebundle relies on ordinary files and directories, it may be difficult to use with note-taking applications that store content exclusively in an internal database.

Editors that work directly with files and are therefore well suited to Notebundle include [VS Code](https://code.visualstudio.com/), [Obsidian](https://obsidian.md/), and [Zettlr](https://www.zettlr.com/).

Although Notebundle was originally conceived for Markdown notes, the convention can also be applied to other file formats.

### Software that directly supports Notebundle

Currently a work in progress.

- [notebundle-poc](./notebundle-poc/README.md) (The `notebundle-poc` Python project included in the current repository)

    This is an experimental implementation that converts between Markdown, Notebundle, and TextBundle, and validates Notebundle directories.
    
    The implementation details of this PoC are not normative and do not define the Notebundle specification.

- obsidian-notebundle (WIP)

    A work-in-progress Obsidian plugin providing support for Notebundle.

## License

**CC0 1.0 Universal — No Rights Reserved**

Except where otherwise noted, the contents of this repository are dedicated to the public domain under CC0.

Files under `notebundle-poc/example-files/` are excluded from this CC0 dedication.
