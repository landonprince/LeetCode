from typing import List

class UniqueOccurrences:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/unique-number-of-occurrences/description/"
        self.instructions = (
            "Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique."
        )
        self.tags = ["Array", "Map"]

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
        # Test cases
        test_cases = [
            ([1, 2, 2, 1, 1, 3], True),
            ([1, 2], False),
            ([3, 3, 3, 2, 2, 1], True),
            ([1, 2, 3, 4, 5], False),
            ([1, 1, 1, 2, 2, 3, 3, 3, 3], True),
            ([], True)  # Edge case: empty array
        ]

        for nums, expected in test_cases:
            result = self.solution(nums)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for nums = {nums}: {result}")

    def __str__(self):
        return (
            f"Problem: Unique Number of Occurrences\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = UniqueOccurrences()
print(solution)  # Display problem information
solution.test()  # Run tests