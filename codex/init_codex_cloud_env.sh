#!/usr/bin/env bash
set -euo pipefail

#=== 基本設定 / Base Configuration ===#
REPO_URL=${REPO_URL:-"https://github.com/ShunsukeHayashi/Auto-coder-agent_Cursor_Roo_code.git"}
TARGET_BRANCH=${TARGET_BRANCH:-"main"}
WORKSPACE_ROOT=${WORKSPACE_ROOT:-"$HOME/repos"}
REPO_NAME=${REPO_NAME:-"Auto-coder-agent_Cursor_Roo_code"}
TARGET_DIR="${WORKSPACE_ROOT}/${REPO_NAME}"
PYTHON_BIN=${PYTHON_BIN:-"python3"}
VENV_DIR=${VENV_DIR:-"${TARGET_DIR}/.venv"}
REQUIREMENTS_FILE=${REQUIREMENTS_FILE:-"affiliate_automation/requirements.txt"}

mkdir -p "${WORKSPACE_ROOT}"

clone_repository() {
  if [ ! -d "${TARGET_DIR}/.git" ]; then
    echo "[Codex Init] リポジトリが見つかりません。新規クローンを開始します。"
    git clone --branch "${TARGET_BRANCH}" "${REPO_URL}" "${TARGET_DIR}"
    return
  fi

  echo "[Codex Init] 既存のリポジトリを検出しました。最新状態へ更新します。"
  (
    cd "${TARGET_DIR}"
    if [ -n "$(git status --porcelain)" ]; then
      echo "[Codex Init][WARN] 未コミットの変更があります。更新前に退避してください。" >&2
    fi
    git fetch origin
    git checkout "${TARGET_BRANCH}"
    git pull --ff-only origin "${TARGET_BRANCH}"
  )
}

setup_virtualenv() {
  if [ ! -d "${VENV_DIR}" ]; then
    echo "[Codex Init] 仮想環境を作成します (${VENV_DIR})"
    "${PYTHON_BIN}" -m venv "${VENV_DIR}"
  else
    echo "[Codex Init] 既存の仮想環境を使用します (${VENV_DIR})"
  fi

  # shellcheck disable=SC1090
  source "${VENV_DIR}/bin/activate"
  pip install --upgrade pip
  if [ -f "${TARGET_DIR}/${REQUIREMENTS_FILE}" ]; then
    pip install -r "${TARGET_DIR}/${REQUIREMENTS_FILE}"
  else
    echo "[Codex Init][INFO] ${REQUIREMENTS_FILE} は見つかりませんでした。追加の依存は手動でインストールしてください。"
  fi
  deactivate
}

bootstrap_env_file() {
  local env_file="${TARGET_DIR}/.env"
  if [ -f "${env_file}" ]; then
    echo "[Codex Init] 既存の .env を保持します。"
    return
  fi

  cat <<'ENV' > "${env_file}"
# Codexクラウド環境用のサンプル設定
OPENAI_API_KEY=""
LOG_LEVEL="INFO"
CODEX_AGENT_PROFILE="default"
LDD_LOG_ROOT="logs"
ENV
  echo "[Codex Init] サンプル .env を生成しました。必要な値を設定してください。"
}

prepare_ldd_assets() {
  echo "[Codex Init] LDD関連アセットを確認します。"
  (
    cd "${TARGET_DIR}"
    mkdir -p logs/tasks logs/system logs/metrics logs/feedback
    for file in "@logging_template.mdc" "@memory-bank.mdc"; do
      if [ -f "$file" ]; then
        echo "[Codex Init] ${file} を確認しました。"
      else
        echo "[Codex Init][WARN] ${file} が見つかりません。必要に応じて追加してください。"
      fi
    done
  )
}

main() {
  clone_repository
  setup_virtualenv
  bootstrap_env_file
  prepare_ldd_assets

  cat <<INFO
[Codex Init] 初期化が完了しました。
[Codex Init] リポジトリ: ${TARGET_DIR}
[Codex Init] ブランチ:    ${TARGET_BRANCH}
[Codex Init] 仮想環境:    ${VENV_DIR}
INFO
}

main "$@"
