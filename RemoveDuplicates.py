class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Initialize two pointers, one at the beginning of the list and one at the current position
        slow = 0
        fast = 1

        # Iterate through the list
        while fast < len(nums):
            # If the current number is different from the previous number, move the slow pointer forward
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

            # Move the fast pointer forward
            fast += 1

        # Return the length of the non-duplicate sublist
        return slow + 1

nums = [1,1,2,3,4,4,5,9,9,10]
solution = Solution()
result = solution.removeDuplicates(nums)

print()
print(f"nums = {nums}, result = {result}")