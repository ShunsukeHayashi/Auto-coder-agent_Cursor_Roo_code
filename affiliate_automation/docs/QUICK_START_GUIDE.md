# AI-Powered Affiliate Marketing Automation System - Quick Start Guide

This guide provides a quick overview of how to get started with the AI-Powered Affiliate Marketing Automation System.

## Prerequisites

- Python 3.8+
- OpenAI API Key
- Basic understanding of affiliate marketing

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/affiliate-automation.git
   cd affiliate-automation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

## Basic Usage

### Running the Full Workflow

To run the complete affiliate marketing automation workflow:

```bash
python main.py --niche online_learning
```

This will execute the following steps:
1. Research the online learning niche
2. Create a website structure
3. Generate content for the website
4. Set up marketing campaigns
5. Track performance and optimize strategies

### Running Specific Modes

You can run specific parts of the workflow using the `--mode` parameter:

```bash
# Run only niche research
python main.py --niche online_learning --mode research

# Run only content generation
python main.py --niche online_learning --mode content

# Run only website creation
python main.py --niche online_learning --mode website --domain your-domain.com

# Run only marketing automation
python main.py --niche online_learning --mode marketing
```

### Using the Run Script

For convenience, you can use the provided shell script:

```bash
./run.sh --niche online_learning --mode full
```

## Available Niches

The system is pre-configured with the following niches:

1. **online_learning**: Online courses and educational content
2. **cruise_travel**: Cruise vacation packages and travel guides
3. **beauty_cosmetics**: Beauty products and cosmetics
4. **home_decoration**: Home decor and furniture
5. **outdoor_products**: Outdoor gear and equipment

## Output Files

The system generates the following output files:

- **Research Data**: `/data/research_[niche].json`
- **Articles**: `/data/articles/[article-title].json`
- **Website Configuration**: `/data/websites/[domain-name].json`
- **Marketing Campaigns**: `/data/campaigns/campaigns_[date].json`
- **Agent State**: `/data/agent_state.json`

## Next Steps

After running the system, you can:

1. Review the generated content in the `data/articles/` directory
2. Examine the website configuration in the `data/websites/` directory
3. Analyze the marketing campaigns in the `data/campaigns/` directory
4. Check the performance metrics in the agent state file

For more detailed information, refer to the following documentation:

- [Implementation Guide](IMPLEMENTATION_GUIDE.md)
- [Technical Architecture](TECHNICAL_ARCHITECTURE.md)
- [Niche Analysis](NICHE_ANALYSIS.md)
- [System Overview](SYSTEM_OVERVIEW.md)
- [User Guide (Japanese)](USER_GUIDE_JP.md)
- [Future Enhancements](FUTURE_ENHANCEMENTS.md)
