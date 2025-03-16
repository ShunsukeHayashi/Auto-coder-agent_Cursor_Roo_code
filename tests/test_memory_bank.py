"""
メモリーバンク機能のテストモジュール
Test module for memory bank functionality
"""

import os
import unittest
import tempfile
import shutil
from datetime import datetime


class TestMemoryBank(unittest.TestCase):
    """メモリーバンク機能のテストクラス / Test class for memory bank functionality"""

    def setUp(self):
        """テスト前の準備 / Setup before tests"""
        # テスト用の一時ディレクトリを作成 / Create temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        
        # テスト用のメモリーバンクファイルを作成 / Create test memory bank file
        self.memory_bank_content = """---
description: Memory bank for storing system state, configurations, and important information
version: 1.0.0
date: 2025-02-21
---

# System Memory Bank

## Environment Configuration
### Operating System
- Type: Windows
- Version: 10.0.26100
- Shell: PowerShell 7+

### Project Structure
- Base Path: /test/path
- Key Directories:
  - `.cursor/rules/`: Cursor rule definitions
  - `logs/`: System and operation logs
  - `docs/`: Project documentation
  - `xnotes/`: Additional notes and records

## Active States
### Current Tasks
- ID: TEST-001
- Status: In Progress
- Priority: High
- Dependencies: None

### System Status
- Last Operation: File Update
- Current State: Idle
- Active Processes: None

## Historical Data
### Completed Tasks
- Task History: TEST-000
- Success Rate: 100%
- Common Issues: None

### System Changes
- Configuration Changes: None
- Version Updates: 1.0.0
- Critical Events: None
"""
        
        self.memory_bank_file = os.path.join(self.test_dir, "@memory-bank.mdc")
        with open(self.memory_bank_file, "w", encoding="utf-8") as f:
            f.write(self.memory_bank_content)

    def tearDown(self):
        """テスト後のクリーンアップ / Cleanup after tests"""
        # テスト用の一時ディレクトリを削除 / Remove temporary directory
        shutil.rmtree(self.test_dir)

    def test_read_memory_bank(self):
        """メモリーバンク読み込みのテスト / Test memory bank reading"""
        # ファイルが存在することを確認 / Verify file exists
        self.assertTrue(os.path.exists(self.memory_bank_file))
        
        # ファイルの内容を読み込む / Read file contents
        with open(self.memory_bank_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 内容を確認 / Verify contents
        self.assertIn("System Memory Bank", content)
        self.assertIn("Environment Configuration", content)
        self.assertIn("Active States", content)
        self.assertIn("Historical Data", content)
        
        # 特定の値を確認 / Verify specific values
        self.assertIn("Type: Windows", content)
        self.assertIn("ID: TEST-001", content)
        self.assertIn("Status: In Progress", content)

    def test_update_memory_bank(self):
        """メモリーバンク更新のテスト / Test memory bank updating"""
        # ファイルの内容を読み込む / Read file contents
        with open(self.memory_bank_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 内容を更新 / Update contents
        updated_content = content.replace("Status: In Progress", "Status: Completed")
        updated_content = updated_content.replace("Current State: Idle", "Current State: Active")
        
        # 更新した内容を書き込む / Write updated contents
        with open(self.memory_bank_file, "w", encoding="utf-8") as f:
            f.write(updated_content)
        
        # 更新された内容を確認 / Verify updated contents
        with open(self.memory_bank_file, "r", encoding="utf-8") as f:
            new_content = f.read()
        
        self.assertIn("Status: Completed", new_content)
        self.assertIn("Current State: Active", new_content)
        self.assertNotIn("Status: In Progress", new_content)
        self.assertNotIn("Current State: Idle", new_content)

    def test_add_task_to_memory_bank(self):
        """メモリーバンクへのタスク追加のテスト / Test adding task to memory bank"""
        # ファイルの内容を読み込む / Read file contents
        with open(self.memory_bank_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 新しいタスクを追加 / Add new task
        task_section = """### Current Tasks
- ID: TEST-001
- Status: In Progress
- Priority: High
- Dependencies: None"""
        
        new_task_section = """### Current Tasks
- ID: TEST-001
- Status: In Progress
- Priority: High
- Dependencies: None
- ID: TEST-002
- Status: Planned
- Priority: Medium
- Dependencies: TEST-001"""
        
        updated_content = content.replace(task_section, new_task_section)
        
        # 更新した内容を書き込む / Write updated contents
        with open(self.memory_bank_file, "w", encoding="utf-8") as f:
            f.write(updated_content)
        
        # 更新された内容を確認 / Verify updated contents
        with open(self.memory_bank_file, "r", encoding="utf-8") as f:
            new_content = f.read()
        
        self.assertIn("ID: TEST-002", new_content)
        self.assertIn("Status: Planned", new_content)
        self.assertIn("Priority: Medium", new_content)
        self.assertIn("Dependencies: TEST-001", new_content)


if __name__ == "__main__":
    unittest.main()
