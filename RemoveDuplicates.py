class RemoveDuplicatesFromSortedArray:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"
        self.instructions = (
            "Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each "
            "unique element appears only once. The relative order of the elements should be kept the same.\n"
            "Return the length of the resulting array.\n"
            "Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."
        )
        self.tags = ["Array", "Two Pointers"]

    def solution(self, nums: list[int]) -> int:
        # Edge case: if the array is empty, return 0
        if not nums:
            return 0

        # Initialize two pointers
        slow = 0

        # Iterate through the list
        for fast in range(1, len(nums)):
            # If the current number is different from the previous number, move the slow pointer forward
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        # Return the length of the non-duplicate sublist
        return slow + 1

    def test(self):
        # Test cases
        test_cases = [
            ([1, 1, 2, 3, 4, 4, 5, 9, 9, 10], [1, 2, 3, 4, 5, 9, 10]),
            ([0, 0, 0, 0], [0]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([1, 1, 1, 2], [1, 2]),
            ([], []),
        ]

        for nums, expected in test_cases:
            nums_copy = nums[:]
            length = self.solution(nums_copy)
            assert nums_copy[:length] == expected, f"Test failed: expected {expected}, got {nums_copy[:length]}"
            print(f"Test passed for nums = {nums}: {nums_copy[:length]}")

    def __str__(self):
        return (
            f"Problem: Remove Duplicates from Sorted Array\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = RemoveDuplicatesFromSortedArray()
print(solution)  # Display problem information
solution.test()  # Run tests
