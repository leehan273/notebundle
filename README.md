# Notebundle

> A proposal for a simple folder structure and naming convention for managing plain-text notes and their attachments.

## Example

Normal Markdown example:

```markdown
# My Note

Lorem ipsum dolor sit amet

![Image](./attachments/image.png)
```

If you convert `my-note.md` to the notebundle format, it looks like this.

```text
my-note.notebundle/
├── attachments/
│   └── image.png
└── my-note.md
```

Each Notebundle refers to "a single note file bundled together with its attachments."

Therefore, when a notebundle is used in a directory that contains multiple note files, the directory will look like this:

```text
notes/
├── just-normal-note.md
├── lorem-ipsum.md
├── MM-DD-research-note.notebundle/
├── my-note.notebundle/
└── todo.md
```

Because Notebundle only specifies naming conventions for directories and main notes (required) and the location of attachments (recommended) ([#Convention](#convention)), the same approach can be used for plain-text notes other than Markdown.

For example, you can also find a JSON Canvas (Obsidian Canvas) note bundle example in [/examples](examples/).

## Why?

Text note files are flexible and extensible, but once you start adding attachments, they become very difficult to manage.

In no time, a shared attachments folder can fill up with countless randomly named “untitled” images, leaving you unable to tell which notes refer to them. Even if you keep a separate attachments folder alongside each note, once the same directory level is crowded with lots of notes, simply looking at the file list in your file manager won’t tell you whether you need to find and move other folders along with a particular note. You have to figure that out every time.

Some note-taking apps magically manage attachments in an internal database, but that ties users to the app and forces them to give up the freedom and compatibility that are among the key benefits of text-based notes.

> File over app is a philosophy: if you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. Use tools that give you this freedom.
>
> File over app is an appeal to tool makers: accept that all software is ephemeral, and give people ownership over their data.

— [File over app — Steph Ango](https://stephango.com/file-over-app)

Notebundle is a proposal for managing text notes and attachments that preserves as much freedom and compatibility with existing systems as possible, without requiring a dedicated syntax or protocol, while allowing the convenience scripts and software people use to work according to a common standard.

## Convention

- **The name of a Notebundle directory must end in `.notebundle`.** (Required)

    Just as ordinary file extensions are useful,
    ordinary directories and Notebundle directories should be immediately distinguishable.

- **A Notebundle’s note file must have the same name as the Notebundle, or be named `note`.** (Required)

    When converting the Markdown note `lorem ipsum.md` into a Notebundle, the result should be one of the following:

    - `lorem ipsum.notebundle/lorem ipsum.md`
    - `lorem ipsum.notebundle/note.md`

    The examples use the Markdown `.md` extension, but there are no restrictions on file extensions.

- **Place any attachments that should be bundled in the `attachments/` folder.** (Recommended)
    
    Attachments needed only by that note file are recommended to be placed in the `attachments/` folder inside `*.notebundle/`.

**The main goal of Notebundle is to help users make use of and manage their own notes in ways that suit their needs,** so the internal structure and the behavior of any scripts used with it may be adapted to individual needs.

## Support software

- **[obsidian-notebundle](https://github.com/leehan273/obsidian-notebundle)**

    Obsidian plugin that supports Notebundle natively.

- ...text editor and file explorer

## License

**Public License**

**CC0, No Rights Reserved**
