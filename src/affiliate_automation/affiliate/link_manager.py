"""
リンク管理モジュール

このモジュールは、アフィリエイトリンクの管理と生成のためのクラスを提供します。
"""

from typing import Dict, Any, List, Optional
import logging
from ..utils.logger import get_logger

# ロガーの設定
logger = get_logger(__name__)

class LinkManager:
    """アフィリエイトリンク管理クラス"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        LinkManagerを初期化します
        
        Args:
            config: リンク管理の設定
        """
        self.config = config or {}
        self.links = self._load_links()
        logger.info("LinkManager initialized")
    
    def _load_links(self) -> Dict[str, Dict[str, Any]]:
        """
        アフィリエイトリンク情報を読み込みます
        
        Returns:
            リンク情報の辞書
        """
        # 実際の実装では、データベースやファイルから読み込むことも可能
        return {
            "pairs": {
                "name": "Pairs",
                "base_url": "https://pairs.lv/",
                "affiliate_id": "af12345",
                "tracking_params": "utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps",
                "full_url": "https://pairs.lv/?utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps&af_id=af12345"
            },
            "with": {
                "name": "with",
                "base_url": "https://with.jp/",
                "affiliate_id": "af67890",
                "tracking_params": "utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps",
                "full_url": "https://with.jp/?utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps&af_id=af67890"
            },
            "zexy_enmusubi": {
                "name": "ゼクシィ縁結び",
                "base_url": "https://zexy-enmusubi.net/",
                "affiliate_id": "af24680",
                "tracking_params": "utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps",
                "full_url": "https://zexy-enmusubi.net/?utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps&af_id=af24680"
            },
            "omiai": {
                "name": "Omiai",
                "base_url": "https://fb.omiai-jp.com/",
                "affiliate_id": "af13579",
                "tracking_params": "utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps",
                "full_url": "https://fb.omiai-jp.com/?utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps&af_id=af13579"
            },
            "marrish": {
                "name": "マリッシュ",
                "base_url": "https://marrish.com/",
                "affiliate_id": "af97531",
                "tracking_params": "utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps",
                "full_url": "https://marrish.com/?utm_source=affiliate&utm_medium=article&utm_campaign=matching_apps&af_id=af97531"
            }
        }
    
    def get_link(self, app_id: str) -> str:
        """
        アプリIDに基づいてアフィリエイトリンクを取得します
        
        Args:
            app_id: アプリのID
        
        Returns:
            アフィリエイトリンク
        
        Raises:
            ValueError: アプリIDが見つからない場合
        """
        if app_id not in self.links:
            logger.warning(f"Unknown app ID: {app_id}")
            return f"[公式サイトを見る](※{app_id}のアフィリエイトリンク)"
        
        link_info = self.links[app_id]
        markdown_link = f"[無料ではじめる]({link_info['full_url']})"
        
        logger.info(f"Generated affiliate link for {app_id}")
        return markdown_link
    
    def get_all_links(self) -> Dict[str, str]:
        """
        すべてのアフィリエイトリンクを取得します
        
        Returns:
            アプリIDとリンクのマッピング
        """
        result = {}
        for app_id, link_info in self.links.items():
            result[app_id] = f"[無料ではじめる]({link_info['full_url']})"
        
        return result
    
    def update_tracking_params(self, params: Dict[str, str]) -> None:
        """
        トラッキングパラメータを更新します
        
        Args:
            params: 更新するパラメータ
        """
        for app_id, link_info in self.links.items():
            tracking_params = "&".join([f"{k}={v}" for k, v in params.items()])
            link_info["tracking_params"] = tracking_params
            
            # フルURLの更新
            base_url = link_info["base_url"]
            affiliate_id = link_info["affiliate_id"]
            link_info["full_url"] = f"{base_url}?{tracking_params}&af_id={affiliate_id}"
        
        logger.info("Updated tracking parameters for all links")
