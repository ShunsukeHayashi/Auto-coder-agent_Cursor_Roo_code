"""
フォーマッタユーティリティモジュール

このモジュールは、記事の出力フォーマットを処理するためのユーティリティを提供します。
"""

from typing import Dict, Any, List, Optional
import logging
import re
from ..utils.logger import get_logger

# ロガーの設定
logger = get_logger(__name__)

class Formatter:
    """フォーマッタクラス"""
    
    @staticmethod
    def format_markdown(content: str) -> str:
        """
        Markdown形式のコンテンツをフォーマットします
        
        Args:
            content: フォーマットするコンテンツ
            
        Returns:
            フォーマットされたコンテンツ
        """
        # 連続する空行を1つにまとめる
        formatted = re.sub(r'\n{3,}', '\n\n', content)
        
        # リストアイテムの前後に適切な空行を追加
        formatted = re.sub(r'([^\n])\n- ', r'\1\n\n- ', formatted)
        formatted = re.sub(r'- ([^\n]*)\n([^-\n])', r'- \1\n\n\2', formatted)
        
        # 見出しの前に空行を追加
        formatted = re.sub(r'([^\n])\n(#+) ', r'\1\n\n\2 ', formatted)
        
        logger.info("Markdown content formatted")
        return formatted
    
    @staticmethod
    def format_html(markdown: str) -> str:
        """
        Markdown形式のコンテンツをHTML形式に変換します
        
        Args:
            markdown: 変換するMarkdownコンテンツ
            
        Returns:
            HTML形式のコンテンツ
        """
        # 実際の実装では、markdownライブラリなどを使用して変換
        # ここでは簡易的な実装
        
        # 見出しの変換
        html = re.sub(r'# (.*?)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
        html = re.sub(r'## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        
        # 段落の変換
        html = re.sub(r'(?<!\n)\n(?!\n)(?!<h|<p|<ul|<li|<ol)', ' ', html)
        html = re.sub(r'\n\n([^<].*?)(?:\n\n|$)', r'<p>\1</p>\n', html, flags=re.DOTALL)
        
        # リストの変換
        html = re.sub(r'- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
        html = re.sub(r'(<li>.*?</li>\n)+', r'<ul>\n\g<0></ul>\n', html, flags=re.DOTALL)
        
        # 強調の変換
        html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
        
        # リンクの変換
        html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
        
        # 画像の変換
        html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', html)
        
        logger.info("Markdown content converted to HTML")
        return html
    
    @staticmethod
    def format_plain_text(markdown: str) -> str:
        """
        Markdown形式のコンテンツをプレーンテキスト形式に変換します
        
        Args:
            markdown: 変換するMarkdownコンテンツ
            
        Returns:
            プレーンテキスト形式のコンテンツ
        """
        # 見出しの変換
        text = re.sub(r'# (.*?)$', r'\1\n' + '=' * 50, markdown, flags=re.MULTILINE)
        text = re.sub(r'## (.*?)$', r'\1\n' + '-' * 40, text, flags=re.MULTILINE)
        text = re.sub(r'### (.*?)$', r'\1\n' + '-' * 30, text, flags=re.MULTILINE)
        
        # 強調の削除
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = re.sub(r'\*(.*?)\*', r'\1', text)
        
        # リンクの変換
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1 (\2)', text)
        
        # 画像の変換
        text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'[画像: \1]', text)
        
        logger.info("Markdown content converted to plain text")
        return text
