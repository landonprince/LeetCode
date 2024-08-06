from problems.abstract_problem import AbstractProblem

class ReverseWords(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Reverse Words in a String",
            difficulty = "Medium",
            link = "https://leetcode.com/problems/reverse-words-in-a-string/description/",
            instructions = (
                "Given an input string s, reverse the order of the words.\n"
                "A word is defined as a sequence of non-space characters. "
                "The words in s will be separated by at least one space.\n"
                "Return a string of the words in reverse order concatenated by a single space."
            ),
            tags = ["String"]
        )

    def solution(self, s: str) -> str:
        # Split the string into words, reverse the list of words, and join them with a single space
        return " ".join(reversed(s.split()))

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ("Hello my name is Landon", "Landon is name my Hello"),
            ("  a  good   example  ", "example good a"),
            ("the sky is blue", "blue is sky the"),
            ("   hello world  ", "world hello"),
            ("a", "a"),  # Single word
            ("", ""),  # Empty string
        ]

        # Run each test case
        for i, (s, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(s)
            if result == expected:
                self.tests_passed += 1


