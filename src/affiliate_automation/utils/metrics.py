"""
メトリクスユーティリティモジュール

このモジュールは、記事の品質と生成パフォーマンスを測定するためのユーティリティを提供します。
"""

from typing import Dict, Any, List, Optional
import logging
import re
import time
from ..utils.logger import get_logger, log_metrics

# ロガーの設定
logger = get_logger(__name__)

class ArticleMetrics:
    """記事メトリクスクラス"""
    
    def __init__(self):
        """ArticleMetricsを初期化します"""
        self.start_time = time.time()
        self.metrics = {}
    
    def start_timer(self) -> None:
        """タイマーを開始します"""
        self.start_time = time.time()
    
    def stop_timer(self) -> float:
        """
        タイマーを停止し、経過時間を返します
        
        Returns:
            経過時間（秒）
        """
        elapsed_time = time.time() - self.start_time
        self.metrics["generation_time"] = elapsed_time
        return elapsed_time
    
    def analyze_content(self, content: str) -> Dict[str, Any]:
        """
        コンテンツを分析し、メトリクスを計算します
        
        Args:
            content: 分析するコンテンツ
            
        Returns:
            メトリクスの辞書
        """
        # 文字数
        char_count = len(content)
        self.metrics["character_count"] = char_count
        
        # 単語数
        word_count = len(content.split())
        self.metrics["word_count"] = word_count
        
        # 段落数
        paragraph_count = len(re.findall(r'\n\n', content)) + 1
        self.metrics["paragraph_count"] = paragraph_count
        
        # 見出し数
        h1_count = len(re.findall(r'^# ', content, re.MULTILINE))
        h2_count = len(re.findall(r'^## ', content, re.MULTILINE))
        h3_count = len(re.findall(r'^### ', content, re.MULTILINE))
        self.metrics["heading_count"] = {
            "h1": h1_count,
            "h2": h2_count,
            "h3": h3_count,
            "total": h1_count + h2_count + h3_count
        }
        
        # リンク数
        link_count = len(re.findall(r'\[.*?\]\(.*?\)', content))
        self.metrics["link_count"] = link_count
        
        # 画像数
        image_count = len(re.findall(r'!\[.*?\]\(.*?\)', content))
        self.metrics["image_count"] = image_count
        
        # リスト項目数
        list_item_count = len(re.findall(r'^- ', content, re.MULTILINE))
        self.metrics["list_item_count"] = list_item_count
        
        # 平均段落長（文字数）
        paragraphs = re.split(r'\n\n', content)
        avg_paragraph_length = sum(len(p) for p in paragraphs) / len(paragraphs) if paragraphs else 0
        self.metrics["avg_paragraph_length"] = avg_paragraph_length
        
        # 読みやすさスコア（簡易版）
        readability_score = self._calculate_readability(content)
        self.metrics["readability_score"] = readability_score
        
        logger.info(f"Content analyzed: {char_count} characters, {word_count} words")
        return self.metrics
    
    def _calculate_readability(self, content: str) -> float:
        """
        コンテンツの読みやすさスコアを計算します（簡易版）
        
        Args:
            content: 計算するコンテンツ
            
        Returns:
            読みやすさスコア（0-100）
        """
        # 実際の実装では、より複雑な読みやすさ指標を使用
        # ここでは簡易的な実装
        
        # 平均文長（文字数）
        sentences = re.split(r'[。.!?！？]', content)
        sentences = [s for s in sentences if s.strip()]
        avg_sentence_length = sum(len(s) for s in sentences) / len(sentences) if sentences else 0
        
        # 長い文の割合
        long_sentences = [s for s in sentences if len(s) > 100]
        long_sentence_ratio = len(long_sentences) / len(sentences) if sentences else 0
        
        # 段落あたりの文数
        paragraphs = re.split(r'\n\n', content)
        sentences_per_paragraph = len(sentences) / len(paragraphs) if paragraphs else 0
        
        # 読みやすさスコアの計算（簡易版）
        # 短い文、少ない長文、適切な段落分割で高スコア
        score = 100 - (avg_sentence_length * 0.2) - (long_sentence_ratio * 30) - (sentences_per_paragraph * 5)
        
        # スコアの範囲を0-100に制限
        score = max(0, min(100, score))
        
        return score
    
    def log_metrics(self, category: str) -> None:
        """
        メトリクスをログに記録します
        
        Args:
            category: メトリクスのカテゴリ
        """
        log_metrics(category, self.metrics)
        logger.info(f"Metrics logged for category: {category}")
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        メトリクスを取得します
        
        Returns:
            メトリクスの辞書
        """
        return self.metrics
