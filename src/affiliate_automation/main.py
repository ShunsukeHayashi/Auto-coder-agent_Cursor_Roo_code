"""
アフィリエイト記事自動生成システムのメインモジュール

このモジュールは、アフィリエイト記事自動生成システムのエントリーポイントを提供します。
"""

import argparse
import json
import os
import sys
from typing import Dict, Any, List, Optional
import logging

from .article_generator import ArticleGenerator
from .content.content_generator import ContentGenerator
from .affiliate.link_manager import LinkManager
from .utils.logger import get_logger, log_task, log_metrics

# ロガーの設定
logger = get_logger(__name__)

def parse_args():
    """コマンドライン引数を解析します"""
    parser = argparse.ArgumentParser(description="アフィリエイト記事自動生成システム")
    
    parser.add_argument(
        "--template",
        type=str,
        default="matching_apps",
        help="使用するテンプレート（デフォルト: matching_apps）"
    )
    
    parser.add_argument(
        "--params",
        type=str,
        help="JSONフォーマットのパラメータ（例: '{\"target_age\": \"30代\", \"purpose\": \"婚活\"}'）"
    )
    
    parser.add_argument(
        "--params-file",
        type=str,
        help="パラメータを含むJSONファイルのパス"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default="article.md",
        help="出力ファイルのパス（デフォルト: article.md）"
    )
    
    parser.add_argument(
        "--log-task",
        action="store_true",
        help="タスクログを記録する"
    )
    
    parser.add_argument(
        "--log-metrics",
        action="store_true",
        help="メトリクスログを記録する"
    )
    
    return parser.parse_args()

def load_params(args) -> Dict[str, Any]:
    """パラメータを読み込みます"""
    params = {}
    
    # JSONパラメータの解析
    if args.params:
        try:
            params = json.loads(args.params)
        except json.JSONDecodeError as e:
            logger.error(f"JSONパラメータの解析エラー: {e}")
            sys.exit(1)
    
    # パラメータファイルの読み込み
    elif args.params_file:
        try:
            with open(args.params_file, "r", encoding="utf-8") as f:
                params = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger.error(f"パラメータファイルの読み込みエラー: {e}")
            sys.exit(1)
    
    return params

def main():
    """メイン関数"""
    # 引数の解析
    args = parse_args()
    
    # パラメータの読み込み
    params = load_params(args)
    
    # デフォルトパラメータの設定
    if not params:
        params = {
            "target_age": "30代",
            "purpose": "婚活",
            "apps_count": 5,
            "include_pricing": True,
            "include_user_reviews": True
        }
    
    # タスクログの記録
    if args.log_task:
        task_id = f"AFFILIATE-{params.get('target_age', 'general')}-{params.get('purpose', 'general')}"
        log_task(
            task_id,
            f"マッチングアプリのアフィリエイト記事生成: {params.get('target_age', '')}向け{params.get('purpose', '')}アプリ紹介",
            "started"
        )
    
    try:
        # 記事生成
        logger.info("記事生成を開始します")
        article_generator = ArticleGenerator(args.template)
        article = article_generator.generate_article(params)
        
        # 記事の保存
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(article.to_markdown())
        
        logger.info(f"記事を保存しました: {args.output}")
        
        # メトリクスログの記録
        if args.log_metrics:
            metrics = {
                "template": args.template,
                "target_age": params.get("target_age", ""),
                "purpose": params.get("purpose", ""),
                "apps_count": params.get("apps_count", 0),
                "sections_count": len(article.sections),
                "word_count": len(article.to_markdown().split()),
                "character_count": len(article.to_markdown())
            }
            log_metrics("article_generation", metrics)
        
        # タスク完了ログ
        if args.log_task:
            log_task(
                task_id,
                f"記事生成完了: {args.output}",
                "completed"
            )
        
        logger.info("処理が完了しました")
        
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}")
        
        # タスクエラーログ
        if args.log_task:
            log_task(
                task_id,
                f"エラーが発生しました: {e}",
                "error"
            )
        
        sys.exit(1)

if __name__ == "__main__":
    main()
