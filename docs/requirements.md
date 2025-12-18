# 要件概要

- リージョン: Azure 東日本
- 実行基盤: Azure Functions（Consumption Plan）
- 実装言語: Python 3.11
- エンドポイント: `/test`
- HTTPメソッド: GET を推奨（ブラウザでクエリを直接指定して結果確認）
- 入力: クエリパラメータ `A` と `B`（整数のみ、必須）と演算指定用の `op`（`mul` または `div`、省略時は `mul`）
- 提供機能: 掛け算（mul）と割り算（div）の2種類の演算
- レスポンス形式: JSON
- エラー処理: 入力欠如・不正な数値・0除算などは HTTP 400 を返す
- デプロイ: 手動で実施（CI/CD は対象外）

## API 仕様（概要）
- エンドポイント: GET /test
- クエリパラメータ:
  - `A` (integer, 必須)
  - `B` (integer, 必須)
  - `op` (string, 任意, `mul`|`div`, デフォルト `mul`)
- 正常レスポンス (HTTP 200, JSON):
  - `{
    "operation": "mul|div",
    "inputs": {"A": 2, "B": 3},
    "result": 6
  }
- エラー時レスポンス (HTTP 400, JSON):
  - `{
    "error": "説明文（例: B が 0 のため割り算不可）"
  }

## 入力検証
- `A` と `B` の存在チェック
- `A` と `B` が整数であることの検証（文字列や浮動小数点はエラー）
- `op` が `mul` または `div` 以外はエラー（もしくはデフォルト適用）
- `div` の場合は `B != 0` を必須とする

## 実装メモ
- 関数名案: `TestFunction`（HTTP トリガー）
- ルート設定: `route`: `test`
- 必要ファイル: `requirements.txt`（`azure-functions` など）
- レスポンスは JSON を返し、ブラウザで直接確認できるようにする
