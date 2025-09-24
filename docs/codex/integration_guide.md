# Codexエージェント統合ガイド / Codex Agent Integration Guide

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 概要 / Overview

- CodexエージェントをAuto-coder-agent_Cursor_Roo_codeのLDDワークフローに組み込むためのベストプラクティスをまとめています。
- This guide explains how to onboard the Codex agent into the Log-Driven Development (LDD) workflow so it can collaborate with Cursor, Roo, and Devin agents.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

## 統合の柱 / Integration Pillars

### Codexクラウド初期化シーケンス / Cloud Init Sequence
- `codex/init_codex_cloud_env.sh` を実行し、クラウド環境でリポジトリ・仮想環境・依存関係を自動セットアップする。
- 詳細手順は `codex/cloud_init_sequence.mdc` を参照し、初期化結果を `codex_prompt_chain` セクションにログ化する。

1. **プロンプトチェーン管理 / Prompt Chain Management**
   - Codexはユーザー意図→計画→実装→検証の順でプロンプトを連結します。
   - Record each stage in task logs using the shared `@logging_template.mdc` so progress is auditable.

2. **ツール実行の明示化 / Explicit Tool Execution**
   - リンター、テスト、フォーマッターのコマンドはすべてCodexレスポンス内に記録し、結果をLDDメトリクスへ反映します。
   - Every command must be reproducible for CursorやRooが再実行しやすいようにする。

3. **メモリーバンク同期 / Memory Bank Synchronisation**
   - Prompt chain checkpoints, generated artefacts, and open issues are appended to `@memory-bank.mdc`.
   - これにより、他のエージェントが途中から作業を引き継いでもコンテキストを失いません。

4. **フィードバックループ / Feedback Loop**
   - Codex outputはSpecStoryとフィードバックログに反映し、次のイテレーションで改善ポイントを明確化します。

## ワークフロー / Workflow

| フェーズ / Phase | Codexアクション / Codex Action | LDD連携 / LDD Alignment |
|------------------|--------------------------------|-------------------------|
| 計画 / Planning | プロンプトチェーンの設計と制約定義 | タスクログに`codex_prompt_chain`セクションを追加 |
| 実行 / Execution | プロンプト送信と生成物の保存 | ログとメモリーバンクに成果を追記 |
| 検証 / Validation | テストと静的解析の実行 | メトリクスログに結果を記録 |
| 移譲 / Handoff | Cursor/Roo/Devin向けの次アクション整理 | フィードバックログとSpecStoryに要約 |

## ログテンプレートへの追加 / Logging Extensions

- `codex_prompt_chain`: 進行中のステージ、使用したプロンプト、得られた回答を要約。
- `tool_invocations`: 実行したコマンドとステータスを表形式で記録。
- `handoff_summary`: 次の担当エージェントに必要なアクション、残課題、検証フックを列挙。

## メモリ連携 / Memory Integration

```
### Codex Collaboration Snapshot
- Stage: {CURRENT_STAGE}
- Artefacts: {ARTEFACT_LIST}
- Tests: {TEST_RESULTS}
- Pending Follow-up: {FOLLOW_UPS}
```

上記スニペットをメモリーバンクに挿入することで、継続的なコンテキスト共有を実現します。

## マルチエージェント協調 / Multi-Agent Collaboration

- Cursor: Codexが作成したコードやログをレビューし、GUI/UX改善や追加調査を担当。
- Roo: プロジェクトルールとスタイル適用を強化し、Codexの実装を補完。
- Devin: Working Backwardsメソッドで大域的な計画を作成し、Codexのプロンプトチェーンと整合させる。

## ベストプラクティス / Best Practices

1. Codexに送信したプロンプトは再利用できるようテンプレート化して保管する。
2. 大きな変更はステージごとにコミットし、ログにコミットIDを残す。
3. 異常系・失敗例も必ずログへ記録し、次回のプロンプト改善に活用する。
4. 他エージェントとの引き継ぎ時は`handoff_summary`を必須項目として維持する。

## 参考ドキュメント / Related Documents

- `codex/README.md` – Codexディレクトリの構成と利用方法
- `codex/codex_agent_template.mdc` – プロンプトチェーンテンプレート
- `codex/ldd_integration.mdc` – LDD統合の詳細
- `docs/integration_mapping.md` – エージェント間統合マッピング（Devin・Codexを含む）
