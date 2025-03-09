"""
ロギングユーティリティモジュール

このモジュールは、LDDアプローチに基づいたロギング機能を提供します。
"""

import logging
import os
from datetime import datetime
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    ロガーを取得します
    
    Args:
        name: ロガーの名前
        level: ロギングレベル
    
    Returns:
        設定されたロガー
    """
    logger = logging.getLogger(name)
    
    # ロガーが既に設定されている場合は、そのまま返す
    if logger.handlers:
        return logger
    
    logger.setLevel(level)
    
    # コンソールハンドラの設定
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # フォーマッタの設定
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    # ハンドラの追加
    logger.addHandler(console_handler)
    
    return logger

def log_task(task_id: str, description: str, status: str = "started") -> None:
    """
    タスクログを記録します
    
    Args:
        task_id: タスクID
        description: タスクの説明
        status: タスクのステータス
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = os.path.join(os.getcwd(), "logs", "tasks")
    
    # ディレクトリが存在しない場合は作成
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"{task_id}.md")
    
    # ファイルが存在しない場合は新規作成
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"# タスクログ: {description}\n\n")
            f.write("## 基本情報\n")
            f.write(f"- タスクID: {task_id}\n")
            f.write(f"- 開始日時: {timestamp}\n")
            f.write(f"- 状態: {status}\n")
            f.write("- 担当: AI Assistant\n\n")
            f.write("## タスク概要\n")
            f.write(f"{description}\n\n")
            f.write("## 実行ログ\n\n")
    else:
        # 既存のファイルに追記
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"### {timestamp} - {status}\n")
            f.write(f"{description}\n\n")

def log_system(category: str, message: str) -> None:
    """
    システムログを記録します
    
    Args:
        category: ログのカテゴリ
        message: ログメッセージ
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = os.path.join(os.getcwd(), "logs", "system")
    
    # ディレクトリが存在しない場合は作成
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"{category}.md")
    
    # ファイルが存在しない場合は新規作成
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"# システムログ: {category}\n\n")
            f.write("## ログエントリ\n\n")
    
    # ログの追記
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"### {timestamp}\n")
        f.write(f"{message}\n\n")

def log_feedback(source: str, content: str, rating: Optional[int] = None) -> None:
    """
    フィードバックログを記録します
    
    Args:
        source: フィードバックの送信元
        content: フィードバックの内容
        rating: 評価（1-5）
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = os.path.join(os.getcwd(), "logs", "feedback")
    
    # ディレクトリが存在しない場合は作成
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"{source}.md")
    
    # ファイルが存在しない場合は新規作成
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"# フィードバックログ: {source}\n\n")
            f.write("## フィードバックエントリ\n\n")
    
    # ログの追記
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"### {timestamp}")
        if rating is not None:
            f.write(f" - 評価: {rating}/5")
        f.write("\n")
        f.write(f"{content}\n\n")

def log_metrics(category: str, metrics: dict) -> None:
    """
    メトリクスログを記録します
    
    Args:
        category: メトリクスのカテゴリ
        metrics: メトリクスデータ
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = os.path.join(os.getcwd(), "logs", "metrics")
    
    # ディレクトリが存在しない場合は作成
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"{category}.md")
    
    # ファイルが存在しない場合は新規作成
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"# メトリクスログ: {category}\n\n")
            f.write("## メトリクスエントリ\n\n")
    
    # ログの追記
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"### {timestamp}\n")
        for key, value in metrics.items():
            f.write(f"- {key}: {value}\n")
        f.write("\n")
