"""
LeetCode 1: Two Sum
==================

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

import os
import sys
from typing import List

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from utils.base_solution import BaseSolution, main_solution_runner


class TwoSum(BaseSolution):
    """
    Solution for Two Sum problem

    Time Complexity: O(n²) for brute force, O(n) for optimized
    Space Complexity: O(1) for brute force, O(n) for optimized
    """

    def __init__(self):
        super().__init__("Two Sum")

    def solve(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach - O(n²) time, O(1) space
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def solve_optimized(self, nums: List[int], target: int) -> List[int]:
        """
        Hash map approach - O(n) time, O(n) space
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

    def _parse_interactive_input(self, user_input: str) -> tuple:
        """
        Parse interactive input for Two Sum

        Expected format: "nums target"
        Examples:
        - "2,7,11,15 9" → nums=[2,7,11,15], target=9
        - "3,2,4 6" → nums=[3,2,4], target=6
        - "1,2,3,4,5 9" → nums=[1,2,3,4,5], target=9
        """
        try:
            parts = user_input.strip().split()
            if len(parts) != 2:
                return None

            nums = [int(x) for x in parts[0].split(",")]
            target = int(parts[1])
            return (nums, target)
        except ValueError:
            return None


if __name__ == "__main__":
    main_solution_runner(TwoSum, "data/test_cases/0001.two_sum.toml")
