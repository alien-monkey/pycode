"""
Codeforces Solution Template
===========================

Clean template for Codeforces solutions with competitive programming features.

Usage:
    1. Copy this template to your problem file (use format: 0001.problem_name.py)
    2. Implement the solve() method
    3. Create a TOML test file in data/test_cases/ (use format: 0001.problem_name.toml)
    4. Run: python your_solution.py

Example:
    python solutions/codeforces/div2/0001.problem_a.py
"""

import os
import sys
from typing import Any, List, Tuple

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from utils.base_solution import BaseSolution, main_solution_runner


class Solution(BaseSolution):
    """
    Your Codeforces solution - focus on the algorithm!

    Time Complexity: O(?) - describe your approach
    Space Complexity: O(?) - describe your approach
    """

    def __init__(self):
        super().__init__("Your Problem Name")

    def solve(self, input_data: str) -> str:
        """
        Main solution method - implement your algorithm here

        Args:
            input_data: Raw input string from Codeforces

        Returns:
            Formatted output string
        """
        # TODO: Implement your solution
        # Parse input
        lines = input_data.strip().split("\n")

        # Your algorithm here
        result = 0

        # Format output
        return str(result)

    def solve_optimized(self, input_data: str) -> str:
        """
        Optimized solution method - implement if you have a better approach
        """
        return self.solve(input_data)

    def _parse_interactive_input(self, user_input: str) -> str:
        """
        Parse interactive input for Codeforces problems

        Args:
            user_input: Raw input from user

        Returns:
            Formatted input string
        """
        # For Codeforces, usually just return the input as-is
        return user_input


if __name__ == "__main__":
    # Replace "0001.your_problem.toml" with your actual test file
    main_solution_runner(Solution, "data/test_cases/0001.your_problem.toml")
