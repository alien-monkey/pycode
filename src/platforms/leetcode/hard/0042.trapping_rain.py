"""
LeetCode Solution Template
=========================

Clean template for LeetCode solutions with minimal boilerplate.
Focus only on the algorithm implementation.

Usage:
    1. Copy this template to your problem file (use format: 0001.problem_name.py)
    2. Implement the solve() method
    3. Optionally implement solve_optimized() for better performance
    4. Create a TOML test file in data/test_cases/ (use format: 0001.problem_name.toml)
    5. Run: python your_solution.py

Example:
    python solutions/leetcode/easy/0001.two_sum.py
"""

import os
import sys
from typing import Any, List, Optional

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from utils.base_solution import BaseSolution, main_solution_runner


class Solution(BaseSolution):
    """
    Your solution class - focus only on the algorithm!

    Time Complexity: O(?) - describe your approach
    Space Complexity: O(?) - describe your approach
    """

    def __init__(self):
        super().__init__("Trapping_Rain")

    def solve(self, height: List[int]) -> Any:
        """
        Main solution method - implement your algorithm here

        Args:
            *args: Input arguments for the problem
            **kwargs: Additional keyword arguments

        Returns:
            Solution result
        """
        n = len(height)
        result = 0
        i = 0
        while i < n - 1:
            if height[i + 1] < height[i]:
                j, water = 1, 0
                while height[i + j] < height[i] and i + j < n:
                    water += max(0, height[i] - height[i + j])
                    j += 1
                i += j - 1
                result += water
            i += 1
        return result

    def solve_optimized(self, height: List[int]) -> Any:
        """
        Optimized solution method - implement if you have a better approach
        """
        return self.solve(height)

    def _parse_interactive_input(self, user_input: str) -> Any:
        """
        Parse interactive input - customize for your problem

        Args:
            user_input: Raw input from user

        Returns:
            Parsed input for your solve() method
        """
        # TODO: Implement input parsing for your problem
        # Example: return user_input.split() for space-separated input
        return user_input


if __name__ == "__main__":
    # Replace "0001.your_problem.toml" with your actual test file
    main_solution_runner(Solution, "data/test_cases/0042.trapping_rain.toml")
