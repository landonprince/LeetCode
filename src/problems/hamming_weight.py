from problems.abstract_problem import AbstractProblem

class HammingWeight(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Hamming Weight",
            difficulty = "Easy",
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
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            (11, 3),  # binary: 1011
            (128, 1), # binary: 10000000
            (42, 3),  # binary: 101010
        ]

        # Run each test case
        for i, (n, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(n)
            if result == expected:
                self.tests_passed += 1
                print(f"Test passed for test case {i} with n = {n}: {result}")
            else:
                print(f"Test failed for test case {i} with n = {n}: expected {expected}, got {result}")

