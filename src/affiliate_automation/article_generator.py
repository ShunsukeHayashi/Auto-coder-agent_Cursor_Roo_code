"""
記事生成モジュール

このモジュールは、アフィリエイト記事を生成するためのメインクラスを提供します。
"""

from typing import Dict, Any, List, Optional
import logging
from .content.content_generator import ContentGenerator
from .affiliate.link_manager import LinkManager
from .utils.logger import get_logger, log_metrics

# ロガーの設定
logger = get_logger(__name__)

class Article:
    """記事クラス"""
    
    def __init__(self, title: str, sections: List[Dict[str, Any]]):
        """
        Articleを初期化します
        
        Args:
            title: 記事のタイトル
            sections: 記事のセクション
        """
        self.title = title
        self.sections = sections
    
    def to_markdown(self) -> str:
        """
        記事をMarkdown形式に変換します
        
        Returns:
            Markdown形式の記事
        """
        markdown = f"# {self.title}\n\n"
        markdown += "![マッチングアプリ比較イメージ](※ここに画像を挿入)\n\n"
        
        for section in self.sections:
            markdown += f"## {section['title']}\n\n"
            markdown += f"{section['content']}\n\n"
            
            for subsection in section.get('subsections', []):
                markdown += f"### {subsection['title']}\n\n"
                markdown += f"{subsection['content']}\n\n"
        
        markdown += "【執筆者プロフィール】\n"
        markdown += "都内在住34歳女性。複数のマッチングアプリを使い、現在は素敵な彼氏と交際中。自身の経験を活かし、アラサー女性の恋愛・婚活事情について発信しています。\n\n"
        
        markdown += "【最終更新日】2025年2月15日"
        
        return markdown

class ArticleGenerator:
    """記事生成クラス"""
    
    def __init__(self, template_name: str = "matching_apps"):
        """
        ArticleGeneratorを初期化します
        
        Args:
            template_name: 使用するテンプレートの名前
        """
        self.template_name = template_name
        self.content_generator = ContentGenerator()
        self.link_manager = LinkManager()
        logger.info(f"ArticleGenerator initialized with template: {template_name}")
    
    def generate_article(self, params: Dict[str, Any]) -> Article:
        """
        記事を生成します
        
        Args:
            params: 記事生成のパラメータ
            
        Returns:
            生成された記事
        """
        logger.info(f"Generating article with params: {params}")
        
        # コンテンツの生成
        content = self.content_generator.generate_content(self.template_name, params)
        
        # アフィリエイトリンクの挿入
        self._insert_affiliate_links(content)
        
        # 記事オブジェクトの作成
        article = Article(content["title"], content["sections"])
        
        # メトリクスの記録
        self._log_metrics(article, params)
        
        logger.info(f"Article generated: {content['title']}")
        return article
    
    def _insert_affiliate_links(self, content: Dict[str, Any]) -> None:
        """
        コンテンツにアフィリエイトリンクを挿入します
        
        Args:
            content: アフィリエイトリンクを挿入するコンテンツ
        """
        # アプリ比較セクションの検索
        for section in content["sections"]:
            if "おすすめマッチングアプリ" in section["title"]:
                for subsection in section.get("subsections", []):
                    app_name = subsection["title"].split(" - ")[0].lower()
                    
                    # アフィリエイトリンクの置換
                    if "affiliate_link" in subsection["content"]:
                        link = self.link_manager.get_link(app_name)
                        subsection["content"] = subsection["content"].replace(
                            "※ここにアフィリエイトリンク", link
                        )
            
            # まとめセクションの検索
            elif "まとめ" in section["title"]:
                # まとめセクションにもアフィリエイトリンクを挿入
                if "無料ではじめる" in section["content"]:
                    link = self.link_manager.get_link("pairs")  # デフォルトはPairs
                    section["content"] = section["content"].replace(
                        "※ここにアフィリエイトリンク", link
                    )
    
    def _log_metrics(self, article: Article, params: Dict[str, Any]) -> None:
        """
        記事生成のメトリクスを記録します
        
        Args:
            article: 生成された記事
            params: 記事生成のパラメータ
        """
        metrics = {
            "template": self.template_name,
            "target_age": params.get("target_age", ""),
            "purpose": params.get("purpose", ""),
            "apps_count": params.get("apps_count", 0),
            "sections_count": len(article.sections),
            "word_count": len(article.to_markdown().split()),
            "character_count": len(article.to_markdown())
        }
        
        log_metrics("article_generation", metrics)
