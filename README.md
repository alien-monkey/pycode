# DSA Practice Repository 🚀

A comprehensive Python repository for Data Structures and Algorithms practice with premium features like LeetCode Pro - **locally and free**!

## 🎯 Mission

Democratize access to premium DSA learning features by providing advanced analytics, debugging tools, performance analysis, and automated benchmarking - all locally without subscription costs.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repository-url>
cd pycode
./install.sh

# Start coding
dsa create 1 two-sum
dsa run 0001.two_sum
dsa list
```

## 📁 Repository Structure

```
pycode/
├── src/platforms/           # Platform-specific solutions
│   ├── leetcode/           # LeetCode problems (easy/medium/hard)
│   ├── codeforces/         # Codeforces problems (div1/div2/div3/div4)
│   ├── topcoder/           # TopCoder problems (srm/marathon)
│   └── codechef/           # CodeChef problems (long/short/cookoff/lunchtime)
├── utils/                   # Core utilities
├── tests/                   # Test suites
├── data/                    # Test cases and benchmarks
├── docs/                    # Documentation
└── tools/                   # Analysis tools
```

## 🛠️ Features

- **🎯 CLI Tool**: Create, run, test solutions with one command
- **📊 Advanced Analytics**: Performance metrics, complexity analysis
- **🐛 Debugging Tools**: Breakpoint debugging, step-by-step tracing
- **⚡ Performance Analysis**: Time/memory profiling, optimization suggestions
- **🔄 Automated Testing**: CI/CD pipeline with performance validation
- **🌐 Multi-Platform**: LeetCode, Codeforces, TopCoder, CodeChef support

## 📚 Documentation

- **[Setup Guide](docs/SETUP_GUIDE.md)** - Complete installation instructions
- **[CLI Usage](docs/CLI_USAGE_GUIDE.md)** - Command-line interface guide
- **[Python Husky Equivalents](docs/PYTHON_HUSKY_EQUIVALENTS.md)** - Development workflow tools
- **[Interactive Features](docs/INTERACTIVE_FEATURES.md)** - Advanced CLI features
- **[Filename Convention](docs/FILENAME_CONVENTION.md)** - File naming standards

## 🎮 CLI Commands

```bash
# Create solutions
dsa create 1 two-sum
dsa create --platform codeforces --division div2 1000 problem-a

# Run and test
dsa run 0001.two_sum
dsa test 0001.two_sum
dsa edit 0001.two_sum

# Manage solutions
dsa list
dsa search --platform leetcode --difficulty easy
dsa clean
```

## 🔧 Development

```bash
# Setup development environment
make setup

# Run tests
make test

# Format code
make format

# Run linting
make lint
```

## 🤝 Contributing

1. Fork the repository
2. Create solution: `dsa create <number> <problem-name>`
3. Implement and test your solution
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**Happy Coding! 🎉**

*The best way to learn algorithms is by solving problems. This repository provides all the tools you need to become a better problem solver.*