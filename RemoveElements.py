from typing import List

class RemoveElement:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/remove-element/description/"
        self.instructions = (
            "Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. "
            "The relative order of the elements may be changed.\n"
            "Return the number of elements in nums which are not equal to val.\n"
            "Note that it is not necessary to change the input array's size in memory, just the number of elements considered."
        )
        self.tags = ["Array", "Two Pointers"]

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
        # Test cases
        test_cases = [
            ([3, 2, 2, 3], 3, [2, 2]),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
            ([4, 4, 4, 4], 4, []),
            ([1, 2, 3], 5, [1, 2, 3]),
            ([], 0, [])
        ]

        for nums, val, expected in test_cases:
            nums_copy = nums[:]
            length = self.solution(nums_copy, val)
            assert nums_copy[:length] == expected, f"Test failed: expected {expected}, got {nums_copy[:length]}"
            print(f"Test passed for nums = {nums}, val = {val}: {nums_copy[:length]}")

    def __str__(self):
        return (
            f"Problem: Remove Element\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = RemoveElement()
print(solution)  # Display problem information
solution.test()  # Run tests
