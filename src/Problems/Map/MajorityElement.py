from typing import List

class MajorityElement:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/majority-element/description/"
        self.instructions = (
            "Given an array nums of size n, return the majority element.\n"
            "The majority element is the element that appears more than ⌊n / 2⌋ times.\n"
            "You may assume that the majority element always exists in the array."
        )
        self.tags = ["Array, Map"]

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
        # Test cases
        test_cases = [
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
            ([1, 1, 2], 1),
            ([6, 5, 5], 5),
            ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4)
        ]

        for nums, expected in test_cases:
            result = self.solution(nums)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for nums = {nums}: {result}")

    def __str__(self):
        return (
            f"Problem: Majority Element\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = MajorityElement()
print(solution)  # Display problem information
solution.test()  # Run tests
