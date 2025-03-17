# 貢献ガイドライン / Contribution Guidelines

## はじめに / Introduction
Auto-coder-agent_Cursor_Roo_codeプロジェクトへの貢献に興味をお持ちいただき、ありがとうございます。このガイドラインは、プロジェクトへの貢献方法を説明します。
Thank you for your interest in contributing to the Auto-coder-agent_Cursor_Roo_code project. These guidelines explain how to contribute to the project.

## 貢献の種類 / Types of Contributions
以下のような様々な方法でプロジェクトに貢献できます：
You can contribute to the project in various ways:

1. **バグ報告 / Bug Reports**
   - 発見したバグを報告する
   - Report bugs you discover

2. **機能リクエスト / Feature Requests**
   - 新機能のアイデアを提案する
   - Suggest ideas for new features

3. **ドキュメント改善 / Documentation Improvements**
   - ドキュメントの追加や修正
   - Add or modify documentation

4. **コード貢献 / Code Contributions**
   - バグ修正や新機能の実装
   - Fix bugs or implement new features

5. **テスト追加 / Adding Tests**
   - 単体テストや統合テストの追加
   - Add unit tests or integration tests

## 貢献プロセス / Contribution Process

### 1. 問題の作成 / Create an Issue
新しい貢献を始める前に、まず問題（Issue）を作成してください：
Before starting a new contribution, first create an issue:

1. GitHubリポジトリの「Issues」タブを開きます。
   Open the "Issues" tab in the GitHub repository.

2. 「New Issue」ボタンをクリックします。
   Click the "New Issue" button.

3. 適切なテンプレートを選択し、必要な情報を入力します。
   Select the appropriate template and fill in the required information.

4. 「Submit new issue」をクリックして問題を作成します。
   Click "Submit new issue" to create the issue.

### 2. フォークとクローン / Fork and Clone
リポジトリをフォークしてローカル環境にクローンします：
Fork the repository and clone it to your local environment:

1. GitHubリポジトリページの右上にある「Fork」ボタンをクリックします。
   Click the "Fork" button in the top right of the GitHub repository page.

2. フォークしたリポジトリをローカル環境にクローンします：
   Clone the forked repository to your local environment:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Auto-coder-agent_Cursor_Roo_code.git
   cd Auto-coder-agent_Cursor_Roo_code
   ```

3. オリジナルリポジトリをリモートとして追加します：
   Add the original repository as a remote:
   ```bash
   git remote add upstream https://github.com/ShunsukeHayashi/Auto-coder-agent_Cursor_Roo_code.git
   ```

### 3. ブランチの作成 / Create a Branch
新しい機能やバグ修正のためのブランチを作成します：
Create a branch for a new feature or bug fix:

```bash
git checkout -b feature/your-feature-name
# または / or
git checkout -b fix/your-bug-fix
```

### 4. 変更の実装 / Implement Changes
ローカル環境で変更を実装します：
Implement changes in your local environment:

1. コードエディタで必要な変更を行います。
   Make the necessary changes in your code editor.

2. プロジェクトのコーディング規約に従ってください。
   Follow the project's coding conventions.

3. 適切なテストを追加または更新します。
   Add or update appropriate tests.

4. ドキュメントを更新します（必要な場合）。
   Update documentation (if necessary).

### 5. 変更のコミット / Commit Changes
変更をコミットします：
Commit your changes:

```bash
git add .
git commit -m "feat: Add new feature" # または / or "fix: Fix bug in ..."
```

コミットメッセージは[Conventional Commits](https://www.conventionalcommits.org/)の形式に従ってください。
Follow the [Conventional Commits](https://www.conventionalcommits.org/) format for commit messages.

### 6. 変更のプッシュ / Push Changes
変更をフォークしたリポジトリにプッシュします：
Push changes to your forked repository:

```bash
git push origin feature/your-feature-name
```

### 7. プルリクエストの作成 / Create a Pull Request
GitHubでプルリクエスト（PR）を作成します：
Create a Pull Request (PR) on GitHub:

1. フォークしたリポジトリページに移動します。
   Go to your forked repository page.

2. 「Compare & pull request」ボタンをクリックします。
   Click the "Compare & pull request" button.

3. PRの詳細を入力します：
   Fill in the PR details:
   - タイトル：変更内容を簡潔に説明
   - 説明：変更の詳細、関連する問題へのリンク
   - Title: Briefly explain the changes
   - Description: Details of changes, links to related issues

4. 「Create pull request」をクリックしてPRを作成します。
   Click "Create pull request" to create the PR.

## コーディング規約 / Coding Conventions

### 一般的なガイドライン / General Guidelines
- 一貫性のあるコードスタイルを維持する
  Maintain consistent code style
- 適切なコメントを追加する
  Add appropriate comments
- 複雑なロジックは説明する
  Explain complex logic
- 変数名と関数名は明確で説明的にする
  Make variable and function names clear and descriptive

### 言語固有のガイドライン / Language-Specific Guidelines

#### Markdown
- 見出しは階層構造に従う
  Headings follow hierarchical structure
- コードブロックは言語を指定する
  Specify language for code blocks
- リンクは適切に機能することを確認する
  Ensure links function properly

#### JavaScript/TypeScript
- ESLintの規則に従う
  Follow ESLint rules
- 非同期処理はPromiseまたはasync/awaitを使用する
  Use Promises or async/await for asynchronous operations
- 型定義を適切に行う（TypeScript）
  Define types appropriately (TypeScript)

#### Python
- PEP 8スタイルガイドに従う
  Follow PEP 8 style guide
- docstringを使用して関数とクラスを文書化する
  Document functions and classes using docstrings
- 型ヒントを使用する（Python 3.6+）
  Use type hints (Python 3.6+)

## テスト / Testing
新しい機能やバグ修正には、適切なテストを追加してください：
Add appropriate tests for new features or bug fixes:

1. 単体テストは`tests/`ディレクトリに追加します。
   Add unit tests to the `tests/` directory.

2. テストを実行して、すべてのテストがパスすることを確認します：
   Run tests to ensure all tests pass:
   ```bash
   # テスト実行コマンド（プロジェクトによって異なる場合があります）
   # Test execution command (may vary depending on the project)
   npm test # または / or pytest
   ```

## レビュープロセス / Review Process
プルリクエストは以下のプロセスでレビューされます：
Pull requests are reviewed with the following process:

1. 自動チェック（CI）がパスすることを確認します。
   Ensure automatic checks (CI) pass.

2. プロジェクトメンテナがコードをレビューします。
   Project maintainers review the code.

3. フィードバックがある場合は、必要な変更を行います。
   Make necessary changes if there is feedback.

4. すべての要件を満たしたら、PRがマージされます。
   Once all requirements are met, the PR will be merged.

## コミュニティ / Community
質問や議論は、以下のチャネルで行うことができます：
Questions and discussions can be conducted through the following channels:

- GitHub Issues
- GitHub Discussions
- プロジェクトのコミュニティチャット（存在する場合）
  Project community chat (if it exists)

## 行動規範 / Code of Conduct
すべての貢献者は、プロジェクトの行動規範に従うことが期待されます。詳細は[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)を参照してください。
All contributors are expected to follow the project's code of conduct. For details, refer to [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).
