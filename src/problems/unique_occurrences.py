from typing import List
from problems.abstract_problem import AbstractProblem

class UniqueOccurrences(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Unique Number of Occurrences",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/unique-number-of-occurrences/description/",
            instructions = (
                "Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique."
            ),
            tags = ["Array", "Map"]
        )

    def solution(self, nums: List[int]) -> bool:
        # Count the occurrences of each number in the array
        countDictionary = {}

        for num in nums:
            if num in countDictionary:
                countDictionary[num] += 1
            else:
                countDictionary[num] = 1

        # Check if the count of each number is unique
        uniqueCount = set()

        # Return False if there are duplicate counts, else True
        for count in countDictionary.values():
            if count in uniqueCount:
                return False
            uniqueCount.add(count)

        return True

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            ([1, 2, 2, 1, 1, 3], True),
            ([1, 2], False),
            ([3, 3, 3, 2, 2, 1], True),
            ([1, 2, 3, 4, 5], False),
            ([1, 1, 1, 2, 2, 3, 3, 3, 3], True),
            ([], True)  # Edge case: empty array
        ]

        # Run each test case
        for nums, expected in test_cases:
            self.total_tests += 1
            result = self.solution(nums)
            if result == expected:
                self.tests_passed += 1


