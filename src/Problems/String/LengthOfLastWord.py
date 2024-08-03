class LengthOfLastWord:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/length-of-last-word/description/"
        self.instructions = (
            "Given a string s consisting of words and spaces, return the length of the last word in the string.\n"
            "A word is a maximal substring consisting of non-space characters only."
        )
        self.tags = ["String"]

    def solution(self, s: str) -> int:
        # Split the string into words
        words = s.split()

        # If the list is empty, return 0
        if not words:
            return 0

        # Return the length of the last word
        return len(words[-1])

    def test(self):
        # Test cases
        test_cases = [
            ("Hello World", 5),
            ("   fly me   to   the moon  ", 4),
            ("luffy is still joyboy", 6),
            ("", 0),
            ("single", 6)
        ]

        for s, expected in test_cases:
            result = self.solution(s)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for string = '{s}': {result}")

    def __str__(self):
        return (
            f"Problem: Length of Last Word\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = LengthOfLastWord()
print(solution)  # Display problem information
solution.test()  # Run tests
