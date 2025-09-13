#!/usr/bin/env python3
"""
DSA Practice CLI Demo
====================

Demonstrates the CLI capabilities with examples.
"""

import subprocess


def run_command(cmd, description):
    """Run a CLI command and show the result"""
    print(f"\n{'='*60}")
    print(f"🎯 {description}")
    print(f"Command: {cmd}")
    print("=" * 60)

    try:
        result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=30)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
    except subprocess.TimeoutExpired:
        print("Command timed out")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Run CLI demo"""
    print("🚀 DSA Practice CLI Demo")
    print("=" * 60)

    # Check if CLI is installed
    try:
        result = subprocess.run(["dsa", "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ DSA CLI not found. Please run: pip install -e .")
            return
    except FileNotFoundError:
        print("❌ DSA CLI not found. Please run: pip install -e .")
        return

    # Demo commands
    commands = [
        ("dsa --help", "Show CLI help"),
        ("dsa list", "List all solutions"),
        (
            "dsa create 4 median-of-two-sorted-arrays --difficulty hard",
            "Create a new solution",
        ),
        ("dsa list", "List solutions after creation"),
        ("dsa search --platform leetcode", "Search LeetCode solutions"),
        ("dsa search --difficulty easy", "Search easy problems"),
        ("dsa run 0001.two_sum", "Run Two Sum solution"),
        ("dsa clean", "Clean up generated files"),
    ]

    for cmd, description in commands:
        run_command(cmd, description)

        # Add pause for interactive commands
        if "run" in cmd:
            print("\n⏸️  Press Enter to continue...")
            input()

    print("\n🎉 Demo completed!")
    print("\n📚 For more information, see:")
    print("   • CLI_USAGE_GUIDE.md - Complete usage guide")
    print("   • README.md - Project overview")
    print("   • dsa --help - CLI help")


if __name__ == "__main__":
    main()
