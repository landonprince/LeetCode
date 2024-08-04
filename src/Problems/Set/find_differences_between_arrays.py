from typing import List
from problems.abstract_problem import AbstractProblem

class FindDifferenceBetweenArrays(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Find the Difference Between Two Arrays",
            difficulty = "easy",
            link = "https://leetcode.com/problems/find-the-difference-of-two-arrays/description/",
            instructions = (
                "Given two integer arrays nums1 and nums2, return a list answer of size 2 where:\n"
                "answer[0] is a list of all distinct integers in nums1 which are not present in nums2.\n"
                "answer[1] is a list of all distinct integers in nums2 which are not present in nums1.\n"
                "Note that the integers in the lists may be returned in any order."
            ),
            tags = ["Array, Set"]
        )

    def solution(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert nums1 and nums2 to sets to remove duplicates and allow for set operations
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the difference between the sets
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]

    def test(self):
        # Test cases
        test_cases = [
            ([1, 2, 3, 5], [2, 3, 4, 5], [[1], [4]]),
            ([1, 2, 3], [4, 5, 6], [[1, 2, 3], [4, 5, 6]]),
            ([1, 1, 2, 2], [2, 2, 3, 3], [[1], [3]])
        ]

        for nums1, nums2, expected in test_cases:
            result = self.solution(nums1, nums2)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed: {result}")

    def __str__(self):
        return super().__str__()
