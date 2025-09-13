#!/bin/bash
# DSA Practice Repository Installation Script
# Run this after cloning the repository

set -e  # Exit on any error

echo "🎯 DSA Practice Repository Installation"
echo "======================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    echo "Please install Python 3.8 or higher and try again"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python 3.8 or higher is required (found $PYTHON_VERSION)"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is required but not installed"
    echo "Please install pip and try again"
    exit 1
fi

echo "✅ pip detected"

# Install the package
echo "🚀 Installing DSA Practice CLI..."
pip install -e .

# Install pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
pip install pre-commit
pre-commit install

# Verify installation
echo "🧪 Verifying installation..."
if dsa --version &> /dev/null; then
    echo "✅ DSA CLI installed successfully!"
else
    echo "❌ DSA CLI installation failed"
    exit 1
fi

echo ""
echo "🎉 Installation completed successfully!"
echo ""
echo "📚 Next steps:"
echo "   1. Run 'dsa --help' to see available commands"
echo "   2. Run 'dsa create 1 two-sum' to create your first solution"
echo "   3. Run 'dsa list' to see all solutions"
echo ""
echo "🔧 For virtual environment setup:"
echo "   Run 'source setup_venv.sh' to set up a clean environment"
echo ""
echo "📖 For complete documentation:"
echo "   See README.md and SETUP_GUIDE.md"
