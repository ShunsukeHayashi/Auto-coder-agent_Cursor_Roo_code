# Auto-coder-agent with Devin

## 概要
このプロジェクトは、Devinを使用した自動コーディングエージェントのためのコードベースです。
ログ駆動開発（LDD）を採用し、AIとの対話履歴を効果的に管理・活用します。

## 特徴
- Devinとの対話履歴の自動保存
- ログ駆動開発（LDD）による開発管理
- 多言語対応（日本語/英語）
- メトリクスベースの品質管理

## ディレクトリ構造
```
.
├── .Devin/           # Devin関連の設定とルール
│   └── rules/        # Cursorのルールファイル
├── .specstory/       # 仕様とストーリーの履歴
│   ├── config.mdc    # SpecStory設定
│   ├── templates/    # ストーリーテンプレート
│   ├── current/      # 現在のストーリー
│   ├── archive/      # 完了したストーリー
│   └── history/      # 履歴ファイル
├── logs/             # LDDログ管理
│   ├── tasks/        # タスク実行ログ
│   ├── system/       # システムログ
│   ├── feedback/     # フィードバックログ
│   └── metrics/      # メトリクスログ
├── EN/               # 英語版ドキュメント
├── JA/               # 日本語版ドキュメント
├── docs/             # プロジェクトドキュメント
├── xnotes/           # 追加のノートと記録
├── @logging_template.mdc    # ロギングテンプレート
└── @memory-bank.mdc        # メモリーバンク
```

## LDDワークフロー

### 1. ログ駆動開発プロセス
1. タスク定義とログ作成
2. 実行と継続的ログ記録
3. フィードバックループ
4. メトリクス分析
5. 最適化と改善

### 2. ログカテゴリ
- **タスクログ**: 個別タスクの実行記録
- **システムログ**: システム全体の状態
- **フィードバックログ**: ユーザー・AI分析結果
- **メトリクスログ**: 品質・パフォーマンス指標

### 3. メモリーバンク活用
- 学習内容の蓄積
- コンテキスト管理
- 最適化履歴

## セットアップ
1. リポジトリのクローン:
```bash
git clone https://github.com/ShunsukeHayashi/Auto-coder-agent_Cursor_Roo_code.git
```

2. 必要なツール:
- Cursor（最新版）
- PowerShell 7以上
- Git
- SpecStory Cursor Extension

3. LDD環境の設定:
- ログディレクトリの確認
- テンプレートのカスタマイズ
- メトリクス収集の設定

## 使用方法

### 1. 基本的な使用方法
1. Cursorでプロジェクトを開く
2. AIとの対話を開始
3. すべての操作は自動的にログ記録

### 2. ログ管理
1. `@logging_template.mdc`に従ってログを記録
2. 適切なログカテゴリを選択
3. メトリクスの定期的な確認

### 3. フィードバックループ
1. タスク完了後のフィードバック記録
2. AI分析結果の統合
3. 改善提案の実装

## メトリクス管理
- コード品質指標
- パフォーマンス測定
- 進捗管理
- 最適化追跡

## 貢献
1. このリポジトリをフォーク
2. 新しいブランチを作成
3. 変更を加える
4. プルリクエストを送信

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。

## 関連リンク
- [SpecStory公式サイト](https://specstory.com/)
- [Cursor公式サイト](https://cursor.sh/)
- [プロジェクトドキュメント](./docs/)
