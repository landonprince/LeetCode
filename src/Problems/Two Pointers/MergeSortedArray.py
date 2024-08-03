class MergeSortedArray:
    from typing import List
    
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/merge-sorted-array/description/"
        self.instructions = (
            "You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, "
            "representing the number of elements in nums1 and nums2 respectively.\n"
            "Merge nums1 and nums2 into a single array sorted in non-decreasing order.\n"
            "The final sorted array should not be returned by the function, but instead be stored inside the array nums1."
        )
        self.tags = ["Array", "Two Pointers"]

    def solution(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # Pointer for the position in nums1 to fill
        p = m + n - 1

        # Compare elements from the end and fill nums1 from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, fill them in nums1
        # Note: if p1 >= 0, the remaining elements are already in place
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

    def test(self):
        # Test cases
        test_cases = [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1])
        ]

        for nums1, m, nums2, n, expected in test_cases:
            nums1_copy = nums1[:]
            self.solution(nums1_copy, m, nums2, n)
            assert nums1_copy == expected, f"Test failed: expected {expected}, got {nums1_copy}"
            print(f"Test passed for nums1 = {nums1}, nums2 = {nums2}: {nums1_copy}")

    def __str__(self):
        return (
            f"Problem: Merge Sorted Array\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = MergeSortedArray()
print(solution)  # Display problem information
solution.test()  # Run tests