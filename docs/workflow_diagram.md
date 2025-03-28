# ワークフローダイアグラム / Workflow Diagram

このドキュメントは、OpenHands Devin AgentとAuto-coder-agent_Cursor_Roo_codeリポジトリのLog-Driven Development（LDD）メソドロジーの統合ワークフローを視覚化します。

This document visualizes the integrated workflow of the OpenHands Devin Agent and the Log-Driven Development (LDD) methodology in the Auto-coder-agent_Cursor_Roo_code repository.

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 全体ワークフロー / Overall Workflow

```
┌───────────────────────────────────────────────────────────────────┐
│                          PLAN フェーズ / PLAN Phase                │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐       │
│  │             │      │             │      │             │       │
│  │ ユーザー入力 │─────►│  意図分析   │─────►│  目標定義   │       │
│  │ User Input  │      │  Intent     │      │  Goal       │       │
│  │             │      │  Analysis   │      │  Definition │       │
│  └─────────────┘      └─────────────┘      └──────┬──────┘       │
│                                                   │              │
│                                                   ▼              │
│                                           ┌─────────────┐        │
│                                           │             │        │
│                                           │ タスク分解   │        │
│                                           │ Task        │        │
│                                           │ Breakdown   │        │
│                                           │             │        │
│                                           └──────┬──────┘        │
│                                                  │               │
│                       ┌────────────────────────┐ │               │
│                       │                        │ │               │
│                       │    ログエントリ作成    │◄┘               │
│                       │    Log Entry Creation  │                 │
│                       │                        │                 │
│                       └────────────┬───────────┘                 │
│                                    │                             │
└────────────────────────────────────┼─────────────────────────────┘
                                     │
                                     ▼
┌───────────────────────────────────────────────────────────────────┐
│                          ACT フェーズ / ACT Phase                  │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐       │
│  │             │      │             │      │             │       │
│  │ タスク実行   │─────►│  結果記録   │─────►│  結果評価   │       │
│  │ Task        │      │  Result     │      │  Result     │       │
│  │ Execution   │      │  Recording  │      │  Evaluation │       │
│  └─────────────┘      └─────────────┘      └──────┬──────┘       │
│         ▲                                          │              │
│         │                                          ▼              │
│         │                                  ┌─────────────┐        │
│         │                                  │             │        │
│         └──────────────────────────────────┤ フィードバック│        │
│                                           │ Feedback    │        │
│                                           │             │        │
│                                           └──────┬──────┘        │
│                                                  │               │
│                       ┌────────────────────────┐ │               │
│                       │                        │ │               │
│                       │    メトリクス収集      │◄┘               │
│                       │    Metrics Collection  │                 │
│                       │                        │                 │
│                       └────────────┬───────────┘                 │
│                                    │                             │
└────────────────────────────────────┼─────────────────────────────┘
                                     │
                                     ▼
┌───────────────────────────────────────────────────────────────────┐
│                     最適化サイクル / Optimization Cycle            │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐       │
│  │             │      │             │      │             │       │
│  │ メトリクス   │─────►│  パターン   │─────►│  改善提案   │       │
│  │ 分析        │      │  識別       │      │  Improvement│       │
│  │ Metrics     │      │  Pattern    │      │  Suggestions│       │
│  │ Analysis    │      │  Recognition│      └──────┬──────┘       │
│  └─────────────┘      └─────────────┘             │              │
│                                                   ▼              │
│                                           ┌─────────────┐        │
│                                           │             │        │
│                                           │ 計画適応    │        │
│                                           │ Plan        │        │
│                                           │ Adaptation  │        │
│                                           │             │        │
│                                           └──────┬──────┘        │
│                                                  │               │
│                                                  │               │
│                                                  │               │
│                                                  │               │
│                                                  │               │
│                                                  ▼               │
└───────────────────────────────────────────────────────────────────┘
                                     │
                                     │
                                     ▼
                          ┌─────────────────┐
                          │                 │
                          │  次のイテレーション │
                          │  Next Iteration  │
                          │                 │
                          └─────────────────┘
```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## PLANフェーズの詳細 / PLAN Phase Details

```
┌─────────────────────────────────────────────────────────────────┐
│                      PLAN フェーズ / PLAN Phase                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────┐                                              │
│  │ DevinAgent    │                                              │
│  ├───────────────┤                                              │
│  │ 意図分析       │                                              │
│  │ Intent Analysis│                                              │
│  └───────┬───────┘                                              │
│          │                                                      │
│          ▼                                                      │
│  ┌───────────────┐     ┌───────────────────────────────┐        │
│  │ PlanningSystem│     │ LDD                           │        │
│  ├───────────────┤     ├───────────────────────────────┤        │
│  │ 計画立案       │────►│ ログエントリ作成              │        │
│  │ Planning      │     │ Log Entry Creation            │        │
│  └───────────────┘     │                               │        │
│                        │ - タスクログ / Task Log        │        │
│                        │ - システムログ / System Log    │        │
│                        └───────────────────────────────┘        │
│                                                                 │
│  ┌───────────────┐     ┌───────────────────────────────┐        │
│  │ ContextManager│     │ メモリーバンク                 │        │
│  ├───────────────┤     ├───────────────────────────────┤        │
│  │ コンテキスト   │────►│ 状態更新                      │        │
│  │ 初期化        │     │ State Update                  │        │
│  │ Context       │     │                               │        │
│  │ Initialization│     │ - アクティブ状態 / Active State │        │
│  └───────────────┘     │ - 参照情報 / References        │        │
│                        └───────────────────────────────┘        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## ACTフェーズの詳細 / ACT Phase Details

```
┌─────────────────────────────────────────────────────────────────┐
│                      ACT フェーズ / ACT Phase                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────┐     ┌───────────────────────────────┐        │
│  │ PlanningSystem│     │ LDD                           │        │
│  ├───────────────┤     ├───────────────────────────────┤        │
│  │ ステップ実行   │────►│ タスク実行ログ                │        │
│  │ Step Execution│     │ Task Execution Log            │        │
│  └───────┬───────┘     │                               │        │
│          │             │ - 実行詳細 / Execution Details │        │
│          │             │ - コマンド履歴 / Command History│       │
│          │             └───────────────────────────────┘        │
│          │                                                      │
│          ▼                                                      │
│  ┌───────────────┐     ┌───────────────────────────────┐        │
│  │ PlanningSystem│     │ LDD                           │        │
│  ├───────────────┤     ├───────────────────────────────┤        │
│  │ 結果記録       │────►│ 結果ログ                      │        │
│  │ Result        │     │ Result Log                    │        │
│  │ Recording     │     │                               │        │
│  └───────┬───────┘     │ - 出力 / Output               │        │
│          │             │ - エラー / Errors              │        │
│          │             │ - 状態変化 / State Changes     │        │
│          │             └───────────────────────────────┘        │
│          │                                                      │
│          ▼                                                      │
│  ┌───────────────┐     ┌───────────────────────────────┐        │
│  │ ContextManager│     │ メモリーバンク                 │        │
│  ├───────────────┤     ├───────────────────────────────┤        │
│  │ コンテキスト   │────►│ 状態更新                      │        │
│  │ 更新          │     │ State Update                  │        │
│  │ Context       │     │                               │        │
│  │ Update        │     │ - 履歴データ / Historical Data │        │
│  └───────────────┘     │ - システム状態 / System State  │        │
│                        └───────────────────────────────┘        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## フィードバックと最適化サイクル / Feedback and Optimization Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│              フィードバックと最適化 / Feedback and Optimization    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────┐     ┌───────────────────────────────┐        │
│  │ LDD           │     │ AdvancedPlanningSystem        │        │
│  ├───────────────┤     ├───────────────────────────────┤        │
│  │ フィードバック │────►│ 計画適応                      │        │
│  │ 収集          │     │ Plan Adaptation               │        │
│  │ Feedback      │     │                               │        │
│  │ Collection    │     │ - 動的計画適応 / Dynamic Plan  │        │
│  └───────────────┘     │   Adaptation                  │        │
│                        │ - 依存関係追跡 / Dependency    │        │
│                        │   Tracking                    │        │
│                        └───────────────────────────────┘        │
│                                                                 │
│  ┌───────────────┐     ┌───────────────────────────────┐        │
│  │ LDD           │     │ ContextManager                │        │
│  ├───────────────┤     ├───────────────────────────────┤        │
│  │ メトリクス     │────►│ コンテキスト更新              │        │
│  │ 分析          │     │ Context Update                │        │
│  │ Metrics       │     │                               │        │
│  │ Analysis      │     │ - 学習履歴 / Learning History  │        │
│  └───────────────┘     │ - パターン / Patterns          │        │
│                        └───────────────────────────────┘        │
│                                                                 │
│  ┌───────────────────────────────────────────────────┐          │
│  │ 継続的改善サイクル / Continuous Improvement Cycle  │          │
│  │                                                   │          │
│  │  ┌─────┐     ┌──────┐     ┌──────┐     ┌─────┐   │          │
│  │  │     │     │      │     │      │     │     │   │          │
│  │  │計画 │────►│ 実行 │────►│ 確認 │────►│ 改善│   │          │
│  │  │Plan │     │ Do   │     │Check │     │ Act │   │          │
│  │  │     │     │      │     │      │     │     │   │          │
│  │  └─────┘     └──────┘     └──────┘     └─────┘   │          │
│  │     ▲                                     │      │          │
│  │     └─────────────────────────────────────┘      │          │
│  │                                                   │          │
│  └───────────────────────────────────────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## ログ記録の役割 / Role of Logging

```
┌─────────────────────────────────────────────────────────────────┐
│                  ログ記録の役割 / Role of Logging                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────────────────────────────────────────┐          │
│  │ ログカテゴリ / Log Categories                      │          │
│  │                                                   │          │
│  │  ┌─────────────┐   ┌─────────────┐               │          │
│  │  │ タスクログ   │   │ システムログ │               │          │
│  │  │ Task Logs   │   │ System Logs │               │          │
│  │  └─────────────┘   └─────────────┘               │          │
│  │                                                   │          │
│  │  ┌─────────────┐   ┌─────────────┐               │          │
│  │  │ フィードバック│   │ メトリクス   │               │          │
│  │  │ ログ         │   │ ログ        │               │          │
│  │  │ Feedback    │   │ Metrics     │               │          │
│  │  │ Logs        │   │ Logs        │               │          │
│  │  └─────────────┘   └─────────────┘               │          │
│  └───────────────────────────────────────────────────┘          │
│                                                                 │
│  ┌───────────────────────────────────────────────────┐          │
│  │ ログの役割 / Logging Roles                         │          │
│  │                                                   │          │
│  │  1. 透明性確保 / Transparency                      │          │
│  │     - 全ての操作を記録 / Record all operations     │          │
│  │     - 決定理由を文書化 / Document decision reasons │          │
│  │                                                   │          │
│  │  2. 分析基盤 / Analysis Foundation                 │          │
│  │     - パターン識別 / Pattern identification        │          │
│  │     - 問題検出 / Problem detection                 │          │
│  │                                                   │          │
│  │  3. 継続的改善 / Continuous Improvement            │          │
│  │     - 改善点の特定 / Identify improvement points   │          │
│  │     - 効果測定 / Measure effectiveness            │          │
│  │                                                   │          │
│  │  4. 知識蓄積 / Knowledge Accumulation             │          │
│  │     - 再利用可能な知識 / Reusable knowledge        │          │
│  │     - 学習履歴 / Learning history                 │          │
│  └───────────────────────────────────────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## コンテキスト維持 / Context Maintenance

```
┌─────────────────────────────────────────────────────────────────┐
│              コンテキスト維持 / Context Maintenance              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────────────────────────────────────────┐          │
│  │ コンテキスト管理 / Context Management              │          │
│  │                                                   │          │
│  │  ┌─────────────────────────────────────────────┐  │          │
│  │  │ DevinAgent - ContextManager                 │  │          │
│  │  │                                             │  │          │
│  │  │ - add_context_item()                        │  │          │
│  │  │ - set_task_info()                           │  │          │
│  │  │ - get_context_items_by_type()               │  │          │
│  │  │ - get_recent_context_items()                │  │          │
│  │  └─────────────────────────────────────────────┘  │          │
│  │                                                   │          │
│  │  ┌─────────────────────────────────────────────┐  │          │
│  │  │ LDD - メモリーバンク / Memory Bank           │  │          │
│  │  │                                             │  │          │
│  │  │ - 環境設定 / Environment Configuration       │  │          │
│  │  │ - アクティブ状態 / Active States             │  │          │
│  │  │ - 履歴データ / Historical Data               │  │          │
│  │  │ - システム参照 / System References           │  │          │
│  │  └─────────────────────────────────────────────┘  │          │
│  └───────────────────────────────────────────────────┘          │
│                                                                 │
│  ┌───────────────────────────────────────────────────┐          │
│  │ コンテキスト維持プロセス / Context Maintenance Process│          │
│  │                                                   │          │
│  │  1. 初期化 / Initialization                       │          │
│  │     - タスク情報の設定 / Set task information      │          │
│  │     - 環境情報の収集 / Collect environment info   │          │
│  │                                                   │          │
│  │  2. 継続的更新 / Continuous Update                │          │
│  │     - 操作結果の記録 / Record operation results   │          │
│  │     - 状態変化の追跡 / Track state changes        │          │
│  │                                                   │          │
│  │  3. コンテキスト検索 / Context Retrieval           │          │
│  │     - 関連情報の取得 / Get relevant information   │          │
│  │     - 過去の決定の参照 / Reference past decisions │          │
│  │                                                   │          │
│  │  4. 最適化 / Optimization                         │          │
│  │     - 不要データの削除 / Remove unnecessary data   │          │
│  │     - 重要情報の強調 / Emphasize important info   │          │
│  └───────────────────────────────────────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 結論 / Conclusion

このワークフローダイアグラムは、OpenHands Devin AgentとAuto-coder-agent_Cursor_Roo_codeのLDDメソドロジーがどのように統合されるかを示しています。PLANフェーズとACTフェーズを中心に、計画、実行、フィードバック、最適化のサイクルが継続的に繰り返されます。ログ記録はこのプロセス全体を通じて重要な役割を果たし、透明性の確保、分析基盤の提供、継続的改善の促進、知識の蓄積に貢献します。また、コンテキスト管理は、DevinのContextManagerとLDDのメモリーバンクを通じて、一貫性のある開発プロセスを実現します。

This workflow diagram shows how the OpenHands Devin Agent and the LDD methodology in Auto-coder-agent_Cursor_Roo_code are integrated. Centered around the PLAN and ACT phases, the cycle of planning, execution, feedback, and optimization is continuously repeated. Logging plays an important role throughout this process, contributing to ensuring transparency, providing an analysis foundation, promoting continuous improvement, and accumulating knowledge. Additionally, context management realizes a consistent development process through Devin's ContextManager and LDD's memory bank.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
