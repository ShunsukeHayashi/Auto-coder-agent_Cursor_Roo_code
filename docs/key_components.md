# 主要コンポーネント / Key Components

このドキュメントは、OpenHands Devin AgentとAuto-coder-agent_Cursor_Roo_codeリポジトリの主要コンポーネントを詳細に説明します。

This document details the key components of the OpenHands Devin Agent and the Auto-coder-agent_Cursor_Roo_code repository.

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## PlanningSystem / 計画システム

PlanningSystemは、DevinAgentの中核となる計画立案と実行管理のコンポーネントです。

PlanningSystem is the core component for planning and execution management in DevinAgent.

### 主要機能 / Key Features

1. **計画立案 / Plan Creation**
   - タスクを小さなステップに分割 / Break tasks into small steps
   - 依存関係の特定と管理 / Identify and manage dependencies
   - 実行順序の最適化 / Optimize execution order

2. **実行管理 / Execution Management**
   - 現在のステップの取得 / Get current step
   - ステップ実行結果の記録 / Record step results
   - 次のステップへの進行 / Advance to next step

3. **計画適応 / Plan Adaptation**
   - 実行結果に基づく計画の調整 / Adjust plan based on execution results
   - 新たな要件への対応 / Accommodate new requirements
   - エラー処理と回復 / Error handling and recovery

### 主要メソッド / Key Methods

```python
# 計画の作成 / Create a plan
create_plan(task_description: str) -> None

# 現在のステップの取得 / Get current step
get_current_step() -> Dict[str, Any]

# ステップ実行結果の記録 / Record step result
record_step_result(result: str, success: bool) -> None

# 次のステップへの進行 / Advance to next step
advance_to_next_step() -> None

# 計画の要約の取得 / Get plan summary
get_plan_summary() -> str
```

### LDDとの統合 / Integration with LDD

PlanningSystemは、LDDの計画フェーズと実行フェーズに対応しています。計画の作成はLDDのタスク定義とログエントリ作成に、実行管理はLDDのタスク実行ログとメトリクス収集に対応します。

PlanningSystem corresponds to the planning and execution phases of LDD. Plan creation corresponds to task definition and log entry creation in LDD, while execution management corresponds to task execution logging and metrics collection in LDD.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## AdvancedPlanningSystem / 高度計画システム

AdvancedPlanningSystemは、PlanningSystemを拡張し、より高度な計画機能を提供するコンポーネントです。

AdvancedPlanningSystem extends PlanningSystem and provides more advanced planning capabilities.

### 主要機能 / Key Features

1. **動的計画適応 / Dynamic Plan Adaptation**
   - 実行中の計画の動的な調整 / Dynamically adjust plans during execution
   - フィードバックに基づく計画の最適化 / Optimize plans based on feedback
   - 予期せぬ状況への対応 / Handle unexpected situations

2. **階層的計画 / Hierarchical Planning**
   - 複雑なタスクの階層的分解 / Hierarchical decomposition of complex tasks
   - サブタスクの管理 / Manage subtasks
   - 異なる抽象レベルでの計画 / Plan at different levels of abstraction

3. **依存関係追跡 / Dependency Tracking**
   - タスク間の依存関係の追跡 / Track dependencies between tasks
   - 並列実行の最適化 / Optimize parallel execution
   - クリティカルパスの特定 / Identify critical paths

### 主要メソッド / Key Methods

```python
# 計画の適応 / Adapt plan
adapt_plan(feedback: str, context_changes: Dict[str, Any]) -> None

# 階層的計画の作成 / Create hierarchical plan
create_hierarchical_plan(task_description: str, depth: int) -> None

# 依存関係の追加 / Add dependency
add_dependency(step_id: str, depends_on_step_id: str) -> None

# 並列実行可能なステップの取得 / Get parallel executable steps
get_parallel_executable_steps() -> List[Dict[str, Any]]
```

### LDDとの統合 / Integration with LDD

AdvancedPlanningSystemは、LDDのフィードバックフェーズと最適化フェーズに対応しています。動的計画適応はLDDのフィードバック分析と適用に、階層的計画と依存関係追跡はLDDのプロセスメトリクスと最適化に対応します。

AdvancedPlanningSystem corresponds to the feedback and optimization phases of LDD. Dynamic plan adaptation corresponds to feedback analysis and application in LDD, while hierarchical planning and dependency tracking correspond to process metrics and optimization in LDD.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## ContextManager / コンテキストマネージャー

ContextManagerは、タスク関連情報と実行結果を管理するコンポーネントです。

ContextManager is a component that manages task-related information and execution results.

### 主要機能 / Key Features

1. **コンテキスト管理 / Context Management**
   - コンテキストアイテムの追加と取得 / Add and retrieve context items
   - タスク情報の設定と取得 / Set and get task information
   - コンテキストの要約の生成 / Generate context summaries

2. **履歴追跡 / History Tracking**
   - 過去のコンテキストアイテムの保存 / Store past context items
   - タイプ別のコンテキストアイテムの検索 / Search context items by type
   - 最近のコンテキストアイテムの取得 / Get recent context items

3. **状態管理 / State Management**
   - 現在の状態の追跡 / Track current state
   - 状態変化の記録 / Record state changes
   - 状態の要約の生成 / Generate state summaries

### 主要メソッド / Key Methods

```python
# コンテキストアイテムの追加 / Add context item
add_context_item(item_type: str, content: str, metadata: Dict[str, Any] = None) -> None

# タスク情報の設定 / Set task information
set_task_info(task_description: str, task_id: str = None) -> None

# タスク情報の取得 / Get task information
get_task_info() -> Dict[str, Any]

# タイプ別のコンテキストアイテムの取得 / Get context items by type
get_context_items_by_type(item_type: str, limit: int = None) -> List[Dict[str, Any]]

# 最近のコンテキストアイテムの取得 / Get recent context items
get_recent_context_items(limit: int = 10) -> List[Dict[str, Any]]

# コンテキストの要約の取得 / Get context summary
get_context_summary() -> str
```

### LDDとの統合 / Integration with LDD

ContextManagerは、LDDのメモリーバンクに対応しています。コンテキスト管理はメモリーバンクの状態更新に、履歴追跡は履歴データの保存に、状態管理はシステム状態の追跡に対応します。

ContextManager corresponds to the memory bank in LDD. Context management corresponds to state updates in the memory bank, history tracking corresponds to historical data storage, and state management corresponds to system state tracking.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## WebBrowsingSystem / Webブラウジングシステム

WebBrowsingSystemは、Webページの閲覧と情報抽出のための機能を提供するコンポーネントです。

WebBrowsingSystem is a component that provides functionality for browsing web pages and extracting information.

### 主要機能 / Key Features

1. **Webページの閲覧 / Web Page Browsing**
   - URLの開閉 / Open and close URLs
   - ページ間の移動 / Navigate between pages
   - ブラウジング履歴の管理 / Manage browsing history

2. **情報抽出 / Information Extraction**
   - ページコンテンツの取得 / Get page content
   - 特定の情報の抽出 / Extract specific information
   - データの構造化 / Structure data

3. **Web要素との対話 / Web Element Interaction**
   - フォームの入力 / Fill forms
   - ボタンのクリック / Click buttons
   - ドロップダウンの選択 / Select from dropdowns

4. **ブラウザ状態の管理 / Browser State Management**
   - セッションの維持 / Maintain sessions
   - Cookieの管理 / Manage cookies
   - ブラウザ設定の制御 / Control browser settings

### 主要メソッド / Key Methods

```python
# URLを開く / Open URL
open_url(url: str) -> None

# ページコンテンツを取得 / Get page content
get_page_content() -> str

# 情報を抽出 / Extract information
extract_information(selector: str) -> str

# フォームに入力 / Fill form
fill_form(form_selector: str, data: Dict[str, str]) -> None

# ボタンをクリック / Click button
click_button(button_selector: str) -> None

# ブラウジング履歴を取得 / Get browsing history
get_browsing_history() -> List[str]
```

### LDDとの統合 / Integration with LDD

WebBrowsingSystemは、LDDの情報収集とリサーチフェーズに対応しています。Webページの閲覧と情報抽出は、LDDのリサーチログとナレッジベースの構築に貢献します。

WebBrowsingSystem corresponds to the information gathering and research phases of LDD. Web page browsing and information extraction contribute to research logging and knowledge base building in LDD.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## Tools / ツール

DevinAgentは、様々なタスクを実行するための多様なツールを提供します。

DevinAgent provides various tools for executing different tasks.

### 利用可能なツール / Available Tools

1. **シェルコマンド実行 / Shell Command Execution**
   - 名前 / Name: `shell`
   - 説明 / Description: シェルコマンドを実行します / Execute shell commands
   - パラメータ / Parameters: `command` (実行するシェルコマンド / Shell command to execute)

2. **ファイル読み込み / File Reading**
   - 名前 / Name: `read_file`
   - 説明 / Description: ファイルの内容を読み込みます / Read file contents
   - パラメータ / Parameters: `path` (読み込むファイルのパス / Path to the file to read)

3. **ファイル書き込み / File Writing**
   - 名前 / Name: `write_file`
   - 説明 / Description: ファイルに内容を書き込みます / Write content to a file
   - パラメータ / Parameters: 
     - `path` (書き込むファイルのパス / Path to the file to write)
     - `content` (書き込む内容 / Content to write)

4. **Webブラウジング / Web Browsing**
   - 名前 / Name: `browse`
   - 説明 / Description: URLを開いてWebページを閲覧します / Open URL and browse web pages
   - パラメータ / Parameters: `url` (開くURL / URL to open)
   - 注意 / Note: `enable_browsing=True` の場合のみ利用可能 / Only available if `enable_browsing=True`

5. **Python実行 / Python Execution**
   - 名前 / Name: `run_python`
   - 説明 / Description: Pythonコードを実行します / Execute Python code
   - パラメータ / Parameters: `code` (実行するPythonコード / Python code to execute)
   - 注意 / Note: `enable_jupyter=True` の場合のみ利用可能 / Only available if `enable_jupyter=True`

6. **LLMエディタ / LLM Editor**
   - 名前 / Name: `edit_code`
   - 説明 / Description: LLMを使用してコードを編集します / Edit code using LLM
   - パラメータ / Parameters: 
     - `path` (編集するファイルのパス / Path to the file to edit)
     - `instruction` (編集の指示 / Editing instructions)
   - 注意 / Note: `enable_llm_editor=True` の場合のみ利用可能 / Only available if `enable_llm_editor=True`

### ツールの使用例 / Tool Usage Examples

```python
# シェルコマンド実行 / Shell command execution
agent.use_tool("shell", {"command": "ls -la"})

# ファイル読み込み / File reading
content = agent.use_tool("read_file", {"path": "/path/to/file.txt"})

# ファイル書き込み / File writing
agent.use_tool("write_file", {"path": "/path/to/file.txt", "content": "Hello, world!"})

# Webブラウジング / Web browsing
agent.use_tool("browse", {"url": "https://example.com"})

# Python実行 / Python execution
result = agent.use_tool("run_python", {"code": "print('Hello, world!')"})

# LLMエディタ / LLM editor
agent.use_tool("edit_code", {"path": "/path/to/code.py", "instruction": "Add error handling"})
```

### LDDとの統合 / Integration with LDD

これらのツールは、LDDの実行フェーズとメトリクス収集フェーズに対応しています。シェルコマンド実行とファイル操作はLDDのタスク実行ログに、Webブラウジングはリサーチログに、Python実行とLLMエディタはコード品質メトリクスに貢献します。

These tools correspond to the execution and metrics collection phases of LDD. Shell command execution and file operations contribute to task execution logging in LDD, web browsing contributes to research logging, and Python execution and LLM editor contribute to code quality metrics.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## Codexエージェント / Codex Agent

Codexエージェントは、プロンプトチェーンとツール実行の記録を重視したコード生成特化エージェントであり、Cursor・Roo・Devinと連携してLDDプロセスを補完します。

The Codex agent focuses on prompt chaining and explicit tool execution logging to complement Cursor, Roo, and Devin within the LDD process.

### 主要機能 / Key Features

1. **プロンプトチェーン駆動 / Prompt-Chain Driven**
   - ユーザー意図から実装・検証までのステージを定義し、`codex_prompt_chain`に記録
   - Define stages from user intent through implementation and validation, storing them in the `codex_prompt_chain` log section

2. **ツール実行の可視化 / Tool Invocation Visibility**
   - テスト・リンター・フォーマッターの実行を`tool_invocations`に追記
   - Append test, linter, and formatter executions to `tool_invocations`

3. **検証マトリクス管理 / Validation Matrix Management**
   - 期待結果と実行結果を表形式で整理し、失敗ケースを明示
   - Organise expected vs. actual outcomes in tables to highlight failure cases

4. **ハンドオフ強化 / Handoff Enablement**
   - `handoff_summary`で次のエージェント向けに残課題と検証フックを提示
   - Provide pending items and verification hooks for the next agent within `handoff_summary`

### LDDとの統合 / Integration with LDD

CodexはLDDの計画フェーズでプロンプトチェーンを定義し、実行フェーズで成果をログに記録し、検証フェーズでメトリクスを更新、フィードバックフェーズでハンドオフノートを共有します。

Codex defines the prompt chain during the planning phase of LDD, records artefacts during execution, updates metrics during validation, and shares handoff notes during the feedback phase.

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## DevinAgent / Devinエージェント

DevinAgentは、上記のすべてのコンポーネントを統合し、自律的なソフトウェア開発を実現するエージェントです。

DevinAgent integrates all the above components to realize autonomous software development.

### 主要機能 / Key Features

1. **タスク理解と計画 / Task Understanding and Planning**
   - ユーザー入力の理解 / Understand user input
   - タスクの分解 / Decompose tasks
   - 実行計画の立案 / Create execution plans

2. **自律的な実行 / Autonomous Execution**
   - 計画に基づく実行 / Execute based on plans
   - ツールの適切な選択と使用 / Appropriately select and use tools
   - 結果の評価と適応 / Evaluate results and adapt

3. **コンテキスト認識 / Context Awareness**
   - タスク関連情報の管理 / Manage task-related information
   - 過去の実行結果の活用 / Utilize past execution results
   - 環境の変化への適応 / Adapt to environmental changes

4. **継続的な学習と改善 / Continuous Learning and Improvement**
   - フィードバックの収集と分析 / Collect and analyze feedback
   - パターンの識別と最適化 / Identify patterns and optimize
   - 知識の蓄積と活用 / Accumulate and utilize knowledge

### LDDとの統合 / Integration with LDD

DevinAgentは、LDDのすべてのフェーズ（計画、実行、フィードバック、最適化）に対応しています。タスク理解と計画はLDDの計画フェーズに、自律的な実行は実行フェーズに、コンテキスト認識はメモリーバンクに、継続的な学習と改善はフィードバックと最適化フェーズに対応します。

DevinAgent corresponds to all phases of LDD (planning, execution, feedback, optimization). Task understanding and planning correspond to the planning phase of LDD, autonomous execution corresponds to the execution phase, context awareness corresponds to the memory bank, and continuous learning and improvement correspond to the feedback and optimization phases.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
## 結論 / Conclusion

OpenHands Devin AgentとAuto-coder-agent_Cursor_Roo_codeのLDDメソドロジーは、相互補完的なコンポーネントを持ち、効率的なソフトウェア開発を実現します。DevinAgentのPlanningSystem、AdvancedPlanningSystem、ContextManager、WebBrowsingSystem、Toolsは、LDDの計画、実行、フィードバック、最適化の各フェーズと統合され、一貫性のある開発プロセスを提供します。

The OpenHands Devin Agent and the LDD methodology in Auto-coder-agent_Cursor_Roo_code have complementary components and realize efficient software development. DevinAgent's PlanningSystem, AdvancedPlanningSystem, ContextManager, WebBrowsingSystem, and Tools are integrated with the planning, execution, feedback, and optimization phases of LDD, providing a consistent development process.
◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
