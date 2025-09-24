#!/usr/bin/env bash
set -euo pipefail

REPO_URL=${1:-"https://github.com/ShunsukeHayashi/Auto-coder-agent_Cursor_Roo_code.git"}
WORKSPACE_ROOT=${WORKSPACE_ROOT:-"$HOME/repos"}
REPO_NAME="Auto-coder-agent_Cursor_Roo_code"
TARGET_DIR="${WORKSPACE_ROOT}/${REPO_NAME}"
PYTHON_BIN=${PYTHON_BIN:-"python3"}
VENV_DIR=${VENV_DIR:-"${TARGET_DIR}/.venv"}
REQUIREMENTS_FILE="affiliate_automation/requirements.txt"

mkdir -p "${WORKSPACE_ROOT}"

if [ ! -d "${TARGET_DIR}/.git" ]; then
  git clone "${REPO_URL}" "${TARGET_DIR}"
else
  git -C "${TARGET_DIR}" fetch --all --prune
  git -C "${TARGET_DIR}" reset --hard origin/main
fi

cd "${TARGET_DIR}"

if [ ! -d "${VENV_DIR}" ]; then
  "${PYTHON_BIN}" -m venv "${VENV_DIR}"
fi

# shellcheck disable=SC1090
source "${VENV_DIR}/bin/activate"

pip install --upgrade pip
if [ -f "${REQUIREMENTS_FILE}" ]; then
  pip install -r "${REQUIREMENTS_FILE}"
fi

if [ ! -f ".env" ]; then
  cat <<'ENV' > .env
# Codexクラウド環境用のサンプル設定
OPENAI_API_KEY=""
LOG_LEVEL="INFO"
ENV
fi

deactivate

echo "[Codex Init] リポジトリ: ${TARGET_DIR}"
echo "[Codex Init] 仮想環境: ${VENV_DIR}"
echo "[Codex Init] .env を作成しました (必要に応じてAPIキーを設定してください)"

echo "[Codex Init] LDDログディレクトリを検証します"
mkdir -p logs/tasks logs/system logs/metrics logs/feedback
for file in "@logging_template.mdc" "@memory-bank.mdc"; do
  if [ -f "$file" ]; then
    echo "[Codex Init] ${file} を確認しました"
  else
    echo "[Codex Init][WARN] ${file} が見つかりません"
  fi
done

echo "[Codex Init] 初期化シーケンスが完了しました"
