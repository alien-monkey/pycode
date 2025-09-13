import collections
import os
import sys
from typing import Any, List, Optional

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from utils.base_solution import BaseSolution, main_solution_runner


class SubstrConcat(BaseSolution):
    """
    Your solution class - focus only on the algorithm!

    Time Complexity: O(?) - describe your approach
    Space Complexity: O(?) - describe your approach
    """

    def __init__(self):
        super().__init__("Substr_Concat")

    def solve(self, s: str, words: List[str]) -> Any:
        """
        Main solution method - implement your algorithm here

        Args:
            *args: Input arguments for the problem
            **kwargs: Additional keyword arguments

        Returns:
            Solution result
        """
        s_len = len(s)
        word_count = len(words)
        result = []
        if s_len > 0 and word_count > 0:
            word_len = len(words[0])
            window_size = word_count * word_len

            for i in range(s_len - window_size - 1):
                freq = collections.Counter(words)
                substr = s[i : i + window_size]
                for j in range(word_count):
                    match = substr[j * word_len : (j + 1) * word_len]
                    if match in freq:
                        freq[match] -= 1
                    if sum(list(freq.values())) == 0:
                        result.append(i)
        return result

    def solve_optimized(self, s: str, words: List[str]) -> Any:
        """
        Optimized solution method - implement if you have a better approach
        """
        return self.solve(s, words)

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
    main_solution_runner(SubstrConcat, "data/test_cases/0030.substr_concat.toml")
