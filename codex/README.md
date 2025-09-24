# Codex Agent Integration

## Overview

This directory provides templates and integration guides that adapt the Auto-coder-agent_Cursor_Roo_code repository for use with the Codex agent. The resources here extend the existing Cursor and Roo workflows so that Codex can participate in the Log-Driven Development (LDD) process with consistent logging, context management, and metric tracking.

## Contents

- `codex_agent_template.mdc`: Prompt-chaining oriented template for Codex agent executions
- `ldd_integration.mdc`: Mapping between Codex agent behaviour and the LDD system
- `README.md`: This file

## Codexクラウド初期化

Codexクラウド環境で本リポジトリを利用する際は、`init_codex_cloud_env.sh` を実行して初期セットアップを行ってください。詳細な手順は
`cloud_init_sequence.mdc` にまとめています。

1. スクリプトをダウンロードし、実行します。
2. `.env` に `OPENAI_API_KEY` を設定します。
3. LDDログテンプレートとメモリバンクの存在を確認します。
4. Codexに読み込ませる `Agent.md` を `codex/agent/` 配下に配置します。

初期化後は、以下のプロンプトチェーンおよびツール実行手順に従ってください。

## Prompt Chaining & Tool Orchestration

The Codex agent is expected to:

1. Build a prompt chain that moves from user intent → plan → implementation → validation
2. Record each stage of the chain in standardised log sections so that other agents can review the reasoning trail
3. Invoke tooling (tests, linters, formatters) explicitly and document their outcomes for reproducibility
4. Feed structured artefacts back into the Memory Bank to keep shared context synchronised

## Integration with LDD

Codex leverages the existing LDD assets by:

- Re-using the shared logging templates with Codex-specific sections for prompt chaining
- Writing execution traces into the Memory Bank so Cursor, Roo, and Devin agents can resume work seamlessly
- Aligning generated stories and plans with SpecStory archives for long-term traceability
- Following the Cursor ruleset to guarantee consistent style, safety, and communication standards

## Usage

1. Start with `codex_agent_template.mdc` when orchestrating Codex runs inside this repository
2. Populate the prompt chain placeholders (intent, plan, draft, review, tests) before sending Codex requests
3. Mirror every Codex action in the LDD logs so other agents can audit or hand over tasks
4. Consult `docs/codex/integration_guide.md` for detailed workflows and best practices shared by all agents

## Visual Format

Codex contributions should continue to use the standard `◤◢` framed blocks for highlighted context to remain visually aligned with existing documentation and templates.
