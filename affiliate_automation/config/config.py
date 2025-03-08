"""
Configuration file for the Affiliate Marketing Automation System.
"""

# OpenAI API Configuration
OPENAI_API_KEY = "${OPENAI_API_KEY}"  # Will be loaded from environment variable

# Top Affiliate Niches Configuration (2025)
AFFILIATE_NICHES = {
    "online_learning": {
        "market_size": "$203.80 billion by 2025",
        "growth_rate": "8.20% annually",
        "top_programs": {
            "masterclass": {"commission": "25%", "cookie_duration": "30 days"},
            "teachable": {"commission": "30%", "cookie_duration": "90 days"},
            "udemy": {"commission": "15%", "cookie_duration": "7 days"},
            "coursera": {"commission": "20%", "cookie_duration": "30 days"},
            "skillshare": {"commission": "40%", "cookie_duration": "30 days"}
        },
        "content_types": ["course reviews", "learning path guides", "skill comparison", "career guides"],
        "keywords": ["best online courses", "learn programming", "digital skills", "certification courses"]
    },
    "cruise_travel": {
        "market_size": "$44.39 billion by 2025",
        "growth_rate": "4.77% annually",
        "top_programs": {
            "virgin_holidays": {"commission": "2%", "cookie_duration": "30 days"},
            "allianz_insurance": {"commission": "flexible", "cookie_duration": "30 days"},
            "royal_caribbean": {"commission": "5%", "cookie_duration": "60 days"},
            "carnival_cruise": {"commission": "3%", "cookie_duration": "45 days"}
        },
        "content_types": ["cruise reviews", "destination guides", "packing lists", "cruise comparisons"],
        "keywords": ["best cruise deals", "luxury cruises", "family cruise packages", "cruise insurance"]
    },
    "beauty_cosmetics": {
        "market_size": "$430 billion globally",
        "growth_rate": "5% annually",
        "top_programs": {
            "yves_rocher": {"commission": "15%", "cookie_duration": "30 days"},
            "olive_young": {"commission": "13%", "cookie_duration": "30 days"},
            "sephora": {"commission": "5%", "cookie_duration": "24 hours"},
            "ulta_beauty": {"commission": "4%", "cookie_duration": "7 days"}
        },
        "content_types": ["product reviews", "beauty tutorials", "skincare guides", "trend reports"],
        "keywords": ["korean skincare", "organic makeup", "beauty products", "skincare routine"]
    },
    "home_decor": {
        "market_size": "$139 billion by 2025",
        "growth_rate": "3.85% annually",
        "top_programs": {
            "pier_1": {"commission": "4%", "cookie_duration": "7 days"},
            "rug_source": {"commission": "10%", "cookie_duration": "180 days"},
            "wayfair": {"commission": "7%", "cookie_duration": "7 days"},
            "pottery_barn": {"commission": "5%", "cookie_duration": "30 days"}
        },
        "content_types": ["interior design guides", "product reviews", "room makeovers", "seasonal decor"],
        "keywords": ["home decor ideas", "interior design", "furniture deals", "home makeover"]
    },
    "outdoors_products": {
        "market_size": "$50+ billion globally",
        "growth_rate": "6% annually",
        "top_programs": {
            "enigma_fishing": {"commission": "20%", "cookie_duration": "30 days"},
            "backcountry": {"commission": "8%", "cookie_duration": "30 days"},
            "rei": {"commission": "5%", "cookie_duration": "15 days"},
            "cabelas": {"commission": "3%", "cookie_duration": "7 days"}
        },
        "content_types": ["gear reviews", "outdoor guides", "comparison articles", "adventure stories"],
        "keywords": ["fishing gear", "camping equipment", "hiking essentials", "outdoor adventure"]
    }
}

# AI Tools Configuration
AI_TOOLS = {
    "content_generation": {
        "openai_gpt4": {
            "api_endpoint": "https://api.openai.com/v1/chat/completions",
            "model": "gpt-4",
            "temperature": 0.7,
            "max_tokens": 2000
        },
        "article_types": {
            "product_review": {
                "structure": ["introduction", "product_overview", "features", "benefits", "drawbacks", "comparison", "conclusion"],
                "word_count": 1500
            },
            "buying_guide": {
                "structure": ["introduction", "market_overview", "key_considerations", "top_products", "recommendations", "conclusion"],
                "word_count": 2000
            },
            "how_to": {
                "structure": ["introduction", "materials_needed", "step_by_step", "tips", "conclusion"],
                "word_count": 1200
            }
        }
    },
    "website_creation": {
        "ai_website_builder": {
            "templates": ["affiliate_blog", "product_review", "comparison_site"],
            "features": ["responsive", "seo_optimized", "fast_loading", "conversion_focused"]
        },
        "hosting": {
            "provider": "aws_lightsail",
            "monthly_cost": "$3.50",
            "features": ["auto_scaling", "cdn", "ssl_certificate"]
        }
    },
    "marketing_automation": {
        "email_marketing": {
            "provider": "mailchimp",
            "features": ["automated_sequences", "a/b_testing", "personalization"]
        },
        "social_media": {
            "platforms": ["pinterest", "instagram", "twitter", "facebook"],
            "posting_frequency": {
                "pinterest": 5,
                "instagram": 3,
                "twitter": 7,
                "facebook": 2
            }
        }
    },
    "analytics": {
        "tracking": {
            "google_analytics": True,
            "hotjar": True,
            "facebook_pixel": True
        },
        "reporting": {
            "frequency": "weekly",
            "metrics": ["traffic", "conversion_rate", "revenue", "top_products"]
        }
    }
}

# Workflow Configuration
WORKFLOW_CONFIG = {
    "content_creation": {
        "articles_per_week": 3,
        "publishing_schedule": ["monday", "wednesday", "friday"],
        "content_refresh": "monthly"
    },
    "seo_optimization": {
        "keyword_research": "weekly",
        "backlink_building": "daily",
        "content_update": "monthly"
    },
    "social_promotion": {
        "platforms": ["pinterest", "twitter", "facebook"],
        "posting_frequency": "daily",
        "engagement_monitoring": "hourly"
    },
    "email_marketing": {
        "newsletter": "weekly",
        "promotional_emails": "bi-weekly",
        "automated_sequences": ["welcome", "abandoned_cart", "upsell"]
    },
    "performance_monitoring": {
        "analytics_review": "daily",
        "conversion_optimization": "weekly",
        "revenue_reporting": "monthly"
    }
}
