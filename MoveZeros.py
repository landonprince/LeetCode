class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Iterate through list to remove all zeros and append them at the end
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)

nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)

print()
print(f"nums = {nums}")

