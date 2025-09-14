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


class ThreeSum(BaseSolution):
    """
    Your solution class - focus only on the algorithm!

    Time Complexity: O(?) - describe your approach
    Space Complexity: O(?) - describe your approach
    """

    def __init__(self):
        super().__init__("3Sum")

    def solve(self, nums: List[int]) -> Any:
        """
        Main solution method - implement your algorithm here

        Args:
            nums: List of integers

        Returns:
            List of unique triplets that sum to zero
        """
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

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
    main_solution_runner(ThreeSum, "data/test_cases/0015.3sum.toml")
