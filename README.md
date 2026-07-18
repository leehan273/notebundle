
# Notebundle (WIP)

> Markdown 등의 노트 파일을 첨부파일까지 포함하여 하나의 노트로서 다루되, 특정 전용 형식이나 소프트웨어에 의존하지 않기 위한 아이디어


설명하기에 앞서 명확히하자면, **Notebundle은 특정 소프트웨어가 필수적인 새로운 파일 형식이 아닙니다.**

Notebundle은 첨부파일이 포함된 Markdown 노트를 작성하고 관리할 때 관행적으로 쓰여오던 파일 관리 형태를 (자동화가 가능할정도로) 조금 더 형식화한것입니다.

[TextBundle](https://textbundle.org/)을 아시는 분이라면, Notebundle은 Markdown과 TextBundle 사이의 영역에 위치하는 개념으로 이해하셔도 좋습니다(단독 Markdown 파일보다 통합적이면서 TextBundle보다 느슨함).

**Notebundle 아이디어의 중점은 '사용자 스스로가 자신의 노트를 자신의 용도에 맞게 활용하고, 관리하는 것'을 보조하는 것에 있습니다.**

자연스레, 이는 특정 소프트웨어의 사용이 필수적이어서는 안되며, 지나치게 형식적이어서 사용에 제약을 추가하는 형태가 되어서는 안됨을 의미합니다.

> File over app is a philosophy: if you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. Use tools that give you this freedom.
>
> File over app is an appeal to tool makers: accept that all software is ephemeral, and give people ownership over their data.

-- [File over app — Steph Ango](https://stephango.com/file-over-app)

Notebundle은 최대한의 자유와 기존 시스템과의 호환성을 유지하면서, 각자가 사용하는 편의 스크립트 / 소프트웨어가 어느정도 공통 규격으로 동작할 수 있도록 하기 위한 아이디어 제안입니다.

## Notebundle Example

이미지 첨부파일을 하나 참조하고 있는, `my-note.md` 라는 Markdown 파일이 존재한다고 가정합시다.
내용은 전혀 특별하지 않으며, 평범한 Markdown 파일입니다.

```markdown
# My Note

Lorem ipsum dolor sit amet

![Image](./attachments/image.png)
```

일반적인 경우, 실제 노트 폴더에서 `my-note.md`는 다음과 같은 방식으로 배치되어있을 것입니다.

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

이러한 방식은 매우 일반적이지만, 이와 같이 구성되어있는 경우 특정 노트 파일의 위치를 이동할 때 해당 노트에서 참조되는 첨부파일 또한 (다른 노트의 첨부파일들이 뒤섞여있는 폴더 내에서) 찾아 이동시켜야합니다. 사용하는 편집 프로그램에 따라 이를 자동으로 지원하기도 하지만, 수정을 거쳐 참조 라인이 누락된 파일, 첨부했을때 다른 노트의 첨부파일과 파일명이 겹치는 경우 발생하는 추가 관리 등 여전히 여러 번거로움이 존재합니다.

노트 프로젝트의 루트에 `all-attachments/` 등의 통합 첨부파일 폴더등을 만들어 사용하면 일부 문제는 해결 가능하나, 해당 프로젝트로부터 노트를 분리하기 어려워지는 것과 통합 첨부파일 폴더가 비대해져 관리하기 어려워지는 문제가 새로 발생합니다.

---

Notebundle 방식을 사용하여 앞선 예시의 `my-note.md`를 `my-note.notebundle`로 변경하면 다음과 같은 형태가 됩니다.
(이때, `my-note.notebundle`는 별도의 특별한 동작이 존재하지 않는 일반적인 디렉토리입니다.)

```text
my-note.notebundle/
├── attachments/
│   └── image.png
└── my-note.md
```

> `my-note` 등의 명칭을 중복 관리하는것을 원치 않을 경우, 다음과 같이 컨텐츠 파일을 `note.*` 형태로 명명하는것도 가능합니다.
> 
> ```text
> my-note.notebundle/
> ├── attachments/
> │   └── image.png
> └── note.md
> ```

`my-note.notebundle/my-note.md` 파일의 콘텐츠는 앞선 예시로부터 아무것도 변경될 필요가 없습니다.

이제, `my-note.md`만을 `my-note.notebundle`로 변환한 이후의 `notes/` 폴더의 모습을 다시 정리해봅시다.

```text
notes/
├── attachments/
│   └── ...
├── note-1.md
├── note-2.md
├── note-3.md
└── my-note.notebundle/
    ├── attachments/
    │   └── image
    └── my-note.md
```

- 이제 `my-note.notebundle` 디렉토리를 그대로 이동 및 복사하여, 해당 노트 파일 및 첨부파일을 놓치지 않고 한번에 조작할 수 있습니다.
- 다른 Markdown 파일에서 기존 `my-note.md` 로의 참조 역시, `[my-note-link](./my-note.notebundle/my-note.md)` 처럼 변경해주기만 하면 그대로 동작합니다.
- `.notebundle` 이라는 특징적인 접미사를 가지고 있기 때문에, 파일 탐색 인터페이스에서도 해당 디렉토리가 (미지의 중첩 구조를 가진 것이 아닌) 실질적으로 개별 노트로서 취급 가능한 것임을 즉각적으로 인지할 수 있습니다.

이처럼 Notebundle은 첨부파일을 참조하는 노트를, 하나의 노트 파일당 하나의 `.notebundle` 접미사가 붙는 디렉토리로 분리하는 개념입니다.

특정 소프트웨어에 의존해야만 생성 가능한 파일 형태가 아니기 때문에 특정 소프트웨어에 얽매일 필요가 없으며, 파일 내용에는 영향을 미치지 않기 때문에 기존에 사용하던 프로그램의 호환성이 그대로 유지되며, 동시에 변환 및 관리를 자동화할 수 있을 정도의 공통 구조를 가지고 있습니다.


## Notebundle specification (recommendation)

- **Notebundle 디렉토리의 명칭은 `.notebundle`로 끝나야합니다.**  

    일반 파일 확장자가 필요한 이유와 마찬가지로, 해당 폴더가 일반 폴더인지 Notebundle 폴더인지 구별 가능해야합니다.

- **Notebundle 내 주요 콘텐츠 파일은 하나일 것을 전제합니다.**  

    기본적으로, 하나의 Notebundle은 하나의 개별 노트로서 취급해야합니다.

- **Notebundle의 컨텐츠가 되는 파일은 Notebundle의 명칭과 동일하거나, `note.*`여야합니다.**  

    Markdown 파일이 주요 콘텐츠인 `lorem-ipsum.notebundle` 라는 Notebundle의 경우, 해당 Notebundle의 주요 콘텐츠 파일명은 `lorem-ipsum.md` 혹은 `note.md` 여야합니다.

- **내장해야하는 첨부파일은 `attachments/` 폴더에 배치합니다.**  
    
    노트 파일을 이동, 복사할 때 함께 작업이 이루어지길 원하는 첨부파일은 `*.notebundle/` 내 `attachments/` 폴더에 배치합니다.

    단, 참조하는 모든 파일을 `attachments/` 폴더에 배치해야할 의무는 없습니다.

**의도적으로, 엄격한 제한 사항이나 상세 동작들은 규정하지 않습니다.**

Markdown과 마찬가지로 느슨합니다. Markdown 파일 내에 어떤 특이한 문법이나 내용이 작성되어있어도 그것을 Markdown 파일이라 부르는것처럼, Notebundle은 자유롭게 활용 가능해야합니다.

**Notebundle의 중점은 '사용자 스스로가 자신의 노트를 자신의 용도에 맞게 활용하고, 관리하는것'을 보조하기 위한 것입니다.** 사용자 본인이 자신의 파일을 활용하는데에 있어서 방해가 되어선 안됩니다.

## 호환 소프트웨어

- 모든 파일 탐색기
- 파일 시스템 위에서 동작하는 모든 파일 편집기

Notebundle 개념은 디렉토리를 자유롭게 사용할 수 있는 파일 시스템에 기반하므로, 콘텐츠 관리를 내부의 자체 데이터베이스에 전적으로 의존하는 노트 작성 프로그램에서는 활용하기가 어렵습니다.

Notebundle 개념을 활용하기에 유리한, 파일 시스템상에서 그대로 동작하는 편집기의 예시로는 [VSCode](https://code.visualstudio.com/), [Obsidian](https://obsidian.md/), [Zettlr](https://www.zettlr.com/) 등이 있습니다.

Notebundle은 Markdown 노트를 관리하는 것을 기준으로 구상되었으나, Markdown 이외의 활용 또한 고려할 수 있습니다.

### Notebundle을 직접 지원하는 소프트웨어

현재 작업중입니다.

- [notebundle-poc](./notebundle-poc/README.md) (현재 레포지토리에 포함되어있는 `notebundle-poc` 파이썬 프로젝트)

    Markdown - Notebundle - TextBundle 간 자동 변환 및 Notebundle 검증의 실험적 구현입니다.
    
    해당 poc의 세부적인 동작이 Notebundle 아이디어의 표준 동작을 규정하지는 않습니다.

- obsidian-notebundle (WIP)

    현재 작업중으로, Obsidian에서 Notebundle 관련 편의 기능을 지원하는 플러그인이 될 예정입니다.

## LICENSE

**Public License**

**CC0, No Rights Reserved**

본 저장소 내의 컨텐츠는 CC0으로 배포됩니다.

단, `notebundle-poc/example-files/` 내 파일은 CC0 라이선스에 해당하지 않습니다.
