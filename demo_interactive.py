#!/usr/bin/env python3
"""
Demo script showing the enhanced interactive mode features
"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(__file__))

from solutions.leetcode.easy.two_sum import TwoSum


def demo_interactive_features():
    """Demonstrate all interactive mode features"""
    print("🎮 Interactive Mode Demo - Enhanced Features")
    print("=" * 60)

    solution = TwoSum()
    solution.test_cases = solution.load_test_cases("data/test_cases/two_sum.toml")

    print("\n📋 Available Commands:")
    print("  help, h, ?     - Show help")
    print("  test, tests, t - List available test cases")
    print("  test N         - Run specific test case")
    print("  run, r         - Run all test cases")
    print("  benchmark, b   - Run performance benchmark")
    print("  analyze, a     - Run performance analysis")
    print("  quit, exit, q  - Exit interactive mode")
    print("  Ctrl+C, Ctrl+D - Exit interactive mode")

    print("\n🎯 Demo Commands:")
    print("1. 'test' - List all test cases")
    print("2. 'test 1' - Run first test case")
    print("3. 'benchmark' - Run performance benchmark")
    print("4. '2,7,11,15 9' - Test custom input")
    print("5. 'exit' - Exit")

    print("\n" + "=" * 60)
    print("Starting interactive mode...")
    print("=" * 60)

    # Start interactive mode
    solution.interactive_mode()


if __name__ == "__main__":
    demo_interactive_features()
