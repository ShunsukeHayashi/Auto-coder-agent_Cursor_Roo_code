# 意図分析構造 / Intent Analysis Structure

このドキュメントは、Auto-coder-agent_Cursor_Roo_codeリポジトリとOpenHands Devin Agentで使用される意図分析構造を説明します。

This document explains the intent analysis structure used in the Auto-coder-agent_Cursor_Roo_code repository and OpenHands Devin Agent.

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 基本構造 / Basic Structure

```
[Input] → [User Intent] → [Intent]
[Input] → [User Intent] → [Want or Need Intent]
```

この構造は、ユーザー入力から意図を抽出し、それを具体的な目標に変換するプロセスを表します。

This structure represents the process of extracting intent from user input and converting it into specific goals.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 目標定義 / Goal Definition

```
[Fixed User Want Intent] = Defined Goal
```

ユーザーの意図から抽出された「欲しいもの」は、明確な目標として定義されます。これにより、曖昧な要求が具体的な達成目標に変換されます。

The "want" extracted from the user's intent is defined as a clear goal. This converts ambiguous requests into specific achievement targets.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## タスク分解 / Task Breakdown

```
Achieve Goal == Need Tasks
[Goal] = [Tasks]
```

定義された目標は、達成するために必要なタスクに分解されます。各タスクは具体的で実行可能な単位です。

The defined goal is broken down into tasks needed to achieve it. Each task is a specific, executable unit.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## タスク実行要件 / Task Execution Requirements

タスク実行には以下の要素が必要です：

1. **プロンプト (Prompt)**: タスクを実行するための指示
2. **ツール (Tools)**: タスク実行に必要なツールやリソース
3. **エージェント割り当て (Agent Assignment)**: タスクを実行する担当エージェント

Task execution requires the following elements:

1. **Prompt**: Instructions for executing the task
2. **Tools**: Tools and resources needed for task execution
3. **Agent Assignment**: The agent responsible for executing the task
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 実装フィードバックループ / Implementation Feedback Loop

```
┌─────────────────┐
│                 │
│  タスク定義     │
│  Task Definition│
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│  タスク実行     │
│  Task Execution │
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│  結果評価       │
│  Result         │
│  Evaluation     │
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│  フィードバック │
│  Feedback       │
│                 │
└────────┬────────┘
         │
         └─────────► (次のタスクまたは再実行)
                    (Next task or re-execution)
```

タスク実行後、結果は評価され、フィードバックが生成されます。このフィードバックは次のタスクの実行や、必要に応じて同じタスクの再実行に活用されます。

After task execution, the results are evaluated and feedback is generated. This feedback is used for the execution of the next task or, if necessary, re-execution of the same task.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 実際の例 / Practical Example

### ユーザー入力 / User Input
```
新しいWebアプリケーションのログイン機能を実装してください。
Please implement a login feature for a new web application.
```

### 意図分析 / Intent Analysis
```
[Input] → [User Intent] → [Intent](Webアプリケーション開発)
[Input] → [User Intent] → [Want Intent](ログイン機能の実装)
```

### 目標定義 / Goal Definition
```
[Fixed User Want Intent] = ユーザー認証システムの実装
[Fixed User Want Intent] = Implementation of user authentication system
```

### タスク分解 / Task Breakdown
```
[Goal] = [Tasks]
1. データベースユーザーモデルの設計
2. ログインフォームのUI実装
3. 認証ロジックの実装
4. セッション管理の実装
5. セキュリティ対策の実装
```

### タスク実行要件（タスク1の例） / Task Execution Requirements (Example for Task 1)
```
- プロンプト: データベースにユーザー情報を格納するためのモデルを設計する
- ツール: データベース設計ツール、SQLエディタ
- エージェント: データベース設計エージェント
```

### フィードバックループ / Feedback Loop
```
- タスク実行: データベースモデルの設計と実装
- 結果評価: モデルの完全性、セキュリティ、パフォーマンスの評価
- フィードバック: パスワードハッシュ化の強化が必要
- 再実行: セキュリティ強化を含むモデルの修正
```
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## ログ記録の統合 / Logging Integration

意図分析とタスク実行の各ステップは、LDDメソドロジーに従ってログに記録されます：

1. **タスクログ**: タスク定義、実行、結果
2. **システムログ**: システム状態、リソース使用状況
3. **フィードバックログ**: 評価結果、改善提案
4. **メトリクスログ**: パフォーマンス指標、品質メトリクス

Each step of intent analysis and task execution is logged according to the LDD methodology:

1. **Task Logs**: Task definition, execution, results
2. **System Logs**: System state, resource usage
3. **Feedback Logs**: Evaluation results, improvement suggestions
4. **Metrics Logs**: Performance indicators, quality metrics
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## メモリーバンクとの連携 / Memory Bank Integration

意図分析の結果とタスク実行の履歴は、メモリーバンク（@memory-bank.mdc）に保存され、将来の意思決定に活用されます：

```
## Active States
### Current Tasks
- ID: LOGIN-001
- Status: IN_PROGRESS
- Priority: HIGH
- Dependencies: USER-MODEL-001

### System Status
- Last Operation: USER_MODEL_CREATION
- Current State: AWAITING_FEEDBACK
- Active Processes: DB_MIGRATION
```

The results of intent analysis and the history of task execution are stored in the memory bank (@memory-bank.mdc) and used for future decision-making.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 結論 / Conclusion

意図分析構造は、ユーザー入力から具体的なタスクへの変換プロセスを体系化し、効率的な開発を可能にします。この構造はOpenHands Devin AgentとAuto-coder-agent_Cursor_Roo_codeの両方で活用され、一貫性のある開発プロセスを実現します。

The intent analysis structure systematizes the process of converting user input into specific tasks, enabling efficient development. This structure is utilized in both OpenHands Devin Agent and Auto-coder-agent_Cursor_Roo_code, realizing a consistent development process.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
