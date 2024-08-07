from problems.abstract_problem import AbstractProblem

class LengthOfLastWord(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Length of Last Word",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/length-of-last-word/description/",
            instructions = (
                "Given a string s consisting of words and spaces, return the length of the last word in the string.\n"
                "A word is a maximal substring consisting of non-space characters only."
            ),
            tags = ["String"]
        )

    def solution(self, s: str) -> int:
        # Split the string into words
        words = s.split()

        # If the list is empty, return 0
        if not words:
            return 0

        # Return the length of the last word
        return len(words[-1])

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ("Hello World", 5),
            ("   fly me   to   the moon  ", 4),
            ("luffy is still joyboy", 6),
            ("", 0),
            ("single", 6)
        ]

        # Run each test case
        for s, expected in test_cases:
            self.total_tests += 1
            result = self.solution(s)
            if result == expected:
                self.tests_passed += 1


