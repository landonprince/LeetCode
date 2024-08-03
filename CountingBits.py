class CountingBits:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/counting-bits/description/"
        self.instructions = (
            "Given an integer n, return an array ans of length n + 1 such that "
            "for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i."
        )
        self.tags = ["Bit Manipulation"]


    def solution(self, n: int) -> list[int]:
        # Create a result array of size n+1 initialized to 0
        result = [0] * (n + 1)
        
        # Iterate over each number from 1 to n
        for i in range(1, n + 1):
            # Use the relation result[i] = result[i >> 1] + (i & 1)
            result[i] = result[i >> 1] + (i & 1)
        
        return result

    def test(self):
        test_cases = [
            (2, [0, 1, 1]),
            (5, [0, 1, 1, 2, 1, 2]),
        ]
        for n, expected in test_cases:
            result = self.solution(n)
            assert result == expected, f"Test failed for n = {n}: expected {expected}, got {result}"
            print(f"Test passed for n = {n}: {result}")

    def __str__(self):
        return f"Problem: Counting Bits\nDifficulty: {self.difficulty}\nLink: {self.link}\nInstructions: {self.instructions}"

# Create an instance of the problem
solution = CountingBits()
print(solution)
print()  # Display problem information
solution.test()  # Run tests
print()