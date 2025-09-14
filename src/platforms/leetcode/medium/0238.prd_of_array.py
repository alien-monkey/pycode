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

import math
import os
import sys
from typing import Any, List

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from utils.base_solution import BaseSolution, main_solution_runner


class PrdOfArray(BaseSolution):
    """
    Your solution class - focus only on the algorithm!

    Time Complexity: O(?) - describe your approach
    Space Complexity: O(?) - describe your approach
    """

    def __init__(self):
        super().__init__("Prd_Of_Array")

    def solve(self, nums: List[int]) -> Any:
        """
        Main solution method - implement your algorithm here

        Args:
            *args: Input arguments for the problem
            **kwargs: Additional keyword arguments

        Returns:
            Solution result
        """
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0] * n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result

    def solve_optimized(self, nums: List[int]) -> Any:
        """
        Optimized solution method - implement if you have a better approach
        """
        return self.solve(nums)

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
    main_solution_runner(PrdOfArray, "data/test_cases/0238.prd_of_array.toml")
