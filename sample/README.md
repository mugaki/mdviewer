# Markdown Viewer サンプル

軽量Markdownビューアーのデモファイルです。

## 見出し

### 3階層目の見出し

#### 4階層目の見出し

---

## テキスト装飾

**太字**、*イタリック*、~~打ち消し~~、`インラインコード`

> これはブロッククォートです。
> 引用文を表示するのに使います。

---

## リスト

### 箇条書き

- アイテム1
- アイテム2
  - ネストされたアイテム
  - もう一つ
- アイテム3

### 番号付きリスト

1. 最初のステップ
2. 次のステップ
3. 最後のステップ

---

## コードブロック

```python
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")
```

```bash
# サーバー起動
python viewer.py ./sample
```

---

## テーブル

| 言語       | パラダイム     | 用途              |
|------------|---------------|-------------------|
| Python     | マルチパラダイム | AI / スクリプト   |
| JavaScript | プロトタイプ   | Web フロントエンド |
| Rust       | 所有権モデル   | システム / WebAssembly |
| Go         | 並行指向       | バックエンド API  |

---

## Mermaid ダイアグラム

### フローチャート

```mermaid
flowchart TD
    A[ファイルを選択] --> B{Markdownか?}
    B -- Yes --> C[パース & レンダリング]
    B -- No  --> D[エラー表示]
    C --> E[Mermaid図を検出]
    E --> F[SVGに変換]
    F --> G[表示完了]
```

### シーケンス図

```mermaid
sequenceDiagram
    participant Browser as ブラウザ
    participant Server  as Pythonサーバー
    participant FS      as ファイルシステム

    Browser->>Server: GET /api/files
    Server->>FS: ディレクトリ走査
    FS-->>Server: ファイル一覧
    Server-->>Browser: JSON レスポンス

    Browser->>Server: GET /api/file?path=README.md
    Server->>FS: ファイル読み込み
    FS-->>Server: Markdownテキスト
    Server-->>Browser: テキストレスポンス

    loop ファイル監視 (SSE)
        FS-->>Server: 変更を検知
        Server-->>Browser: reload イベント
        Browser->>Browser: 自動リロード
    end
```

### クラス図

```mermaid
classDiagram
    class MarkdownViewer {
        +String rootDir
        +int port
        +start()
        +stop()
    }
    class FileWatcher {
        +Path directory
        +watch()
        +notifyClients()
    }
    class HTTPHandler {
        +handleFiles()
        +handleFile()
        +handleSSE()
    }
    MarkdownViewer --> FileWatcher
    MarkdownViewer --> HTTPHandler
```

---

## リンク・画像

[marked.js ドキュメント](https://marked.js.org/)
[mermaid.js ドキュメント](https://mermaid.js.org/)

---

## 数式っぽい表現

コードブロックで数式を表現することもできます:

```
E = mc²
∑(i=1 to n) i = n(n+1)/2
```
