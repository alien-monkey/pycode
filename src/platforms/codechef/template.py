"""
CodeChef Solution Template
=========================

This template provides a standardized structure for CodeChef solutions
with contest-specific features.

Usage:
    python solutions/codechef/template.py
"""

import sys
import time
from dataclasses import dataclass
from typing import Any, List, Tuple

from utils.benchmarking.performance_analyzer import PerformanceAnalyzer
from utils.testing.test_runner import TestRunner


@dataclass
class TestCase:
    """Test case structure for CodeChef problems"""

    input: str
    expected: str
    description: str = ""
    timeout: float = 1.0  # seconds
    subtask: int = 1  # For subtask-based scoring


class Solution:
    """
    Base solution class for CodeChef problems

    Replace the method implementation with your solution
    """

    def solve(self, input_data: str) -> str:
        """
        Main solution method
        Override this method with your implementation

        Args:
            input_data: Raw input string from CodeChef

        Returns:
            Formatted output string
        """
        raise NotImplementedError("Solution not implemented")

    def solve_optimized(self, input_data: str) -> str:
        """
        Optimized solution method
        Implement your most efficient solution here
        """
        return self.solve(input_data)


def get_test_cases() -> List[TestCase]:
    """
    Define your test cases here
    Use raw input strings as they would appear in CodeChef
    """
    return [
        # TestCase(
        #     input="1\n5\n1 2 3 4 5",
        #     expected="15",
        #     description="Sample test case"
        # ),
    ]


def parse_input(input_data: str) -> Any:
    """
    Parse input data based on problem requirements
    Override this method for specific problems
    """
    lines = input_data.strip().split("\n")
    return lines


def format_output(result: Any) -> str:
    """
    Format output according to problem requirements
    Override this method for specific problems
    """
    return str(result)


def main():
    """Main execution function"""
    solution = Solution()
    test_runner = TestRunner()
    performance_analyzer = PerformanceAnalyzer()

    # Run tests
    test_cases = get_test_cases()
    if test_cases:
        print("Running tests...")
        test_runner.run_tests(solution, test_cases)

    # Performance analysis
    print("\nRunning performance analysis...")
    performance_analyzer.analyze(solution, test_cases)

    # Interactive mode for manual testing
    print("\nEntering interactive mode...")
    print("Enter your test input (or 'quit' to exit):")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == "quit":
                break

            # Parse and solve
            parsed_input = parse_input(user_input)
            result = solution.solve(user_input)
            formatted_output = format_output(result)
            print(f"Output: {formatted_output}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
