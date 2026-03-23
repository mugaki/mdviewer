# アーキテクチャ

## 全体構成

```mermaid
graph LR
    subgraph Client["ブラウザ (Client)"]
        A[index.html]
        B[marked.js]
        C[mermaid.js]
        D[highlight.js]
    end
    subgraph Server["Python サーバー (stdlib のみ)"]
        E[HTTPServer]
        F[FileWatcher]
        G[SSE Handler]
    end
    subgraph FS["ファイルシステム"]
        H[".md ファイル群"]
    end

    A -- HTTP --> E
    E -- SSE --> A
    E --> F
    F --> H
    A --> B
    A --> C
    A --> D
```

## 依存関係

| レイヤー   | ライブラリ       | バージョン | 読み込み方式 |
|-----------|-----------------|-----------|-------------|
| Markdown  | marked.js       | 13.x      | CDN         |
| 図        | mermaid.js      | 11.x      | CDN         |
| コード強調 | highlight.js    | 11.x      | CDN         |
| サーバー  | Python stdlib   | 3.8+      | 組み込み     |

外部への依存は**CDN のみ**（オフライン環境では動作しません）。
