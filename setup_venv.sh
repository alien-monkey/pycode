#!/bin/bash
# Virtual environment activation script
# This script sets up the DSA Practice environment

echo "🐍 Setting up DSA Practice environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install DSA CLI
echo "🚀 Installing DSA CLI..."
pip install -e .

# Install pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
pip install pre-commit
pre-commit install

echo "✅ DSA Practice environment ready!"
echo "🎯 Use 'dsa --help' to get started"
echo "💡 Run 'source venv/bin/activate' to activate the environment"
