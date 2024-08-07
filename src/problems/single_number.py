from typing import List
from problems.abstract_problem import AbstractProblem

class SingleNumber(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Single Number",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/single-number/description/",
            instructions = (
                "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.\n"
                "You must implement a solution with a linear runtime complexity and use only constant extra space."
            ),
            tags = ["Array", "Bit Manipulation"]
        )

    def solution(self, nums: List[int]) -> int:
        # XOR all numbers in the array
        result = 0
        for num in nums:
            result ^= num  # XOR with each number

        return result

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ([1, 1, 2, 2, 3, 3, 4, 5, 5], 4),
            ([4, 1, 2, 1, 2], 4),
            ([2, 2, 1], 1),
            ([1], 1),  # Single element
            ([0, 0, 1], 1)
        ]

        # Run each test case
        for nums, expected in test_cases:
            self.total_tests += 1
            result = self.solution(nums)
            if result == expected:
                self.tests_passed += 1


