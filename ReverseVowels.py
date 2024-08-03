class ReverseVowels:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/reverse-vowels-of-a-string/description/"
        self.instructions = (
            "Given a string s, reverse only all the vowels in the string and return it.\n"
            "The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once."
        )
        self.tags = ["String", "Two Pointers"]

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
        # Test cases
        test_cases = [
            ("hello", "holle"),
            ("leetcode", "leotcede"),
            ("aA", "Aa"),
            ("", ""),
            ("bcdfg", "bcdfg")  # No vowels to reverse
        ]

        for string, expected in test_cases:
            result = self.solution(string)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for string = '{string}': {result}")

    def __str__(self):
        return (
            f"Problem: Reverse Vowels of a String\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = ReverseVowels()
print(solution)  # Display problem information
solution.test()  # Run tests
