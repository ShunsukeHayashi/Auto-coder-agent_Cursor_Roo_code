#!/usr/bin/env python3
"""
Affiliate Marketing Automation System

This script implements a complete AI agent automation workflow for affiliate marketing.
It orchestrates the entire process from niche selection to performance optimization.
"""

import os
import sys
import logging
import json
import time
import argparse
from datetime import datetime
from typing import Dict, List, Any, Optional

# Import configuration and modules
sys.path.append('/home/ubuntu/affiliate_automation')
from config.config import AFFILIATE_NICHES, AI_TOOLS, WORKFLOW_CONFIG
from agent.affiliate_agent import AffiliateMarketingAgent
from agent.content_generator import ContentGenerator
from agent.website_generator import WebsiteGenerator
from agent.marketing_automation import MarketingAutomation

# Set up logging
os.makedirs("/home/ubuntu/affiliate_automation/logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/home/ubuntu/affiliate_automation/logs/main.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("AffiliateAutomation")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Affiliate Marketing Automation System")
    parser.add_argument("--niche", type=str, default="online_learning",
                        help="Affiliate marketing niche to focus on")
    parser.add_argument("--mode", type=str, choices=["full", "research", "content", "website", "marketing"],
                        default="full", help="Operation mode")
    parser.add_argument("--domain", type=str, default=None,
                        help="Domain name for the affiliate website")
    parser.add_argument("--state-file", type=str, default=None,
                        help="Path to agent state file")
    return parser.parse_args()

def validate_niche(niche: str) -> bool:
    """Validate that the specified niche exists in configuration."""
    return niche in AFFILIATE_NICHES

def get_domain_name(niche: str) -> str:
    """Generate a domain name for the affiliate website."""
    return f"{niche.replace('_', '-')}-affiliate-guide.com"

def print_banner():
    """Print a banner for the application."""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   AI-Powered Affiliate Marketing Automation System            ║
    ║   ---------------------------------------------------        ║
    ║                                                               ║
    ║   Automate your affiliate marketing business using AI         ║
    ║   Focus on the most profitable niches and strategies          ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_workflow_visualization():
    """Print a visualization of the affiliate marketing automation workflow."""
    workflow = """
    ◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
    ◤                                                            ◢
    ◢       AI-Powered Affiliate Marketing Automation Flow       ◤
    ◤                                                            ◢
    ◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
    
    ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
    │                 │     │                 │     │                 │
    │  Niche Research │────▶│ Website Creation│────▶│Content Generation│
    │                 │     │                 │     │                 │
    └─────────────────┘     └─────────────────┘     └─────────────────┘
             │                                               │
             │                                               │
             │                                               ▼
    ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
    │                 │     │                 │     │                 │
    │   Optimization  │◀────│  Performance    │◀────│   Marketing     │
    │                 │     │   Tracking      │     │  Automation     │
    └─────────────────┘     └─────────────────┘     └─────────────────┘
             │                                               
             │                                               
             ▼                                               
    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │                  Continuous Improvement Loop                    │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘
    """
    print(workflow)

def run_full_workflow(niche: str, domain: str = None, state_file: str = None):
    """
    Run the complete affiliate marketing automation workflow.
    
    Args:
        niche: Affiliate marketing niche to focus on
        domain: Domain name for the affiliate website (optional)
        state_file: Path to agent state file (optional)
    """
    logger.info(f"Starting full affiliate marketing automation workflow for niche: {niche}")
    
    # Initialize the main agent
    agent = AffiliateMarketingAgent(niche=niche)
    
    # Load state if provided
    if state_file and os.path.exists(state_file):
        agent.load_state(state_file)
        logger.info(f"Loaded agent state from: {state_file}")
    
    # Run the complete workflow
    success = agent.run_workflow()
    
    if success:
        logger.info("Affiliate marketing automation workflow completed successfully")
        
        # Save the final state
        if state_file:
            agent.save_state(state_file)
        else:
            agent.save_state()
    else:
        logger.error("Affiliate marketing automation workflow failed")

def run_research_mode(niche: str):
    """
    Run only the niche research part of the workflow.
    
    Args:
        niche: Affiliate marketing niche to focus on
    """
    logger.info(f"Running niche research for: {niche}")
    
    # Initialize the main agent
    agent = AffiliateMarketingAgent(niche=niche)
    
    # Run only the research step
    agent.research_niche()
    
    # Save the research results
    research_file = f"/home/ubuntu/affiliate_automation/data/research_{niche}.json"
    with open(research_file, 'w') as f:
        json.dump(agent.state["research"], f, indent=2)
    
    logger.info(f"Niche research completed and saved to: {research_file}")
    
    # Print research summary
    print("\nResearch Summary:")
    print(f"Niche: {niche}")
    print(f"Market Size: {agent.state['research']['market_size']}")
    print(f"Growth Rate: {agent.state['research']['growth_rate']}")
    print("Top Programs:")
    for program, details in agent.state["research"]["top_programs"].items():
        print(f"  - {program}: {details}")
    print("Target Keywords:")
    for keyword in agent.state["research"]["keywords"]:
        print(f"  - {keyword}")

def run_content_mode(niche: str):
    """
    Run only the content generation part of the workflow.
    
    Args:
        niche: Affiliate marketing niche to focus on
    """
    logger.info(f"Running content generation for niche: {niche}")
    
    # Initialize the content generator
    content_generator = ContentGenerator(niche=niche)
    
    # Generate different types of content
    articles = []
    
    # Product review
    product_name = f"Best {niche.replace('_', ' ').title()} Products"
    review = content_generator.generate_product_review(product_name, "top_program")
    articles.append(review)
    
    # Buying guide
    guide_topic = f"{niche.replace('_', ' ').title()} Buying Guide"
    guide = content_generator.generate_buying_guide(guide_topic)
    articles.append(guide)
    
    # How-to guide
    how_to_topic = f"How to Choose the Best {niche.replace('_', ' ').title()} Products"
    how_to = content_generator.generate_how_to(how_to_topic)
    articles.append(how_to)
    
    # Save the generated content
    os.makedirs(f"/home/ubuntu/affiliate_automation/data/articles", exist_ok=True)
    for article in articles:
        filepath = content_generator.save_article(article)
        logger.info(f"Saved article: {article['title']} to {filepath}")
    
    logger.info(f"Content generation completed: {len(articles)} articles generated")
    
    # Print content summary
    print("\nContent Generation Summary:")
    print(f"Niche: {niche}")
    print(f"Articles Generated: {len(articles)}")
    for article in articles:
        print(f"  - {article['title']} ({article['word_count']} words)")

def run_website_mode(niche: str, domain: str = None):
    """
    Run only the website creation part of the workflow.
    
    Args:
        niche: Affiliate marketing niche to focus on
        domain: Domain name for the affiliate website (optional)
    """
    logger.info(f"Running website creation for niche: {niche}")
    
    # Initialize the website generator
    website_generator = WebsiteGenerator(niche=niche)
    
    # Generate domain name if not provided
    if domain is None:
        domain = get_domain_name(niche)
    
    # Create the website
    website = website_generator.create_website(domain_name=domain)
    
    # Deploy the website
    deployment = website_generator.deploy_website(website)
    
    # Save the website configuration
    filepath = website_generator.save_website(website)
    
    logger.info(f"Website creation completed: {deployment['url']}")
    
    # Print website summary
    print("\nWebsite Creation Summary:")
    print(f"Niche: {niche}")
    print(f"Domain: {domain}")
    print(f"Template: {website['template']}")
    print(f"URL: {deployment['url']}")
    print(f"Pages: {len(website['pages'])}")
    for page in website['pages']:
        print(f"  - {page['title']}")

def run_marketing_mode(niche: str):
    """
    Run only the marketing automation part of the workflow.
    
    Args:
        niche: Affiliate marketing niche to focus on
    """
    logger.info(f"Running marketing automation for niche: {niche}")
    
    # Initialize the marketing automation
    marketing = MarketingAutomation(niche=niche)
    
    # Create sample content for marketing
    sample_content = {
        "id": "article_1",
        "title": f"The Ultimate {niche.replace('_', ' ').title()} Guide",
        "topic": niche.replace('_', ' '),
        "url": f"https://{get_domain_name(niche)}/guide"
    }
    
    # Create marketing campaigns
    campaigns = []
    
    # Social media campaign
    social_campaign = marketing.create_social_media_campaign(sample_content)
    campaigns.append(social_campaign)
    
    # Email campaigns
    newsletter = marketing.create_email_campaign(sample_content, "newsletter")
    campaigns.append(newsletter)
    
    promotional = marketing.create_email_campaign(sample_content, "promotional")
    campaigns.append(promotional)
    
    automated = marketing.create_email_campaign(sample_content, "automated_sequence")
    campaigns.append(automated)
    
    # Track performance
    performance = marketing.track_performance(campaigns)
    
    # Optimize campaigns
    optimized_campaigns = marketing.optimize_campaigns(performance, campaigns)
    
    # Save campaigns
    filepath = marketing.save_campaigns(optimized_campaigns)
    
    logger.info(f"Marketing automation completed: {len(campaigns)} campaigns created")
    
    # Print marketing summary
    print("\nMarketing Automation Summary:")
    print(f"Niche: {niche}")
    print(f"Campaigns Created: {len(campaigns)}")
    for campaign in campaigns:
        print(f"  - {campaign['type']} campaign: {campaign.get('campaign_type', '')}")
    
    print("\nPerformance Summary:")
    print(f"Impressions: {performance['overall']['impressions']}")
    print(f"Clicks: {performance['overall']['clicks']}")
    print(f"Conversions: {performance['overall']['conversions']}")
    print(f"Revenue: ${performance['overall']['revenue']:.2f}")
    print(f"CTR: {performance['overall']['ctr']:.2f}%")
    print(f"Conversion Rate: {performance['overall']['conversion_rate']:.2f}%")

def main():
    """Main entry point for the application."""
    # Parse command line arguments
    args = parse_arguments()
    
    # Print banner
    print_banner()
    
    # Validate niche
    if not validate_niche(args.niche):
        logger.error(f"Invalid niche: {args.niche}")
        print(f"Error: Invalid niche '{args.niche}'. Available niches:")
        for niche in AFFILIATE_NICHES.keys():
            print(f"  - {niche}")
        return 1
    
    # Print workflow visualization
    print_workflow_visualization()
    
    # Run the selected mode
    if args.mode == "full":
        run_full_workflow(args.niche, args.domain, args.state_file)
    elif args.mode == "research":
        run_research_mode(args.niche)
    elif args.mode == "content":
        run_content_mode(args.niche)
    elif args.mode == "website":
        run_website_mode(args.niche, args.domain)
    elif args.mode == "marketing":
        run_marketing_mode(args.niche)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
