# Hello Function App (ローカル実行用)

このリポジトリには Azure Functions の HTTP トリガー `test` を想定したスケルトン実装が含まれます。ローカルで簡単に動作確認するための手順は以下です。

1. Python3.11 を使って依存関係をインストールする（任意）:

```bash
python -m pip install -r requirements.txt
```

2. ローカルの簡易検証（Azure Functions Core Tools が不要な簡易モード）:

```bash
python -m src.test_function 2 3 mul
```

出力例:

{
  "operation": "mul",
  "inputs": {"A": 2, "B": 3},
  "result": 6
}

3. Azure へデプロイする場合は、Azure Functions Core Tools を使用して手動デプロイしてください（手順は別途記載します）。
