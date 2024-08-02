class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Initialize two pointers, one at the beginning of the list and one at the end position
        left = 0
        right = len(nums) - 1

        # Perform binary search until the left pointer is less than or equal to the right pointer
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


nums = [1, 3, 5, 6, 7, 8, 9, 10, 11, 12]
target = 5
solution = Solution()
result = solution.searchInsert(nums, target)

print()
print(f"nums = {nums}, target = {target}, result = {result}")
        
