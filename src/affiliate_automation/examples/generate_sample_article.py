"""
サンプル記事生成スクリプト

このスクリプトは、アフィリエイト記事自動生成システムのサンプル使用例を提供します。
"""

import os
import sys
import json

# 親ディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.affiliate_automation.article_generator import ArticleGenerator
from src.affiliate_automation.utils.metrics import ArticleMetrics

def main():
    """メイン関数"""
    print("マッチングアプリのアフィリエイト記事生成サンプル")
    
    # パラメータの設定
    params = {
        "target_age": "30代",
        "purpose": "婚活",
        "apps_count": 5,
        "include_pricing": True,
        "include_user_reviews": True
    }
    
    # メトリクスの初期化
    metrics = ArticleMetrics()
    metrics.start_timer()
    
    # 記事生成
    generator = ArticleGenerator("matching_apps")
    article = generator.generate_article(params)
    
    # 生成時間の計測
    generation_time = metrics.stop_timer()
    print(f"記事生成時間: {generation_time:.2f}秒")
    
    # コンテンツの分析
    markdown = article.to_markdown()
    content_metrics = metrics.analyze_content(markdown)
    
    # メトリクスの表示
    print("\n記事メトリクス:")
    print(f"- 文字数: {content_metrics['character_count']}")
    print(f"- 単語数: {content_metrics['word_count']}")
    print(f"- 段落数: {content_metrics['paragraph_count']}")
    print(f"- 見出し数: {content_metrics['heading_count']['total']}")
    print(f"- リンク数: {content_metrics['link_count']}")
    print(f"- 読みやすさスコア: {content_metrics['readability_score']:.1f}/100")
    
    # 記事の保存
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "matching_apps_article.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)
    
    print(f"\n記事を保存しました: {output_file}")
    
    # メトリクスの保存
    metrics_file = os.path.join(output_dir, "metrics.json")
    with open(metrics_file, "w", encoding="utf-8") as f:
        json.dump(content_metrics, f, ensure_ascii=False, indent=2)
    
    print(f"メトリクスを保存しました: {metrics_file}")

if __name__ == "__main__":
    main()
