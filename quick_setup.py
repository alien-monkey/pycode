#!/usr/bin/env python3
"""
Quick Setup Script for DSA Practice Repository
No circular dependencies - safe to run
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description=""):
    """Run a command and handle errors"""
    print(f"🔄 {description}")
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False


def check_dsa_cli():
    """Check if DSA CLI is already installed"""
    try:
        result = subprocess.run(["dsa", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ DSA CLI already installed!")
            return True
    except FileNotFoundError:
        pass
    return False


def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")

    # Install basic dependencies
    deps = [
        "click>=8.0.0",
        "rich>=13.0.0",
        "toml>=0.10.2",
        "pytest>=7.0.0",
        "pytest-benchmark>=4.0.0",
        "memory-profiler>=0.60.0",
        "psutil>=5.9.0",
    ]

    for dep in deps:
        if not run_command(f"pip install {dep}", f"Installing {dep}"):
            print(f"⚠️  Failed to install {dep}, continuing...")

    return True


def install_dsa_cli():
    """Install the DSA CLI in development mode"""
    if check_dsa_cli():
        return True

    print("🚀 Installing DSA Practice CLI...")

    # Install in development mode
    if run_command("pip install -e .", "Installing DSA CLI"):
        print("✅ DSA CLI installed successfully!")
        return True
    else:
        print("⚠️  DSA CLI installation failed, but continuing...")
        return True


def setup_pre_commit():
    """Set up pre-commit hooks"""
    print("🔧 Setting up pre-commit hooks...")

    # Install pre-commit
    if run_command("pip install pre-commit", "Installing pre-commit"):
        # Install hooks
        if run_command("pre-commit install", "Installing pre-commit hooks"):
            print("✅ Pre-commit hooks installed!")
            return True
        else:
            print("⚠️  Pre-commit hooks installation failed, continuing...")
            return True
    else:
        print("⚠️  Pre-commit installation failed, continuing...")
        return True


def create_venv_script():
    """Create a virtual environment setup script"""
    venv_script = """#!/bin/bash
# Virtual environment setup script for DSA Practice

echo "🐍 Setting up DSA Practice virtual environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install DSA CLI
echo "🚀 Installing DSA CLI..."
pip install -e .

# Install pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
pip install pre-commit
pre-commit install

echo "✅ DSA Practice virtual environment ready!"
echo "🎯 Use 'dsa --help' to get started"
echo "💡 Run 'source venv/bin/activate' to activate the environment"
"""

    with open("setup_venv.sh", "w") as f:
        f.write(venv_script)

    # Make executable
    os.chmod("setup_venv.sh", 0o755)
    print("✅ Created setup_venv.sh script")


def main():
    """Main setup function"""
    print("🎯 DSA Practice Repository Quick Setup")
    print("=" * 50)

    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)

    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

    # Install dependencies
    install_dependencies()

    # Install DSA CLI
    install_dsa_cli()

    # Set up pre-commit hooks
    setup_pre_commit()

    # Create virtual environment script
    create_venv_script()

    print("\n🎉 Quick setup completed!")
    print("\n📚 Next steps:")
    print("   1. Run 'dsa --help' to see available commands")
    print("   2. Run 'dsa create 1 two-sum' to create your first solution")
    print("   3. Run 'dsa list' to see all solutions")
    print("\n🔧 For virtual environment:")
    print("   Run 'source setup_venv.sh' to set up a clean environment")
    print("\n📖 For complete setup guide:")
    print("   See SETUP_GUIDE.md")


if __name__ == "__main__":
    main()
