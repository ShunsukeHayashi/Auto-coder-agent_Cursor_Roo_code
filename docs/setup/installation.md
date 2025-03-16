# インストールガイド / Installation Guide

## 前提条件 / Prerequisites
このプロジェクトを使用するには、以下のソフトウェアが必要です：
The following software is required to use this project:

- Cursor IDE (最新版 / latest version)
- Git 2.30.0+
- PowerShell 7+ (Windows) または / or Bash (Linux/macOS)
- Node.js 16+ (オプション / optional)
- Python 3.8+ (オプション / optional)

## インストール手順 / Installation Steps

### 1. リポジトリのクローン / Clone the Repository
```bash
git clone https://github.com/ShunsukeHayashi/Auto-coder-agent_Cursor_Roo_code.git
cd Auto-coder-agent_Cursor_Roo_code
```

### 2. Cursor IDEのセットアップ / Cursor IDE Setup
1. [Cursor公式サイト](https://cursor.sh/)から最新版をダウンロードしてインストールします。
   Download and install the latest version from the [Cursor official site](https://cursor.sh/).

2. Cursorを起動し、クローンしたリポジトリを開きます。
   Launch Cursor and open the cloned repository.

3. Cursor拡張機能の確認：
   Verify Cursor extensions:
   - SpecStory拡張機能がインストールされていることを確認します。
   - Ensure the SpecStory extension is installed.

### 3. 環境設定 / Environment Configuration

#### Windows環境の場合 / For Windows Environment
PowerShellスクリプトを実行してルールを適用します：
Run the PowerShell script to apply rules:
```powershell
.\apply-rules.ps1
```

#### Linux/macOS環境の場合 / For Linux/macOS Environment
Bashスクリプトを実行してルールを適用します：
Run the Bash script to apply rules:
```bash
chmod +x apply-rules.sh
./apply-rules.sh
```

### 4. ログディレクトリの確認 / Verify Log Directories
以下のディレクトリが存在することを確認します：
Verify that the following directories exist:
```bash
ls -la logs/
```

必要に応じて、不足しているディレクトリを作成します：
Create any missing directories if necessary:
```bash
mkdir -p logs/tasks logs/system logs/feedback logs/metrics
```

### 5. 設定の確認 / Verify Configuration
メモリーバンクの設定を確認します：
Check the memory bank configuration:
```bash
cat @memory-bank.mdc
```

必要に応じて、環境に合わせて設定を調整します。
Adjust settings according to your environment if necessary.

## トラブルシューティング / Troubleshooting

### 一般的な問題 / Common Issues

#### ルール適用エラー / Rule Application Errors
ルール適用スクリプトでエラーが発生した場合：
If errors occur in the rule application script:
1. スクリプトの実行権限を確認します。
   Check the script execution permissions.
2. 必要に応じて手動でルールファイルをコピーします。
   Manually copy rule files if necessary.

#### ログディレクトリエラー / Log Directory Errors
ログディレクトリに関するエラーが発生した場合：
If errors occur related to log directories:
1. 必要なディレクトリを手動で作成します。
   Manually create the necessary directories.
2. ディレクトリのアクセス権限を確認します。
   Check directory access permissions.

#### Cursor拡張機能の問題 / Cursor Extension Issues
Cursor拡張機能に関する問題が発生した場合：
If issues occur with Cursor extensions:
1. Cursorを再起動します。
   Restart Cursor.
2. 拡張機能を再インストールします。
   Reinstall the extension.

## 次のステップ / Next Steps
インストールが完了したら、[使用ガイド](../usage/getting_started.md)を参照して、プロジェクトの使用方法を学びましょう。
After installation is complete, refer to the [Usage Guide](../usage/getting_started.md) to learn how to use the project.
