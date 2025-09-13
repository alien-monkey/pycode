# DSA Practice Repository Makefile
# Similar to npm scripts in package.json

.PHONY: help install dev-install clean test lint format setup venv

# Default target
help:
	@echo "🎯 DSA Practice Repository Commands"
	@echo "=================================="
	@echo ""
	@echo "Setup Commands:"
	@echo "  make install     - Install DSA CLI and dependencies"
	@echo "  make dev-install - Install in development mode"
	@echo "  make setup       - Complete setup (install + pre-commit)"
	@echo "  make venv        - Create and setup virtual environment"
	@echo ""
	@echo "Development Commands:"
	@echo "  make test        - Run all tests"
	@echo "  make lint        - Run linting checks"
	@echo "  make format      - Format code with black"
	@echo "  make clean       - Clean up generated files"
	@echo ""
	@echo "Pre-commit Commands:"
	@echo "  make hooks       - Install basic pre-commit hooks"
	@echo "  make hooks-extended - Install extended pre-commit hooks"
	@echo "  make pre-commit  - Run pre-commit on staged files"
	@echo "  make pre-commit-all - Run pre-commit on all files"
	@echo "  make update-hooks - Update pre-commit hooks"
	@echo ""
	@echo "CLI Commands:"
	@echo "  dsa --help       - Show CLI help"
	@echo "  dsa create 1 two-sum - Create new solution"
	@echo "  dsa list         - List all solutions"

# Install DSA CLI
install:
	@echo "🚀 Installing DSA CLI..."
	pip install -e .
	@echo "✅ Installation complete!"

# Development installation
dev-install: install
	@echo "🔧 Installing development dependencies..."
	pip install pre-commit
	pre-commit install
	@echo "✅ Development setup complete!"

# Complete setup
setup: dev-install
	@echo "🎯 DSA Practice setup complete!"
	@echo "Run 'dsa --help' to get started"

# Create virtual environment
venv:
	@echo "🐍 Creating virtual environment..."
	python3 -m venv venv
	@echo "🔄 Activating virtual environment..."
	@echo "Run 'source venv/bin/activate' to activate"
	@echo "Then run 'make dev-install' to install dependencies"

# Run tests
test:
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v

# Run linting
lint:
	@echo "🔍 Running linting checks..."
	flake8 .
	mypy .

# Format code
format:
	@echo "🎨 Formatting code..."
	black .
	isort .

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf reports/
	rm -rf benchmark_results/
	@echo "✅ Cleanup complete!"

# Install pre-commit hooks
hooks:
	@echo "🔧 Installing pre-commit hooks..."
	pre-commit install
	@echo "✅ Hooks installed!"

# Install extended pre-commit hooks
hooks-extended:
	@echo "🔧 Installing extended pre-commit hooks..."
	cp .pre-commit-config-extended.yaml .pre-commit-config.yaml
	pre-commit install
	@echo "✅ Extended hooks installed!"

# Run pre-commit on all files
pre-commit-all:
	@echo "🔍 Running pre-commit on all files..."
	pre-commit run --all-files

# Run pre-commit on staged files only
pre-commit:
	@echo "🔍 Running pre-commit on staged files..."
	pre-commit run

# Update pre-commit hooks
update-hooks:
	@echo "⬆️  Updating pre-commit hooks..."
	pre-commit autoupdate
	@echo "✅ Hooks updated!"
