from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Create a set of nums1 and nums2
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the difference between the sets
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]

nums1 = [1, 2, 3, 5]
nums2 = [2, 3, 4, 5]
solution = Solution()
result = solution.findDifference(nums1, nums2)

print()
print(f"nums1 = {nums1}, nums2 = {nums2}, result = {result}")