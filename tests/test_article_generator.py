"""
記事生成のテスト

このモジュールは、アフィリエイト記事生成システムのテストを提供します。
"""

import unittest
import os
import sys
from typing import Dict, Any

# テスト対象のモジュールをインポート
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.affiliate_automation.article_generator import ArticleGenerator, Article
from src.affiliate_automation.content.content_generator import ContentGenerator
from src.affiliate_automation.affiliate.link_manager import LinkManager

class TestArticleGenerator(unittest.TestCase):
    """ArticleGeneratorのテストクラス"""
    
    def setUp(self):
        """テストの前処理"""
        self.generator = ArticleGenerator("matching_apps")
        self.test_params = {
            "target_age": "30代",
            "purpose": "婚活",
            "apps_count": 3
        }
    
    def test_article_generation(self):
        """記事生成のテスト"""
        # 記事の生成
        article = self.generator.generate_article(self.test_params)
        
        # 記事オブジェクトの検証
        self.assertIsInstance(article, Article)
        self.assertIsNotNone(article.title)
        self.assertGreater(len(article.title), 0)
        self.assertIsInstance(article.sections, list)
        self.assertGreater(len(article.sections), 0)
        
        # Markdown変換の検証
        markdown = article.to_markdown()
        self.assertIsInstance(markdown, str)
        self.assertGreater(len(markdown), 0)
        self.assertIn(self.test_params["target_age"], markdown)
        self.assertIn(self.test_params["purpose"], markdown)
    
    def test_title_generation(self):
        """タイトル生成のテスト"""
        # 記事の生成
        article = self.generator.generate_article(self.test_params)
        
        # タイトルの検証
        self.assertIn(self.test_params["target_age"], article.title)
        self.assertIn(self.test_params["purpose"], article.title)
        self.assertIn("マッチングアプリ", article.title)
        self.assertIn(str(self.test_params["apps_count"]), article.title)
    
    def test_affiliate_links(self):
        """アフィリエイトリンクのテスト"""
        # 記事の生成
        article = self.generator.generate_article(self.test_params)
        markdown = article.to_markdown()
        
        # アフィリエイトリンクの検証
        self.assertIn("[無料ではじめる](", markdown)
        self.assertNotIn("※ここにアフィリエイトリンク", markdown)
    
    def test_different_params(self):
        """異なるパラメータでのテスト"""
        # 異なるパラメータ
        different_params = {
            "target_age": "20代",
            "purpose": "恋活",
            "apps_count": 2
        }
        
        # 記事の生成
        article = self.generator.generate_article(different_params)
        markdown = article.to_markdown()
        
        # パラメータの反映を検証
        self.assertIn(different_params["target_age"], markdown)
        self.assertIn(different_params["purpose"], markdown)
        
        # セクション数の検証（apps_countが少ないので、アプリ紹介セクションが少なくなるはず）
        app_sections = 0
        for section in article.sections:
            if "おすすめマッチングアプリ" in section["title"]:
                app_sections = len(section.get("subsections", []))
                break
        
        self.assertEqual(app_sections, different_params["apps_count"])

if __name__ == "__main__":
    unittest.main()
