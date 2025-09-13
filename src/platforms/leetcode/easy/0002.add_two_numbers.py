"""
LeetCode 2: Add Two Numbers
==========================

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

import os
import sys
from typing import List, Optional

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from utils.base_solution import BaseSolution, main_solution_runner


class AddTwoNumbers(BaseSolution):
    """
    Solution for Add Two Numbers problem

    Time Complexity: O(max(m,n)) where m and n are lengths of the two lists
    Space Complexity: O(max(m,n)) for the result list
    """

    def __init__(self):
        super().__init__("Add Two Numbers")

    def solve(self, l1: List[int], l2: List[int]) -> List[int]:
        """
        Add two numbers represented as linked lists (arrays for simplicity)
        """
        result = []
        carry = 0
        i, j = 0, 0

        while i < len(l1) or j < len(l2) or carry:
            val1 = l1[i] if i < len(l1) else 0
            val2 = l2[j] if j < len(l2) else 0

            total = val1 + val2 + carry
            carry = total // 10
            result.append(total % 10)

            i += 1
            j += 1

        return result

    def solve_optimized(self, l1: List[int], l2: List[int]) -> List[int]:
        """
        Same algorithm, but this shows how you can have different approaches
        """
        return self.solve(l1, l2)

    def _parse_interactive_input(self, user_input: str) -> tuple:
        """Parse interactive input for Add Two Numbers"""
        try:
            parts = user_input.strip().split("|")
            if len(parts) != 2:
                return None

            l1 = [int(x) for x in parts[0].split(",")]
            l2 = [int(x) for x in parts[1].split(",")]
            return (l1, l2)
        except ValueError:
            return None


if __name__ == "__main__":
    main_solution_runner(AddTwoNumbers, "data/test_cases/0002.add_two_numbers.toml")
