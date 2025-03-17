"""
ログ機能のテストモジュール
Test module for logging functionality
"""

import os
import unittest
import tempfile
import shutil
import json
from datetime import datetime


class TestLogging(unittest.TestCase):
    """ログ機能のテストクラス / Test class for logging functionality"""

    def setUp(self):
        """テスト前の準備 / Setup before tests"""
        # テスト用の一時ディレクトリを作成 / Create temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.logs_dir = os.path.join(self.test_dir, "logs")
        self.tasks_dir = os.path.join(self.logs_dir, "tasks")
        self.system_dir = os.path.join(self.logs_dir, "system")
        self.feedback_dir = os.path.join(self.logs_dir, "feedback")
        self.metrics_dir = os.path.join(self.logs_dir, "metrics")
        
        # ディレクトリ構造を作成 / Create directory structure
        os.makedirs(self.tasks_dir, exist_ok=True)
        os.makedirs(self.system_dir, exist_ok=True)
        os.makedirs(self.feedback_dir, exist_ok=True)
        os.makedirs(self.metrics_dir, exist_ok=True)

    def tearDown(self):
        """テスト後のクリーンアップ / Cleanup after tests"""
        # テスト用の一時ディレクトリを削除 / Remove temporary directory
        shutil.rmtree(self.test_dir)

    def test_create_task_log(self):
        """タスクログ作成のテスト / Test task log creation"""
        # テスト用のタスクログを作成 / Create a test task log
        task_id = "TEST-001"
        task_title = "Test Task"
        task_description = "This is a test task"
        
        log_content = f"""---
id: {task_id}
title: {task_title}
description: {task_description}
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
status: In Progress
---

# {task_title}

## Description
{task_description}

## Steps
1. Step 1
2. Step 2
3. Step 3

## Results
- Result 1
- Result 2
"""
        
        log_file = os.path.join(self.tasks_dir, f"{task_id}_test_task.md")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(log_content)
        
        # ファイルが作成されたことを確認 / Verify file was created
        self.assertTrue(os.path.exists(log_file))
        
        # ファイルの内容を確認 / Verify file contents
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        self.assertIn(task_id, content)
        self.assertIn(task_title, content)
        self.assertIn(task_description, content)

    def test_create_metrics_log(self):
        """メトリクスログ作成のテスト / Test metrics log creation"""
        # テスト用のメトリクスログを作成 / Create a test metrics log
        metrics_data = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "code_quality": {
                "test_coverage": 85.5,
                "code_quality_score": 92.3,
                "technical_debt": "Low"
            },
            "performance": {
                "execution_time": 1.25,
                "memory_usage": "45MB",
                "response_time": 0.8
            },
            "process": {
                "completed_tasks": 5,
                "bug_rate": 0.05,
                "improvement_cycle_time": 3.5
            }
        }
        
        metrics_file = os.path.join(self.metrics_dir, "test_metrics.json")
        with open(metrics_file, "w", encoding="utf-8") as f:
            json.dump(metrics_data, f, indent=2)
        
        # ファイルが作成されたことを確認 / Verify file was created
        self.assertTrue(os.path.exists(metrics_file))
        
        # ファイルの内容を確認 / Verify file contents
        with open(metrics_file, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        
        self.assertEqual(loaded_data["code_quality"]["test_coverage"], 85.5)
        self.assertEqual(loaded_data["performance"]["execution_time"], 1.25)
        self.assertEqual(loaded_data["process"]["completed_tasks"], 5)

    def test_create_system_log(self):
        """システムログ作成のテスト / Test system log creation"""
        # テスト用のシステムログを作成 / Create a test system log
        system_log_content = f"""---
timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
type: system
level: info
---

# System Status Update

## Current State
- Memory Usage: 65%
- CPU Usage: 45%
- Disk Space: 75% free

## Active Processes
- Process 1: Running
- Process 2: Waiting
- Process 3: Completed

## Notifications
- No critical issues detected
- Scheduled maintenance in 2 days
"""
        
        system_file = os.path.join(self.system_dir, "test_system_log.md")
        with open(system_file, "w", encoding="utf-8") as f:
            f.write(system_log_content)
        
        # ファイルが作成されたことを確認 / Verify file was created
        self.assertTrue(os.path.exists(system_file))
        
        # ファイルの内容を確認 / Verify file contents
        with open(system_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        self.assertIn("System Status Update", content)
        self.assertIn("Memory Usage: 65%", content)
        self.assertIn("No critical issues detected", content)


if __name__ == "__main__":
    unittest.main()
