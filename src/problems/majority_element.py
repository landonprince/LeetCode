from typing import List
from problems.abstract_problem import AbstractProblem

class MajorityElement(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Majority Element",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/majority-element/description/",
            instructions = (
                "Given an array nums of size n, return the majority element.\n"
                "The majority element is the element that appears more than ⌊n / 2⌋ times.\n"
                "You may assume that the majority element always exists in the array."
            ),
            tags = ["Array", "Map"]
        )

    def solution(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the count of each number
        count_dict = {}

        # Iterate through the list of numbers
        for num in nums:
            # Increment the count for this number
            count_dict[num] = count_dict.get(num, 0) + 1

            # If the count is greater than half the length of nums, return the number
            if count_dict[num] > len(nums) // 2:
                return num

        # The majority element should have been found, but this is just a safety return
        return -1  # Alternatively, raise an exception since the problem guarantees a majority element

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
            ([1, 1, 2], 1),
            ([6, 5, 5], 5),
            ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4)
        ]

        # Run each test case
        for i, (nums, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(nums)
            if result == expected:
                self.tests_passed += 1


