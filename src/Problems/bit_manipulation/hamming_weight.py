from problems.abstract_problem import AbstractProblem

class HammingWeight(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Hamming Weight",
            difficulty = "easy",
            link = "https://leetcode.com/problems/number-of-1-bits/description/",
            instructions = (
                "Write a function that takes an unsigned integer and returns the number of '1' bits it has "
                "(also known as the Hamming weight)."
            ),
            tags = ["Bit Manipulation"]
        )

    def solution(self, n: int) -> int:
        # Initialize count of '1' bits
        count = 0
        
        # Iterate while there are still bits in n
        while n:
            # Increment count for every '1' bit
            count += n & 1
            # Right shift n by one to check the next bit
            n >>= 1
        
        return count

    def test(self):
        test_cases = [
            (11, 3),  # binary: 1011
            (128, 1), # binary: 10000000
            (42, 3),  # binary: 101010
        ]
        for n, expected in test_cases:
            result = self.solution(n)
            assert result == expected, f"Test failed for n = {n}: expected {expected}, got {result}"
            print(f"Test passed for n = {n}: {result}")

    def __str__(self):
        return f"Problem: Hamming Weight\nDifficulty: {self.difficulty}\nLink: {self.link}\nInstructions: {self.instructions}"

    def __str__(self):
        return super().__str__()
