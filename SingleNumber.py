class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # XOR of a number with itself is 0, and XOR of a number with 0 is the number itself
        result = 0
        for num in nums:
            result ^= num

        return result
    
nums = [1,1,2,2,3,3,4,5,5]
solution = Solution()
result = solution.singleNumber(nums)

print()
print(f"nums = {nums}, result = {result}")
        
