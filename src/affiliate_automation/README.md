# アフィリエイト記事自動生成エージェント

## 概要
このモジュールは、マッチングアプリに関するアフィリエイト記事を自動生成するエージェントを提供します。
テンプレート化された記事構造に基づいて、マッチングアプリの比較・紹介記事を効率的に生成します。

## 機能
- マッチングアプリの比較記事の自動生成
- 記事構造のテンプレート化と再利用
- アフィリエイトリンクの自動挿入
- 記事のカスタマイズ（ターゲット年齢層、目的など）
- Markdown形式での出力

## ディレクトリ構造
```
affiliate_automation/
├── README.md                 # このファイル
├── __init__.py               # パッケージ初期化
├── article_generator.py      # 記事生成のメインクラス
├── templates/                # 記事テンプレート
│   ├── __init__.py
│   ├── base_template.py      # 基本テンプレート
│   ├── matching_apps.py      # マッチングアプリ専用テンプレート
│   └── sections/             # 記事セクションテンプレート
│       ├── __init__.py
│       ├── introduction.py   # 導入部分
│       ├── comparison.py     # 比較セクション
│       └── conclusion.py     # 結論部分
├── content/                  # コンテンツ生成
│   ├── __init__.py
│   ├── content_generator.py  # コンテンツ生成ロジック
│   └── data_sources.py       # データソース管理
├── affiliate/                # アフィリエイト管理
│   ├── __init__.py
│   ├── link_manager.py       # リンク管理
│   └── tracking.py           # トラッキング機能
└── utils/                    # ユーティリティ
    ├── __init__.py
    ├── logger.py             # ロギングユーティリティ
    ├── metrics.py            # 品質メトリクス
    └── formatter.py          # 出力フォーマッタ
```

## 使用方法
```python
from affiliate_automation.article_generator import ArticleGenerator

# 記事ジェネレーターの初期化
generator = ArticleGenerator(template_type="matching_apps")

# 記事生成パラメータの設定
params = {
    "target_age": "30代",
    "purpose": "婚活",
    "apps_count": 5,
    "include_pricing": True,
    "include_user_reviews": True
}

# 記事の生成
article = generator.generate_article(params)

# Markdown形式で出力
markdown_content = article.to_markdown()
print(markdown_content)

# ファイルに保存
with open("matching_apps_article.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)
```

## 開発ステータス
- 初期開発段階
- テンプレートエンジンの実装中
- コンテンツ生成ロジックの開発予定
- アフィリエイトリンク管理の実装予定

## 貢献
プルリクエストやイシューは歓迎します。大きな変更を加える前には、まずイシューを開いて議論してください。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。
