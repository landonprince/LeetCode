class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Iterate through the list
        i = 0
        while i < len(nums):
            # If the current number is not equal to the value, move the slow pointer forward
            if nums[i] != val:
                i += 1
            # If the current number is equal to the value, remove it from the list by swapping it with the last element and reducing the list length by 1
            else:
                nums[i], nums[-1] = nums[-1], nums[i]
                nums.pop()

        return i
    
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
result = solution.removeElement(nums, val)

print()
print(f"nums = {nums}, result = {result}")

