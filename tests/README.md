# テスト / Tests

このディレクトリには、Auto-coder-agent_Cursor_Roo_codeプロジェクトのテストが含まれています。
This directory contains tests for the Auto-coder-agent_Cursor_Roo_code project.

## テストの構造 / Test Structure

- `test_logging.py`: ログ機能のテスト / Tests for logging functionality
- `test_memory_bank.py`: メモリーバンク機能のテスト / Tests for memory bank functionality

## テストの実行方法 / How to Run Tests

### 前提条件 / Prerequisites

- Python 3.8以上 / Python 3.8 or higher
- unittest（Pythonの標準ライブラリ） / unittest (Python standard library)

### すべてのテストを実行 / Run All Tests

```bash
python -m unittest discover tests
```

### 特定のテストを実行 / Run Specific Tests

```bash
python -m unittest tests/test_logging.py
python -m unittest tests/test_memory_bank.py
```

## テストの追加 / Adding Tests

新しいテストを追加する場合は、以下のガイドラインに従ってください：
When adding new tests, please follow these guidelines:

1. 適切な命名規則を使用する（`test_*.py`） / Use appropriate naming conventions (`test_*.py`)
2. テストケースは`unittest.TestCase`を継承する / Test cases should inherit from `unittest.TestCase`
3. テストメソッドは`test_`で始める / Test methods should start with `test_`
4. 適切なアサーションを使用する / Use appropriate assertions
5. テストの目的を明確にするコメントを追加する / Add comments that clarify the purpose of the test

## テストカバレッジ / Test Coverage

テストカバレッジを確認するには、以下のコマンドを実行します：
To check test coverage, run the following command:

```bash
# coverageのインストール / Install coverage
pip install coverage

# カバレッジを測定してテストを実行 / Run tests with coverage measurement
coverage run -m unittest discover tests

# カバレッジレポートの表示 / Display coverage report
coverage report

# HTMLカバレッジレポートの生成 / Generate HTML coverage report
coverage html
```

## CI/CD統合 / CI/CD Integration

このテストスイートは、CI/CDパイプラインに統合することができます。`.github/workflows/`ディレクトリにワークフロー設定を追加することで、プルリクエストやプッシュ時に自動的にテストを実行できます。

This test suite can be integrated into CI/CD pipelines. By adding workflow configurations to the `.github/workflows/` directory, tests can be automatically run on pull requests or pushes.
