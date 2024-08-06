from typing import List
from problems.abstract_problem import AbstractProblem

class MoveZeroes(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Move Zeroes",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/move-zeroes/description/",
            instructions = (
                "Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the "
                "non-zero elements.\n"
                "Note that you must do this in-place without making a copy of the array."
            ),
            tags = ["Array"]
        )

    def solution(self, nums: List[int]) -> None:
        # Two-pointer approach
        last_non_zero_found_at = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1

        # Fill the remaining positions with zeros
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0, 0, 1], [1, 0, 0]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([0, 0, 0, 0], [0, 0, 0, 0]),
            ([2, 1], [2, 1])
        ]

        # Run each test case
        for i, (nums, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            nums_copy = nums[:]
            self.solution(nums_copy)
            if nums_copy == expected:
                self.tests_passed += 1
                print(f"Test passed for test case {i} with nums = {nums}: {nums_copy}")
            else:
                print(f"Test failed for test case {i} with nums = {nums}: expected {expected}, got {nums_copy}")

