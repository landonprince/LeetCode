from typing import List
from problems.abstract_problem import AbstractProblem

class CountingBits(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Counting Bits",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/counting-bits/description/",
            instructions = (
                "Given an integer n, return an array ans of length n + 1 such that "
                "for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i."
            ),
            tags = ["Array", "Bit Manipulation"]
        )

    def solution(self, n: int) -> List[int]:
        # Create a result array of size n+1 initialized to 0
        result = [0] * (n + 1)
        
        # Iterate over each number from 1 to n
        for i in range(1, n + 1):
            # Use the relation result[i] = result[i >> 1] + (i & 1)
            result[i] = result[i >> 1] + (i & 1)
        
        return result

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Define test cases
        test_cases = [
            (2, [0, 1, 1]),
            (5, [0, 1, 1, 2, 1, 2]),
        ]

        # Run each test case
        for n, expected in test_cases:
            self.total_tests += 1
            result = self.solution(n)
            if result == expected:
                self.tests_passed += 1



