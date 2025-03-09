"""
基本テンプレートモジュール

このモジュールは、すべての記事テンプレートの基底クラスを提供します。
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class BaseTemplate(ABC):
    """記事テンプレートの基底クラス"""
    
    def __init__(self, name: str, description: str):
        """
        BaseTemplateを初期化します
        
        Args:
            name: テンプレートの名前
            description: テンプレートの説明
        """
        self.name = name
        self.description = description
        self.sections = []
    
    @abstractmethod
    def generate_title(self, params: Dict[str, Any]) -> str:
        """
        タイトルを生成します
        
        Args:
            params: タイトル生成のパラメータ
            
        Returns:
            生成されたタイトル
        """
        pass
    
    @abstractmethod
    def generate_sections(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        記事のセクションを生成します
        
        Args:
            params: セクション生成のパラメータ
            
        Returns:
            生成されたセクションのリスト
        """
        pass
    
    def validate_params(self, params: Dict[str, Any]) -> bool:
        """
        パラメータを検証します
        
        Args:
            params: 検証するパラメータ
            
        Returns:
            パラメータが有効な場合はTrue、そうでない場合はFalse
        """
        return True
    
    def get_required_params(self) -> List[str]:
        """
        必須パラメータのリストを取得します
        
        Returns:
            必須パラメータのリスト
        """
        return []
