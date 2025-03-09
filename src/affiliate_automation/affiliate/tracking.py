"""
トラッキングモジュール

このモジュールは、アフィリエイトリンクのトラッキング機能を提供します。
"""

from typing import Dict, Any, List, Optional
import logging
import json
import os
from datetime import datetime
from ..utils.logger import get_logger, log_metrics

# ロガーの設定
logger = get_logger(__name__)

class LinkTracker:
    """リンクトラッキングクラス"""
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        LinkTrackerを初期化します
        
        Args:
            storage_path: トラッキングデータの保存パス
        """
        self.storage_path = storage_path or os.path.join(
            os.getcwd(), "logs", "metrics", "link_tracking.json"
        )
        self.tracking_data = self._load_tracking_data()
        logger.info("LinkTracker initialized")
    
    def _load_tracking_data(self) -> Dict[str, Any]:
        """
        トラッキングデータを読み込みます
        
        Returns:
            トラッキングデータの辞書
        """
        if not os.path.exists(self.storage_path):
            # ディレクトリが存在しない場合は作成
            os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
            
            # 初期データの作成
            initial_data = {
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "apps": {},
                "total_impressions": 0,
                "total_clicks": 0
            }
            
            # ファイルに保存
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(initial_data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Created new tracking data file: {self.storage_path}")
            return initial_data
        
        try:
            # 既存のデータを読み込み
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            logger.info(f"Loaded tracking data from: {self.storage_path}")
            return data
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger.error(f"Error loading tracking data: {e}")
            
            # エラーが発生した場合は新しいデータを作成
            initial_data = {
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "apps": {},
                "total_impressions": 0,
                "total_clicks": 0
            }
            
            return initial_data
    
    def _save_tracking_data(self) -> None:
        """トラッキングデータを保存します"""
        # 更新日時の更新
        self.tracking_data["updated_at"] = datetime.now().isoformat()
        
        # ディレクトリが存在しない場合は作成
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        
        # ファイルに保存
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(self.tracking_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Saved tracking data to: {self.storage_path}")
    
    def record_impression(self, app_id: str, article_id: Optional[str] = None) -> None:
        """
        アプリのインプレッションを記録します
        
        Args:
            app_id: アプリのID
            article_id: 記事のID（オプション）
        """
        # アプリデータの取得または作成
        if app_id not in self.tracking_data["apps"]:
            self.tracking_data["apps"][app_id] = {
                "impressions": 0,
                "clicks": 0,
                "articles": {}
            }
        
        # インプレッションのカウント
        self.tracking_data["apps"][app_id]["impressions"] += 1
        self.tracking_data["total_impressions"] += 1
        
        # 記事IDが指定されている場合は記事ごとのインプレッションも記録
        if article_id:
            if article_id not in self.tracking_data["apps"][app_id]["articles"]:
                self.tracking_data["apps"][app_id]["articles"][article_id] = {
                    "impressions": 0,
                    "clicks": 0
                }
            
            self.tracking_data["apps"][app_id]["articles"][article_id]["impressions"] += 1
        
        # データの保存
        self._save_tracking_data()
        
        logger.info(f"Recorded impression for app: {app_id}")
    
    def record_click(self, app_id: str, article_id: Optional[str] = None) -> None:
        """
        アプリのクリックを記録します
        
        Args:
            app_id: アプリのID
            article_id: 記事のID（オプション）
        """
        # アプリデータの取得または作成
        if app_id not in self.tracking_data["apps"]:
            self.tracking_data["apps"][app_id] = {
                "impressions": 0,
                "clicks": 0,
                "articles": {}
            }
        
        # クリックのカウント
        self.tracking_data["apps"][app_id]["clicks"] += 1
        self.tracking_data["total_clicks"] += 1
        
        # 記事IDが指定されている場合は記事ごとのクリックも記録
        if article_id:
            if article_id not in self.tracking_data["apps"][app_id]["articles"]:
                self.tracking_data["apps"][app_id]["articles"][article_id] = {
                    "impressions": 0,
                    "clicks": 0
                }
            
            self.tracking_data["apps"][app_id]["articles"][article_id]["clicks"] += 1
        
        # データの保存
        self._save_tracking_data()
        
        logger.info(f"Recorded click for app: {app_id}")
    
    def get_app_stats(self, app_id: str) -> Dict[str, Any]:
        """
        アプリの統計情報を取得します
        
        Args:
            app_id: アプリのID
            
        Returns:
            アプリの統計情報
        """
        if app_id not in self.tracking_data["apps"]:
            return {
                "impressions": 0,
                "clicks": 0,
                "ctr": 0.0,
                "articles": {}
            }
        
        app_data = self.tracking_data["apps"][app_id]
        
        # CTR（クリック率）の計算
        ctr = app_data["clicks"] / app_data["impressions"] if app_data["impressions"] > 0 else 0
        
        # 記事ごとのCTRの計算
        articles_with_ctr = {}
        for article_id, article_data in app_data["articles"].items():
            article_ctr = article_data["clicks"] / article_data["impressions"] if article_data["impressions"] > 0 else 0
            articles_with_ctr[article_id] = {
                "impressions": article_data["impressions"],
                "clicks": article_data["clicks"],
                "ctr": article_ctr
            }
        
        return {
            "impressions": app_data["impressions"],
            "clicks": app_data["clicks"],
            "ctr": ctr,
            "articles": articles_with_ctr
        }
    
    def get_all_stats(self) -> Dict[str, Any]:
        """
        すべてのアプリの統計情報を取得します
        
        Returns:
            すべてのアプリの統計情報
        """
        stats = {
            "total_impressions": self.tracking_data["total_impressions"],
            "total_clicks": self.tracking_data["total_clicks"],
            "overall_ctr": (
                self.tracking_data["total_clicks"] / self.tracking_data["total_impressions"]
                if self.tracking_data["total_impressions"] > 0 else 0
            ),
            "apps": {}
        }
        
        # アプリごとの統計情報を取得
        for app_id in self.tracking_data["apps"]:
            stats["apps"][app_id] = self.get_app_stats(app_id)
        
        return stats
    
    def log_stats(self) -> None:
        """統計情報をログに記録します"""
        stats = self.get_all_stats()
        log_metrics("link_tracking", stats)
        logger.info("Link tracking stats logged")
