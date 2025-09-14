import os
import sys
from typing import Any, List, Optional

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))

from utils.base_solution import BaseSolution, main_solution_runner


class TrieNode:
    """
    Trie node for storing words in reverse order to efficiently find palindrome pairs.

    🎯 KEY INSIGHT: We store words in REVERSE order in the trie!

    Why reverse? Let's see with an example:
    ======================================

    Words: ["abcd", "dcba", "lls", "s"]

    Normal Trie (WRONG approach):
    ============================
    Root
    ├── a
    │   └── b
    │       └── c
    │           └── d
    ├── d
    │   └── c
    │       └── b
    │           └── a
    ├── l
    │   └── l
    │       └── s
    └── s

    Reverse Trie (CORRECT approach):
    ===============================
    Root
    ├── d (from "dcba" - "abcd" reversed)
    │   └── c
    │       └── b
    │           └── a
    ├── a (from "abcd" - "dcba" reversed)
    │   └── b
    │       └── c
    │           └── d
    ├── s (from "sll" - "lls" reversed)
    │   └── l
    │       └── l
    └── s (from "s" - "s" reversed)

    Now when we traverse "abcd" normally against the reverse trie:
    - 'a' matches 'a' in "dcba" path
    - 'b' matches 'b' in "dcba" path
    - 'c' matches 'c' in "dcba" path
    - 'd' matches 'd' in "dcba" path
    - We've found a complete match! "abcd" + "dcba" = "abcddcba" ✓
    """

    def __init__(self):
        # Dictionary mapping characters to child nodes
        # Using dict instead of array for flexibility with any character set
        self.children = {}

        # Index of the word that ends at this node (-1 if no word ends here)
        # This helps us identify when we've found a complete word match
        self.word_end = -1

        # List of word indices that have palindromic suffixes from this point
        # This is crucial for finding palindrome pairs efficiently
        self.palindrome_suffixes = []


class PalindromePairs(BaseSolution):
    """
    LeetCode 336: Palindrome Pairs - Trie-based Solution

    🎯 PROBLEM STATEMENT:
    ====================
    Given a list of unique words, return all the pairs of distinct indices (i, j)
    such that the concatenation of the two words words[i] + words[j] is a palindrome.

    🧠 CORE CONCEPT - Why Use a Trie?
    ================================
    The naive approach would be O(n² * k) where we check every pair of words.
    Using a Trie allows us to optimize this by:

    1. Storing words in REVERSE order in the trie
    2. When traversing a word normally against the trie, we're checking if
       the current word's prefix matches any word's suffix
    3. If the remaining part of the current word is a palindrome, we found a pair!

    🔑 KEY INSIGHT:
    ==============
    For words[i] + words[j] to be a palindrome, one of these must be true:
    - words[i] is a palindrome and words[j] is empty (or vice versa)
    - words[i] = reverse(words[j]) (exact reverse)
    - words[i] = prefix + palindrome, and words[j] = reverse(prefix)
    - words[i] = reverse(suffix), and words[j] = palindrome + suffix

    The Trie helps us efficiently find these cases by storing reversed words
    and checking palindromic properties during traversal.

    🎨 VISUAL OVERVIEW - How the Algorithm Works:
    ===========================================

    Input: ["abcd", "dcba", "lls", "s", "sssll"]

    Step 1: Build Reverse Trie
    =========================

    Original Words → Reversed for Trie:
    ┌─────────────┬─────────────────┐
    │ "abcd"      │ "dcba"          │
    │ "dcba"      │ "abcd"          │
    │ "lls"       │ "sll"           │
    │ "s"         │ "s"             │
    │ "sssll"     │ "llsss"         │
    └─────────────┴─────────────────┘

    Trie Structure:
    ==============
    Root
    ├── d (from "dcba")
    │   └── c
    │       └── b
    │           └── a (word_end=0, palindrome_suffixes=[0])
    ├── a (from "abcd")
    │   └── b
    │       └── c
    │           └── d (word_end=1, palindrome_suffixes=[1])
    ├── s (from "sll" and "s")
    │   ├── l (from "sll")
    │   │   └── l (word_end=2, palindrome_suffixes=[2])
    │   └── (word_end=3, palindrome_suffixes=[3])
    └── l (from "llsss")
        └── l
            └── s
                └── s
                    └── s (word_end=4, palindrome_suffixes=[4])

    Step 2: Search for Pairs
    =======================

    🔍 Example 1: Search "abcd" against trie
    =======================================
    Current word: "abcd"
    Trie path: Root → d → c → b → a

    Traversal:
    - 'a' matches 'a' in "dcba" path ✓
    - 'b' matches 'b' in "dcba" path ✓
    - 'c' matches 'c' in "dcba" path ✓
    - 'd' matches 'd' in "dcba" path ✓
    - Found complete match! word_end=0 (which is "dcba")
    - Result: "abcd" + "dcba" = "abcddcba" ✓

    🔍 Example 2: Search "lls" against trie
    ======================================
    Current word: "lls"
    Trie path: Root → s → l → l

    Traversal:
    - 'l' doesn't exist in root's children
    - Return early (no matches possible)

    🔍 Example 3: Search "s" against trie
    ====================================
    Current word: "s"
    Trie path: Root → s

    Traversal:
    - 's' matches 's' in root's children ✓
    - Found word_end=3 (which is "lls")
    - Check if remaining part of "s" (empty) is palindrome: Yes!
    - Result: "s" + "lls" = "slls" ✓

    🎯 FINAL RESULT:
    ===============
    All palindrome pairs found:
    - [0, 1]: "abcd" + "dcba" = "abcddcba" ✓
    - [1, 0]: "dcba" + "abcd" = "dcbaabcd" ✓
    - [2, 4]: "lls" + "sssll" = "llssssll" ✓
    - [3, 2]: "s" + "lls" = "slls" ✓

    📚 DETAILED EXAMPLE WALKTHROUGH:
    ================================
    Words: ["abcd", "dcba", "lls", "s", "sssll"]

    Step 1 - Build Trie (storing in reverse):
    ========================================
    Original words → Reversed for trie:
    - "abcd" → "dcba"
    - "dcba" → "abcd"
    - "lls" → "sll"
    - "s" → "s"
    - "sssll" → "llsss"

    Trie Structure:
    ==============
    Root
    ├── d (from "dcba")
    │   └── c
    │       └── b
    │           └── a (word_end=0, palindrome_suffixes=[0])
    ├── a (from "abcd")
    │   └── b
    │       └── c
    │           └── d (word_end=1, palindrome_suffixes=[1])
    ├── s (from "sll" and "s")
    │   ├── l (from "sll")
    │   │   └── l (word_end=2, palindrome_suffixes=[2])
    │   └── (word_end=3, palindrome_suffixes=[3])
    └── l (from "llsss")
        └── l
            └── s
                └── s
                    └── s (word_end=4, palindrome_suffixes=[4])

    Step 2 - Search for pairs:
    =========================

    🔍 Checking "abcd" against trie:
    ================================
    Current word: "abcd"
    Trie path: Root → d → c → b → a
    Match found! word_end=0 (which is "dcba")
    Result: "abcd" + "dcba" = "abcddcba" ✓

    🔍 Checking "dcba" against trie:
    ================================
    Current word: "dcba"
    Trie path: Root → a → b → c → d
    Match found! word_end=1 (which is "abcd")
    Result: "dcba" + "abcd" = "dcbaabcd" ✓

    🔍 Checking "lls" against trie:
    ==============================
    Current word: "lls"
    Trie path: Root → s → l → l
    Match found! word_end=2 (which is "s")
    Result: "lls" + "s" = "llss" ✓

    🔍 Checking "s" against trie:
    ============================
    Current word: "s"
    Trie path: Root → s
    Match found! word_end=3 (which is "lls")
    Result: "s" + "lls" = "slls" ✓

    🔍 Checking "sssll" against trie:
    ================================
    Current word: "sssll"
    Trie path: Root → l → l → s → s → s
    Match found! word_end=4 (which is "sssll")
    But this is a self-pair, so we skip it.

    Also checking palindrome_suffixes at each node...
    Result: "sssll" + "lls" = "ssslllls" ✓

    Time Complexity: O(n * k^2) where n = number of words, k = average word length
    - Building trie: O(n * k^2) for inserting all words and checking palindromes
    - Searching: O(n * k^2) for finding all palindrome pairs
    Space Complexity: O(n * k) for the trie structure storing all words
    """

    def __init__(self):
        super().__init__("Palindrome_Pairs")

    def is_palindrome(self, word, left, right):
        """
        Check if substring word[left:right+1] is a palindrome.

        🔍 TWO-POINTER TECHNIQUE:
        ========================
        This function uses two pointers starting from both ends and moving inward.

        Example: Check if "racecar" is a palindrome
        ==========================================

        Step 1: left=0, right=6
        word[0] = 'r', word[6] = 'r' → Match! ✓

        Step 2: left=1, right=5
        word[1] = 'a', word[5] = 'a' → Match! ✓

        Step 3: left=2, right=4
        word[2] = 'c', word[4] = 'c' → Match! ✓

        Step 4: left=3, right=3
        left >= right, so we stop → It's a palindrome! ✓

        Visual representation:
        =====================
        "racecar"
         ↑     ↑
         l     r  (Step 1: 'r' == 'r' ✓)

        "racecar"
          ↑   ↑
          l   r  (Step 2: 'a' == 'a' ✓)

        "racecar"
           ↑ ↑
           l r  (Step 3: 'c' == 'c' ✓)

        "racecar"
            ↑
            l,r  (Step 4: l >= r, stop ✓)

        Args:
            word: The string to check
            left: Starting index (inclusive)
            right: Ending index (inclusive)

        Returns:
            bool: True if the substring is a palindrome, False otherwise
        """
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def add_word(self, root, word, index):
        """
        Add word to trie in REVERSE order with its index.

        🎯 CORE INSIGHT: We store words in REVERSE order!
        ================================================

        Why reverse? Let's trace through an example:
        ===========================================

        Example: Adding "lls" (index=2) to the trie
        ==========================================

        Step 1: Reverse "lls" → "sll"
        Step 2: Process each character in "sll"

        📊 DETAILED TRACE:
        =================

        Initial state:
        =============
        Root
        (empty trie)

        Processing "sll" (reversed "lls"):
        =================================

        i=0, char='s':
        - Check if word[0:3-0-1] = word[0:2] = "ll" is palindrome
        - "ll" is palindrome! ✓
        - Add index 2 to palindrome_suffixes at root
        - Create 's' child: Root → s

        i=1, char='l':
        - Check if word[0:3-1-1] = word[0:1] = "l" is palindrome
        - "l" is palindrome! ✓
        - Add index 2 to palindrome_suffixes at 's' node
        - Create 'l' child: Root → s → l

        i=2, char='l':
        - Check if word[0:3-2-1] = word[0:0] = "" is palindrome
        - "" is palindrome! ✓ (empty string is palindrome)
        - Add index 2 to palindrome_suffixes at 'l' node
        - Create 'l' child: Root → s → l → l
        - Mark this as end of word: word_end = 2

        Final trie state:
        ================
        Root
        └── s (palindrome_suffixes=[2])
            └── l (palindrome_suffixes=[2])
                └── l (word_end=2, palindrome_suffixes=[2])

        🧠 WHY THIS WORKS:
        =================
        When we later search for "lls" against this trie:
        - We traverse "lls" normally: l → l → s
        - We match the trie path: s → l → l (which is "lls" reversed)
        - We find a complete match at the end!
        - This means "lls" + "lls" could form a palindrome
        - But we skip self-pairs, so this is just for demonstration

        Args:
            root: Root of the trie
            word: Word to add to the trie
            index: Index of the word in the original array
        """
        node = root

        # Process word in REVERSE order - this is the key insight!
        for i, char in enumerate(reversed(word)):
            # Check if the remaining part of the original word (from start to current position)
            # forms a palindrome. If yes, this word can be paired with words that
            # have the current prefix as a suffix.
            if self.is_palindrome(word, 0, len(word) - i - 1):
                node.palindrome_suffixes.append(index)

            # Create child node if it doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode()

            # Move to the child node
            node = node.children[char]

        # Mark this node as the end of a word
        node.word_end = index

    def search_word(self, root, word, index, results):
        """
        Search for palindrome pairs for the given word using the trie.

        🔍 HOW SEARCH WORKS:
        ===================
        We traverse the current word normally while traversing the trie (
        which contains reversed words).

        This allows us to find cases where the current word's prefix matches some word's suffix.

        📚 DETAILED EXAMPLE:
        ===================
        Let's trace through searching for "lls" (index=2) in a trie that contains "s" (index=3).

        Trie state (after adding "s"):
        =============================
        Root
        └── s (word_end=3, palindrome_suffixes=[3])

        Search process for "lls":
        ========================

        Step 1: i=0, char='l'
        - Check if node.word_end >= 0: No (node.word_end = -1)
        - Check if 'l' exists in children: No
        - Return early (no matches possible)

        Wait! Let's try a better example with "s" searching for "lls":

        Step 1: i=0, char='s'
        - Check if node.word_end >= 0: Yes! (node.word_end = 3)
        - Check if node.word_end != index: Yes! (3 != 2)
        - Check if word[0:2] = "s" is palindrome: Yes! (single character)
        - Found match! Add [2, 3] to results
        - "lls" + "s" = "llss" ✓

        🎯 THREE CASES FOR PALINDROME PAIRS:
        ===================================

        CASE 1: Prefix + Palindrome + Reverse(Prefix)
        ============================================
        Current word: "lls" = "ll" + "s"
        Trie word: "s" (stored as "s")
        Result: "lls" + "s" = "ll" + "s" + "s" = "llss" ✓

        Visual:
        =======
        Current: "lls"
                 ↑
                 i=0 (remaining "lls" is not palindrome)

        Current: "lls"
                  ↑
                  i=1 (remaining "ls" is not palindrome)

        Current: "lls"
                   ↑
                   i=2 (remaining "s" is palindrome! ✓)

        CASE 2: Current + Word with Palindromic Suffix
        =============================================
        Current word: "s"
        Trie word: "lls" (stored as "sll", has palindromic suffix "ll")
        Result: "s" + "lls" = "s" + "ll" + "s" = "slls" ✓

        CASE 3: Exact Reverse Match
        ==========================
        Current word: "abcd"
        Trie word: "dcba" (stored as "abcd")
        Result: "abcd" + "dcba" = "abcddcba" ✓

        Args:
            root: Root of the trie
            word: Current word to find pairs for
            index: Index of the current word
            results: List to store found palindrome pairs
        """
        node = root

        # Traverse the word character by character
        for i, char in enumerate(word):
            # CASE 1: We've reached the end of a word in the trie
            # AND the remaining part of the current word is a palindrome
            # This means: current_word = prefix + palindrome, trie_word = reverse(prefix)
            # So current_word + trie_word = prefix + palindrome + reverse(prefix) = palindrome!
            if (
                node.word_end >= 0
                and node.word_end != index
                and self.is_palindrome(word, i, len(word) - 1)
            ):
                # We found a palindrome pair: current_word + trie_word
                # Example: current_word="lls", trie_word="s" (stored as "s")
                # "lls" = "ll" + "s", where "s" is a palindrome
                # "lls" + "s" = "ll" + "s" + "s" = "llss" (palindrome!)
                results.append([index, node.word_end])

            # If the current character doesn't exist in the trie, no more matches possible
            if char not in node.children:
                return

            # Move to the next node in the trie
            node = node.children[char]

        # CASE 2: We've completely traversed the current word
        # Check all words that have palindromic suffixes from this point
        # This handles cases where current_word + some_word_with_palindromic_suffix = palindrome
        for palindrome_index in node.palindrome_suffixes:
            if palindrome_index != index:
                # Found a palindrome pair: current_word + word_with_palindromic_suffix
                # Example: current_word="s", some_word="lls" (stored as "sll")
                # "s" + "lls" = "s" + "ll" + "s" = "slls" (palindrome!)
                results.append([index, palindrome_index])

        # CASE 3: We've reached the end of a word in the trie
        # This handles exact reverse matches: current_word + trie_word = palindrome
        if node.word_end >= 0 and node.word_end != index:
            # Found a palindrome pair: current_word + trie_word
            # Example: current_word="abcd", trie_word="dcba" (stored as "abcd")
            # "abcd" + "dcba" = "abcddcba" (palindrome!)
            results.append([index, node.word_end])

    def solve(self, words: List[str]) -> Any:
        """
        Main solution method - find all palindrome pairs using Trie data structure.

        🚀 ALGORITHM OVERVIEW:
        ======================
        1. Build a Trie with all words stored in REVERSE order
        2. For each word, traverse it normally while traversing the trie
        3. When we find matches, check if the remaining part forms a palindrome
        4. If yes, we've found a valid palindrome pair

        🎯 WHY REVERSE ORDER?
        ====================
        By storing words in reverse order, when we traverse a word normally against
        the trie, we're essentially checking if the current word's prefix matches
        any word's suffix. This is exactly what we need to form palindromes!

        📊 STEP-BY-STEP EXAMPLE:
        =======================
        Words: ["abcd", "dcba", "lls", "s", "sssll"]

        Step 1: Build Trie (reverse order)
        =================================
        "abcd" → "dcba" → Store in trie
        "dcba" → "abcd" → Store in trie
        "lls" → "sll" → Store in trie
        "s" → "s" → Store in trie
        "sssll" → "llsss" → Store in trie

        Final Trie:
        ==========
        Root
        ├── d (from "dcba")
        │   └── c
        │       └── b
        │           └── a (word_end=0)
        ├── a (from "abcd")
        │   └── b
        │       └── c
        │           └── d (word_end=1)
        ├── s (from "sll" and "s")
        │   ├── l (from "sll")
        │   │   └── l (word_end=2)
        │   └── (word_end=3)
        └── l (from "llsss")
            └── l
                └── s
                    └── s
                        └── s (word_end=4)

        Step 2: Search for pairs
        =======================

        🔍 Example: Checking "lls" against trie
        ======================================
        Current word: "lls"
        Trie traversal: Root → s → l → l

        At each step:
        - i=0, char='l': No match in trie, return
        - Wait, let's check "s" against "lls":

        🔍 Example: Checking "s" against trie
        ====================================
        Current word: "s"
        Trie traversal: Root → s

        At i=0, char='s':
        - Found word_end=3 (which is "lls")
        - Check if remaining part of "s" (empty) is palindrome: Yes!
        - Found pair: "s" + "lls" = "slls" ✓

        Args:
            words: List of words to find palindrome pairs from

        Returns:
            List of pairs [i, j] where words[i] + words[j] is a palindrome
        """
        if not words:
            return []

        # Step 1: Build the trie with all words stored in reverse order
        # This is the key optimization - by storing words in reverse,
        # we can efficiently check if a word's prefix matches any word's suffix
        root = TrieNode()
        results = []

        # Add all words to the trie in reverse order
        # Each word is processed character by character in reverse
        for i, word in enumerate(words):
            self.add_word(root, word, i)

        # Step 2: For each word, search for palindrome pairs
        # We traverse each word normally while traversing the trie (which contains reversed words)
        # This allows us to find cases where word1 + word2 forms a palindrome
        for i, word in enumerate(words):
            self.search_word(root, word, i, results)

        return results

    def solve_optimized(self, words: List[str]) -> Any:
        """
        Optimized solution method - same as main solution using Trie
        The Trie-based approach is already optimal for this problem
        """
        return self.solve(words)

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
    main_solution_runner(PalindromePairs, "data/test_cases/0336.palindrome_pairs.toml")
