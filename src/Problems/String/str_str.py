from problems.abstract_problem import AbstractProblem

class StrStr(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Implement strStr()",
            difficulty = "easy",
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
        # Test cases
        test_cases = [
            ("hello world", "world", 6),
            ("abcdef", "def", 3),
            ("abcdef", "gh", -1),
            ("aaa", "a", 0),
            ("mississippi", "issip", 4)
        ]

        for haystack, needle, expected in test_cases:
            result = self.solution(haystack, needle)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for haystack = '{haystack}', needle = '{needle}': {result}")


