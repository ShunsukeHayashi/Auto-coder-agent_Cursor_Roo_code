"""
Content Generator Module

This module handles AI-powered content generation for affiliate marketing.
"""

import os
import logging
import json
import time
from typing import Dict, List, Any, Optional
import requests
from datetime import datetime

# Import configuration
import sys
sys.path.append('/home/ubuntu/affiliate_automation')
from config.config import AI_TOOLS, AFFILIATE_NICHES, OPENAI_API_KEY

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/home/ubuntu/affiliate_automation/logs/content_generator.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ContentGenerator")

class ContentGenerator:
    """
    AI-powered content generator for affiliate marketing.
    
    This class handles the generation of various types of content for
    affiliate marketing websites, including product reviews, buying guides,
    how-to articles, and more.
    """
    
    def __init__(self, niche: str = "online_learning"):
        """
        Initialize the Content Generator.
        
        Args:
            niche: The affiliate marketing niche to focus on
        """
        self.niche = niche
        self.niche_data = AFFILIATE_NICHES.get(niche, {})
        if not self.niche_data:
            logger.error(f"Niche '{niche}' not found in configuration")
            raise ValueError(f"Niche '{niche}' not found in configuration")
            
        self.content_config = AI_TOOLS["content_generation"]
        self.openai_api_key = os.environ.get("OPENAI_API_KEY", OPENAI_API_KEY)
        
        logger.info(f"Content Generator initialized for niche: {niche}")
    
    def generate_article(self, article_type: str, topic: str, keywords: List[str]) -> Dict[str, Any]:
        """
        Generate a complete article using AI.
        
        Args:
            article_type: Type of article to generate (product_review, buying_guide, how_to)
            topic: The main topic of the article
            keywords: List of keywords to include in the article
            
        Returns:
            Dictionary containing the generated article content
        """
        logger.info(f"Generating {article_type} article on topic: {topic}")
        
        # Get article structure from configuration
        article_structure = self.content_config["article_types"].get(article_type, {}).get("structure", [])
        if not article_structure:
            logger.error(f"Article type '{article_type}' not found in configuration")
            raise ValueError(f"Article type '{article_type}' not found in configuration")
        
        # Generate article sections
        sections = {}
        for section in article_structure:
            sections[section] = self._generate_section(article_type, section, topic, keywords)
        
        # Compile complete article
        article = {
            "title": f"The Ultimate {topic.title()} {article_type.replace('_', ' ').title()}",
            "type": article_type,
            "topic": topic,
            "keywords": keywords,
            "sections": sections,
            "word_count": sum(len(section.split()) for section in sections.values()),
            "generated_at": datetime.now().isoformat()
        }
        
        logger.info(f"Generated {article_type} article: {article['title']} ({article['word_count']} words)")
        return article
    
    def _generate_section(self, article_type: str, section: str, topic: str, keywords: List[str]) -> str:
        """
        Generate a section of an article using AI.
        
        Args:
            article_type: Type of article
            section: Section name
            topic: Article topic
            keywords: Keywords to include
            
        Returns:
            Generated section content
        """
        logger.info(f"Generating {section} section for {article_type} on {topic}")
        
        # Prepare prompt for the AI model
        prompt = self._create_section_prompt(article_type, section, topic, keywords)
        
        # Call OpenAI API to generate content
        try:
            content = self._call_openai_api(prompt)
            return content
        except Exception as e:
            logger.error(f"Error generating section {section}: {str(e)}")
            return f"[Error generating {section} section]"
    
    def _create_section_prompt(self, article_type: str, section: str, topic: str, keywords: List[str]) -> str:
        """
        Create a prompt for generating a specific section of an article.
        
        Args:
            article_type: Type of article
            section: Section name
            topic: Article topic
            keywords: Keywords to include
            
        Returns:
            Prompt for the AI model
        """
        # Base prompts for different article types
        prompts = {
            "product_review": {
                "introduction": f"Write an engaging introduction for a product review about {topic}. Include why this product is important and who would benefit from it. Naturally incorporate these keywords: {', '.join(keywords[:2])}.",
                "product_overview": f"Write a comprehensive overview of {topic}, including its main features, specifications, and what sets it apart from competitors. Naturally incorporate these keywords: {', '.join(keywords[1:3])}.",
                "features": f"Write a detailed section about the key features of {topic}. Explain how each feature works and its benefits. Naturally incorporate these keywords: {', '.join(keywords[2:4])}.",
                "benefits": f"Write a section explaining the main benefits of using {topic}. Include real-world examples of how these benefits impact users. Naturally incorporate these keywords: {', '.join(keywords[1:3])}.",
                "drawbacks": f"Write an honest section about any limitations or drawbacks of {topic}. Be fair and balanced in your assessment. Naturally incorporate these keywords: {', '.join(keywords[3:5])}.",
                "comparison": f"Write a section comparing {topic} with its main competitors. Highlight where it excels and where it falls short. Naturally incorporate these keywords: {', '.join(keywords[2:4])}.",
                "conclusion": f"Write a compelling conclusion for the {topic} review, including a final recommendation and who should purchase it. Naturally incorporate these keywords: {', '.join(keywords[:2])}."
            },
            "buying_guide": {
                "introduction": f"Write an engaging introduction for a buying guide about {topic}. Explain why this guide is valuable and who it's for. Naturally incorporate these keywords: {', '.join(keywords[:2])}.",
                "market_overview": f"Write a comprehensive overview of the {topic} market, including current trends and what buyers should know. Naturally incorporate these keywords: {', '.join(keywords[1:3])}.",
                "key_considerations": f"Write a detailed section about the key factors to consider when buying {topic}. Explain why each factor matters. Naturally incorporate these keywords: {', '.join(keywords[2:4])}.",
                "top_products": f"Write a section highlighting the top {topic} products currently available, with brief descriptions of each. Naturally incorporate these keywords: {', '.join(keywords[1:3])}.",
                "recommendations": f"Write specific recommendations for different types of buyers looking for {topic}. Include budget options, premium choices, and best overall. Naturally incorporate these keywords: {', '.join(keywords[3:5])}.",
                "conclusion": f"Write a helpful conclusion for the {topic} buying guide, summarizing the key points and offering final advice. Naturally incorporate these keywords: {', '.join(keywords[:2])}."
            },
            "how_to": {
                "introduction": f"Write an engaging introduction for a how-to guide about {topic}. Explain the value of learning this skill and who will benefit. Naturally incorporate these keywords: {', '.join(keywords[:2])}.",
                "materials_needed": f"Write a comprehensive list of materials or tools needed for {topic}, with brief explanations of why each is necessary. Naturally incorporate these keywords: {', '.join(keywords[1:3])}.",
                "step_by_step": f"Write detailed step-by-step instructions for {topic}. Make each step clear and actionable. Naturally incorporate these keywords: {', '.join(keywords[2:4])}.",
                "tips": f"Write a section with expert tips and tricks for mastering {topic}. Include common mistakes to avoid. Naturally incorporate these keywords: {', '.join(keywords[1:3])}.",
                "conclusion": f"Write an encouraging conclusion for the {topic} guide, including next steps and how to build on this skill. Naturally incorporate these keywords: {', '.join(keywords[:2])}."
            }
        }
        
        # Get the appropriate prompt for this article type and section
        base_prompt = prompts.get(article_type, {}).get(section, f"Write content about {topic} for the {section} section.")
        
        # Add affiliate marketing context
        affiliate_context = f"\n\nThis is for an affiliate marketing website in the {self.niche.replace('_', ' ')} niche. "
        affiliate_context += f"Where appropriate, mention affiliate products naturally and ethically. "
        affiliate_context += f"The content should be helpful, informative, and trustworthy to build reader confidence."
        
        # Add SEO instructions
        seo_instructions = f"\n\nOptimize the content for SEO while maintaining readability and value for the reader. "
        seo_instructions += f"Use keywords naturally without keyword stuffing."
        
        # Combine all parts
        full_prompt = base_prompt + affiliate_context + seo_instructions
        
        return full_prompt
    
    def _call_openai_api(self, prompt: str) -> str:
        """
        Call the OpenAI API to generate content.
        
        Args:
            prompt: The prompt to send to the API
            
        Returns:
            Generated content from the API
        """
        logger.info("Calling OpenAI API for content generation")
        
        # In a real implementation, this would make an actual API call
        # For this example, we'll simulate the API response
        
        # Simulate API call delay
        time.sleep(1)
        
        # Simulate API response
        return f"This is simulated content generated based on the prompt: '{prompt[:50]}...'. In a real implementation, this would be actual content from the OpenAI API."
    
    def generate_product_review(self, product_name: str, affiliate_program: str) -> Dict[str, Any]:
        """
        Generate a product review article for affiliate marketing.
        
        Args:
            product_name: Name of the product to review
            affiliate_program: Name of the affiliate program
            
        Returns:
            Dictionary containing the generated product review
        """
        # Get keywords for this niche
        keywords = self.niche_data.get("keywords", [])
        
        # Generate the product review
        return self.generate_article(
            article_type="product_review",
            topic=product_name,
            keywords=keywords
        )
    
    def generate_buying_guide(self, topic: str) -> Dict[str, Any]:
        """
        Generate a buying guide article for affiliate marketing.
        
        Args:
            topic: Topic of the buying guide
            
        Returns:
            Dictionary containing the generated buying guide
        """
        # Get keywords for this niche
        keywords = self.niche_data.get("keywords", [])
        
        # Generate the buying guide
        return self.generate_article(
            article_type="buying_guide",
            topic=topic,
            keywords=keywords
        )
    
    def generate_how_to(self, topic: str) -> Dict[str, Any]:
        """
        Generate a how-to article for affiliate marketing.
        
        Args:
            topic: Topic of the how-to guide
            
        Returns:
            Dictionary containing the generated how-to guide
        """
        # Get keywords for this niche
        keywords = self.niche_data.get("keywords", [])
        
        # Generate the how-to guide
        return self.generate_article(
            article_type="how_to",
            topic=topic,
            keywords=keywords
        )
    
    def save_article(self, article: Dict[str, Any], filepath: str = None) -> str:
        """
        Save a generated article to a file.
        
        Args:
            article: The article to save
            filepath: Path to save the article (optional)
            
        Returns:
            Path where the article was saved
        """
        if filepath is None:
            # Generate a filename based on the article title
            title_slug = article["title"].lower().replace(" ", "-").replace(":", "").replace("?", "").replace("!", "")
            filepath = f"/home/ubuntu/affiliate_automation/data/articles/{title_slug}.json"
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Save article to file
        with open(filepath, 'w') as f:
            json.dump(article, f, indent=2)
            
        logger.info(f"Article saved to {filepath}")
        return filepath
    
    def load_article(self, filepath: str) -> Dict[str, Any]:
        """
        Load an article from a file.
        
        Args:
            filepath: Path to the article file
            
        Returns:
            The loaded article
        """
        try:
            with open(filepath, 'r') as f:
                article = json.load(f)
                
            logger.info(f"Article loaded from {filepath}")
            return article
        except FileNotFoundError:
            logger.error(f"Article file not found: {filepath}")
            raise FileNotFoundError(f"Article file not found: {filepath}")
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in article file: {filepath}")
            raise ValueError(f"Invalid JSON in article file: {filepath}")
