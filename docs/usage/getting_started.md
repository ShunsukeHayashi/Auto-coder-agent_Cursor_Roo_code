# 使用ガイド / Usage Guide

## はじめに / Introduction
このガイドでは、Auto-coder-agent_Cursor_Roo_codeの基本的な使用方法を説明します。
This guide explains the basic usage of Auto-coder-agent_Cursor_Roo_code.

## 基本的なワークフロー / Basic Workflow

### 1. プロジェクトを開く / Open the Project
Cursor IDEでプロジェクトを開きます：
Open the project in Cursor IDE:
1. Cursorを起動します。
   Launch Cursor.
2. `File > Open Folder`を選択し、クローンしたリポジトリのディレクトリを選択します。
   Select `File > Open Folder` and choose the cloned repository directory.

### 2. AIとの対話を開始 / Start Interaction with AI
Cursor IDEのAIアシスタント機能を使用して対話を開始します：
Use the AI assistant feature in Cursor IDE to start interaction:
1. `Ctrl+K`（または`Cmd+K`）を押してAIアシスタントを呼び出します。
   Press `Ctrl+K` (or `Cmd+K`) to invoke the AI assistant.
2. 質問やタスクを入力します。
   Enter your question or task.

### 3. ログの確認 / Check Logs
すべての対話は自動的にログに記録されます。ログを確認するには：
All interactions are automatically logged. To check logs:
1. `logs/`ディレクトリ内の適切なカテゴリを開きます。
   Open the appropriate category in the `logs/` directory.
2. 最新のログファイルを確認します。
   Check the latest log file.

### 4. メモリーバンクの活用 / Utilize Memory Bank
メモリーバンクを活用して、コンテキストを維持します：
Utilize the memory bank to maintain context:
1. `@memory-bank.mdc`ファイルを確認します。
   Check the `@memory-bank.mdc` file.
2. 必要に応じて、重要な情報を追加します。
   Add important information as needed.

## 主要な機能 / Key Features

### 1. ログ駆動開発（LDD） / Log-Driven Development (LDD)
LDDワークフローに従って開発を進めます：
Follow the LDD workflow for development:
1. タスク定義とログエントリ作成
   Task definition and log entry creation
2. 継続的ログ記録
   Continuous logging
3. フィードバック分析
   Feedback analysis
4. 改善実施
   Implementation of improvements

### 2. SpecStory活用 / Utilizing SpecStory
SpecStoryを使用して開発ストーリーを管理します：
Use SpecStory to manage development stories:
1. `.specstory/templates/`からテンプレートを使用して新しいストーリーを作成します。
   Create new stories using templates from `.specstory/templates/`.
2. ストーリーのステータスを更新します。
   Update story status.
3. 完了したストーリーをアーカイブします。
   Archive completed stories.

### 3. メトリクス収集 / Metrics Collection
開発メトリクスを収集して品質を向上させます：
Collect development metrics to improve quality:
1. コード品質メトリクス
   Code quality metrics
2. パフォーマンスメトリクス
   Performance metrics
3. プロセスメトリクス
   Process metrics

## 高度な使用方法 / Advanced Usage

### 1. カスタムルールの作成 / Creating Custom Rules
Cursorのルールをカスタマイズします：
Customize Cursor rules:
1. `.cursor/rules/`ディレクトリに新しいルールファイルを作成します。
   Create a new rule file in the `.cursor/rules/` directory.
2. 既存のルールファイルを参考にフォーマットを設定します。
   Set the format referring to existing rule files.
3. ルール適用スクリプトを実行して変更を適用します。
   Run the rule application script to apply changes.

### 2. フィードバックループの最適化 / Optimizing Feedback Loop
フィードバックループを最適化して開発効率を向上させます：
Optimize the feedback loop to improve development efficiency:
1. フィードバックの収集方法を定義します。
   Define how to collect feedback.
2. 分析プロセスを確立します。
   Establish an analysis process.
3. 改善サイクルを短縮します。
   Shorten the improvement cycle.

### 3. メトリクス分析の自動化 / Automating Metrics Analysis
メトリクス分析を自動化して継続的な改善を促進します：
Automate metrics analysis to promote continuous improvement:
1. 分析スクリプトを作成します。
   Create analysis scripts.
2. 定期的な実行をスケジュールします。
   Schedule regular execution.
3. 結果に基づいて自動的に改善提案を生成します。
   Automatically generate improvement suggestions based on results.

## 次のステップ / Next Steps
より詳細な情報については、以下のドキュメントを参照してください：
For more detailed information, refer to the following documents:
- [LDDワークフロー](../ldd/workflow.md)
- [メトリクス管理](../metrics/overview.md)
- [フィードバックループ](../feedback/overview.md)
