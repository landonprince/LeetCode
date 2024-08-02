class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create an empty dictionary to store the numbers and their indices
        num_dict = {}

        # Iterate over the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the complement of the current number with respect to the target
            complement = target - num

            # If the complement is found, return the indices of the complement and the current number
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # If the complement is not found, add the current number and its index to the dictionary
            num_dict[num] = i

solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = solution.twoSum(nums1, target1)

print()
print(f"nums = {nums1}, target = {target1}, result = {result1}")