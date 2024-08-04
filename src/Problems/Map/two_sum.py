from typing import List
from Problems.AbstractProblem import AbstractProblem

class TwoSum(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Two Sum",
            difficulty = "easy",
            link = "https://leetcode.com/problems/two-sum/description/",
            instructions = (
                "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n"
                "You may assume that each input would have exactly one solution, and you may not use the same element twice.\n"
                "You can return the answer in any order."
            ),
            tags = ["Array", "Map"]
        )

    def solution(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers and their indices
        num_dict = {}

        # Iterate over the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the complement of the current number with respect to the target
            complement = target - num

            # If the complement is found, return the indices of the complement and the current number
            if complement in num_dict:
                return [num_dict[complement], i]

            # If the complement is not found, add the current number and its index to the dictionary
            num_dict[num] = i

        # If no solution is found, return an empty list (although the problem guarantees a solution)
        return []

    def test(self):
        # Test cases
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([1, 5, 7, 9], 14, [2, 3]),
            ([1, 2, 3, 4, 5], 9, [3, 4])
        ]

        for nums, target, expected in test_cases:
            result = self.solution(nums, target)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for nums = {nums}, target = {target}: {result}")

    def __str__(self):
        return super().__str__()
