from problems.abstract_problem import AbstractProblem

class ReverseVowels(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Reverse Vowels of a String",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/reverse-vowels-of-a-string/description/",
            instructions = (
                "Given a string s, reverse only all the vowels in the string and return it.\n"
                "The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once."
            ),
            tags = ["String", "Two Pointers"]
        )

    def solution(self, s: str) -> str:
        # Use two pointers to find vowels and swap them
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s_list[left] not in vowels:
                left += 1
            elif s_list[right] not in vowels:
                right -= 1
            else:
                # Swap vowels
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        # Join the characters back into a string and return it
        return ''.join(s_list)

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ("hello", "holle"),
            ("leetcode", "leotcede"),
            ("aA", "Aa"),
            ("", ""),
            ("bcdfg", "bcdfg")  # No vowels to reverse
        ]

        # Run each test case
        for i, (string, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(string)
            if result == expected:
                self.tests_passed += 1


