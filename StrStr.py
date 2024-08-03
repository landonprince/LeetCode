class StrStr:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/implement-strstr/description/"
        self.instructions = (
            "Implement strStr().\n"
            "Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, "
            "or -1 if needle is not part of haystack."
        )
        self.tags = ["String"]

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

    def __str__(self):
        return (
            f"Problem: Implement strStr\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = StrStr()
print(solution)  # Display problem information
solution.test()  # Run tests
