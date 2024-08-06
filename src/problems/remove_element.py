from typing import List
from problems.abstract_problem import AbstractProblem

class RemoveElement(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Remove Element",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/remove-element/description/",
            instructions = (
                "Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. "
                "The relative order of the elements may be changed.\n"
                "Return the number of elements in nums which are not equal to val.\n"
                "Note that it is not necessary to change the input array's size in memory, just the number of elements considered."
            ),
            tags = ["Array", "Two Pointers"]
        )

    def solution(self, nums: List[int], val: int) -> int:
        # Initialize a pointer for the position to overwrite
        slow = 0

        # Iterate through the list
        for fast in range(len(nums)):
            # If the current number is not equal to the value, move it to the slow pointer's position
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        # Return the new length of the array without the value
        return slow

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ([3, 2, 2, 3], 3, [2, 2]),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
            ([4, 4, 4, 4], 4, []),
            ([1, 2, 3], 5, [1, 2, 3]),
            ([], 0, [])
        ]

        # Run each test case
        for i, (nums, val, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            nums_copy = nums[:]
            length = self.solution(nums_copy, val)
            if nums_copy[:length] == expected:
                self.tests_passed += 1
                print(f"Test passed for test case {i} with nums = {nums}, val = {val}: {nums_copy[:length]}")
            else:
                print(f"Test failed for test case {i} with nums = {nums}, val = {val}: expected {expected}, got {nums_copy[:length]}")

