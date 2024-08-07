from problems.abstract_problem import AbstractProblem

class MergeStringsAlternately(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Merge Strings Alternately",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/merge-strings-alternately/description/",
            instructions = (
                "You are given two strings word1 and word2. Merge the strings by "
                "adding letters in alternating order, starting with word1. If a string " 
                "is longer than the other, append the additional letters onto the end of the merged string."
            ),
            tags = ["String", "Two-Pointers"]
        )
        
    def solution(self, word1: str, word2: str) -> str:
        # Initialize result string and pointers for word1 and word2
        result = ""
        i, j = 0, 0

        # Iterate until either word1 or word2 is exhausted
        while i < len(word1) and j < len(word2):
            # Append the current character from word1 to the result
            result += word1[i]
            # Increment the pointer for word1
            i += 1
            # Append the current character from word2 to the result
            result += word2[j]
            # Increment the pointer for word2
            j += 1

        # Append the remaining characters from word1 or word2, if any
        result += word1[i:] if i < len(word1) else word2[j:]

        return result
    
    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ("abc", "def", "adbecf"),
            ("abcde", "fghij", "afbgchdiej"),
            ("a", "b", "ab"),
            ("aa", "aa", "aaaa"),
        ]

        # Run each test case
        for word1, word2, expected in test_cases:
            self.total_tests += 1
            result = self.solution(word1, word2)
            if result == expected:
                self.tests_passed += 1