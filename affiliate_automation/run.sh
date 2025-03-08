#!/bin/bash

# Affiliate Marketing Automation System Runner

# Create necessary directories
mkdir -p logs
mkdir -p data/articles
mkdir -p data/websites
mkdir -p data/campaigns

# Check if OpenAI API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Warning: OPENAI_API_KEY environment variable is not set."
    echo "Some features may not work correctly."
fi

# Parse command line arguments
NICHE="online_learning"
MODE="full"
DOMAIN=""
STATE_FILE=""

while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --niche)
        NICHE="$2"
        shift
        shift
        ;;
        --mode)
        MODE="$2"
        shift
        shift
        ;;
        --domain)
        DOMAIN="$2"
        shift
        shift
        ;;
        --state-file)
        STATE_FILE="$2"
        shift
        shift
        ;;
        *)
        echo "Unknown option: $1"
        exit 1
        ;;
    esac
done

# Build command
CMD="python main.py --niche $NICHE --mode $MODE"

if [ ! -z "$DOMAIN" ]; then
    CMD="$CMD --domain $DOMAIN"
fi

if [ ! -z "$STATE_FILE" ]; then
    CMD="$CMD --state-file $STATE_FILE"
fi

# Run the command
echo "Running: $CMD"
$CMD
