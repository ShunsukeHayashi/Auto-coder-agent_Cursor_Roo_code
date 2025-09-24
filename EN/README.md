# Auto-coder-agent_Cursor_Roo_code

## Overview
This project is a codebase for automated coding workflows powered by Cursor, Roo, and Codex agents.
It adopts Log-Driven Development (LDD) to effectively manage and utilize multi-agent interaction history.

## Features
- Automatic saving of Cursor / Codex AI interaction history
- Development management through Log-Driven Development (LDD)
- Multilingual support (Japanese/English)
- Metrics-based quality management
- Prompt-chaining templates and integration guides for the Codex agent

## Directory Structure
```
EN/
├── @logging_template.mdc    # Logging Template
├── @memory-bank.mdc        # Memory Bank (Execution History & Context)
├── .logs/                  # Log Files Directory
└── docs/                   # Documentation
```

## Setup
1. Verify Required Files
2. Configure Logging Template
3. Initialize Memory Bank
4. Verify Environment Settings

## Usage

### 1. Basic Usage
1. Open the project in Cursor
2. Start AI interaction
3. All operations are automatically logged

### 2. Log Management
1. Record logs according to `@logging_template.mdc`
2. Select appropriate log categories
3. Reflect outputs from Cursor, Roo, Codex, and Devin agents in the metrics

### 3. Feedback Loop
1. Record feedback after task completion
2. Integrate AI analysis results from Cursor, Roo, Codex, and Devin
3. Implement improvement suggestions

## Development Process
- LDD-based Development Cycle
- Utilization of Feedback Loop
- Continuous Improvement and Optimization

## Metrics
- Code Quality Indicators
- Test Coverage
- Documentation Completeness
- Rule Optimization Effects

## License
This project is released under the MIT License.
