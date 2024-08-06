from problems.abstract_problem import AbstractProblem

class StrStr(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Find Index of First Occurrence in String",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/implement-strstr/description/",
            instructions = (
                "Implement strStr().\n"
                "Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, "
                "or -1 if needle is not part of haystack."
            ),
            tags = ["String"]
        )

    def solution(self, haystack: str, needle: str) -> int:
        # Check if needle is in haystack
        if needle not in haystack:
            return -1
        # Return the index of the first occurrence of needle in haystack
        return haystack.index(needle)

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ("hello world", "world", 6),
            ("abcdef", "def", 3),
            ("abcdef", "gh", -1),
            ("aaa", "a", 0),
            ("mississippi", "issip", 4)
        ]

        # Run each test case
        for i, (haystack, needle, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(haystack, needle)
            if result == expected:
                self.tests_passed += 1
                print(f"Test passed for test case {i} with haystack = '{haystack}', needle = '{needle}': {result}")
            else:
                print(f"Test failed for test case {i} with haystack = '{haystack}', needle = '{needle}': expected {expected}, got {result}")


