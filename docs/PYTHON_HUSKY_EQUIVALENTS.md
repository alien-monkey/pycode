# 🐍 Python Equivalents of Husky (Node.js)

## **Overview**

This document explains Python equivalents to Node.js tools like Husky for automatic setup, pre-commit hooks, and development workflow automation.

## **🔧 Python Equivalents to Husky**

### **1. Pre-commit Hooks (Most Similar to Husky)**

**Node.js (Husky):**
```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "pre-push": "npm test"
    }
  }
}
```

**Python (Pre-commit):**
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 7.3.0
    hooks:
      - id: flake8
```

**Installation:**
```bash
# Install pre-commit (like husky install)
pip install pre-commit
pre-commit install

# Run hooks (like husky pre-commit)
pre-commit run --all-files
```

### **2. Package.json Scripts Equivalent**

**Node.js (package.json):**
```json
{
  "scripts": {
    "start": "node index.js",
    "test": "jest",
    "lint": "eslint .",
    "format": "prettier --write ."
  }
}
```

**Python (Makefile):**
```makefile
# Makefile
.PHONY: help test lint format

help:
	@echo "Available commands:"
	@echo "  make test    - Run tests"
	@echo "  make lint    - Run linting"
	@echo "  make format  - Format code"

test:
	python -m pytest tests/ -v

lint:
	flake8 .
	mypy .

format:
	black .
	isort .
```

**Usage:**
```bash
# Run commands (like npm run test)
make test
make lint
make format
```

### **3. Automatic CLI Installation**

**Node.js (package.json):**
```json
{
  "bin": {
    "my-cli": "./bin/my-cli.js"
  }
}
```

**Python (pyproject.toml):**
```toml
[project.scripts]
dsa = "dsa_practice.cli:main"
```

**Installation:**
```bash
# Install CLI (like npm install -g)
pip install -e .

# Use CLI
dsa --help
```

## **🚀 Complete Setup Solutions**

### **Option 1: Pre-commit Hooks (Recommended)**

**Setup:**
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files
```

**Benefits:**
- ✅ **Automatic code formatting** on commit
- ✅ **Linting and type checking** before commit
- ✅ **Security checks** with bandit
- ✅ **Import sorting** with isort
- ✅ **Works with any Python project**

### **Option 2: Makefile Commands**

**Setup:**
```bash
# Use Makefile commands
make help
make test
make lint
make format
```

**Benefits:**
- ✅ **Familiar syntax** for developers
- ✅ **Cross-platform** compatibility
- ✅ **Easy to extend** with new commands
- ✅ **No additional dependencies**

### **Option 3: Setup Scripts**

**Setup:**
```bash
# Run setup script
python quick_setup.py

# Or use install script
./install.sh
```

**Benefits:**
- ✅ **One-command setup** like `npm install`
- ✅ **Automatic dependency installation**
- ✅ **Environment validation**
- ✅ **Custom setup logic**

## **📁 Virtual Environment Handling**

### **✅ What to EXCLUDE from Git**

```gitignore
# Virtual environments
venv/
.venv/
env/
.env/
ENV/
env.bak/
venv.bak/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db
```

### **✅ What to INCLUDE in Git**

```
# Package configuration
pyproject.toml
requirements.txt
setup.py (if needed)

# Source code
src/
tests/
docs/

# Configuration files
.pre-commit-config.yaml
pytest.ini
.gitignore
Makefile

# Documentation
README.md
CHANGELOG.md
```

## **🎯 Development Workflow**

### **1. First Time Setup**

```bash
# Clone repository
git clone <repository-url>
cd project

# Install package
pip install -e .

# Setup pre-commit hooks
pip install pre-commit
pre-commit install

# Verify setup
dsa --help
```

### **2. Daily Development**

```bash
# Activate virtual environment (if using)
source venv/bin/activate

# Create new solution
dsa create 1 two-sum

# Edit solution
dsa edit 0001.two_sum

# Run solution
dsa run 0001.two_sum

# Test solution
dsa test 0001.two_sum

# Commit changes (hooks run automatically)
git add .
git commit -m "Add Two Sum solution"
```

### **3. Team Collaboration**

```bash
# Clone repository
git clone <repository-url>
cd project

# Setup development environment
make setup

# Start developing
dsa create 2 add-two-numbers
```

## **🔧 Advanced Features**

### **1. Custom Pre-commit Hooks**

```yaml
# .pre-commit-config.yaml
repos:
  # Custom hook for DSA CLI
  - repo: local
    hooks:
      - id: install-dsa-cli
        name: Install DSA CLI
        entry: pip install -e .
        language: system
        always_run: true
        stages: [pre-commit]
```

### **2. GitHub Actions Integration**

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - run: pip install -e .
      - run: dsa list
      - run: python -m pytest tests/
```

### **3. Virtual Environment Scripts**

```bash
#!/bin/bash
# setup_venv.sh
echo "🐍 Setting up virtual environment..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install package
pip install -e .

# Install pre-commit hooks
pip install pre-commit
pre-commit install

echo "✅ Setup complete!"
```

## **📊 Comparison Table**

| Feature | Node.js (Husky) | Python (Pre-commit) |
|---------|----------------|---------------------|
| **Pre-commit hooks** | ✅ Husky | ✅ Pre-commit |
| **Scripts** | ✅ package.json | ✅ Makefile |
| **CLI installation** | ✅ npm install -g | ✅ pip install -e . |
| **Automatic setup** | ✅ husky install | ✅ pre-commit install |
| **Cross-platform** | ✅ Yes | ✅ Yes |
| **Easy configuration** | ✅ JSON | ✅ YAML |
| **Rich ecosystem** | ✅ Yes | ✅ Yes |

## **🎉 Benefits**

### **1. Automatic Setup**
- ✅ **One command setup** like `npm install`
- ✅ **Pre-commit hooks** like Husky
- ✅ **Automatic CLI installation**
- ✅ **Development environment ready**

### **2. Team Collaboration**
- ✅ **Consistent environment** across team
- ✅ **Automatic code formatting** on commit
- ✅ **Linting and type checking** before commit
- ✅ **Easy onboarding** for new developers

### **3. Development Experience**
- ✅ **Makefile commands** like npm scripts
- ✅ **Rich CLI interface** with colors and tables
- ✅ **Comprehensive help** and error messages
- ✅ **Easy solution management**

## **🚀 Quick Start**

```bash
# 1. Clone repository
git clone <repository-url>
cd project

# 2. Install package
pip install -e .

# 3. Setup pre-commit hooks
pip install pre-commit
pre-commit install

# 4. Start using CLI
dsa --help
dsa create 1 two-sum
dsa run 0001.two_sum
```

## **📚 Additional Resources**

- **Pre-commit Documentation**: https://pre-commit.com/
- **Python Packaging Guide**: https://packaging.python.org/
- **Makefile Tutorial**: https://makefiletutorial.com/
- **Git Hooks Guide**: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks

The Python ecosystem provides **excellent equivalents** to Node.js tools like Husky, making development workflow automation **seamless and powerful**! 🎯
