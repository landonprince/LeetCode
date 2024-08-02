class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
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

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2,5,6]
m = 3
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)

print()
print(f"nums1 = {nums1}")
