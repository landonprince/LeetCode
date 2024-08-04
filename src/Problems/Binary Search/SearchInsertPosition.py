from typing import List
from Problems.AbstractProblem import AbstractProblem

class SearchInsertPosition(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Search Insert Position",
            difficulty = "easy",
            link = "https://leetcode.com/problems/search-insert-position/description/",
            instructions = (
                "Given a sorted array of distinct integers and a target value, return the index if the target is found.\n"
                "If not, return the index where it would be if it were inserted in order."
            ),
            tags = ["Array", "Binary Search"]
        )

    def solution(self, nums: List[int], target: int) -> int:
        # Initialize two pointers
        left = 0
        right = len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # If the target is found, return its index
            if nums[mid] == target:
                return mid

            # If the target is less than the middle element, update the right pointer
            elif nums[mid] > target:
                right = mid - 1

            # If the target is greater than the middle element, update the left pointer
            else:
                left = mid + 1

        # If the target is not found, return the index where it should be inserted
        return left

    def test(self):
        # Test cases
        test_cases = [
            ([1, 3, 5, 6], 5, 2),   # Target exists in the list
            ([1, 3, 5, 6], 2, 1),   # Target does not exist, insert between
            ([1, 3, 5, 6], 7, 4),   # Target does not exist, insert at the end
            ([1, 3, 5, 6], 0, 0),   # Target does not exist, insert at the beginning
            ([1], 0, 0),            # Single element list, target not in list
            ([1], 1, 0)             # Single element list, target is the only element
        ]

        for nums, target, expected in test_cases:
            result = self.solution(nums, target)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for nums = {nums}, target = {target}: {result}")

    def __str__(self):
        return (
            f"Problem: Search Insert Position\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

    def __str__(self):
        return super().__str__()
