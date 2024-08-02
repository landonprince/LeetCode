class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Initialize a dictionary to store the count of each number
        count_dict = {}

        # Iterate through the list of numbers
        for num in nums:
            # If the number is already in the dictionary, increment its count
            if num in count_dict:
                count_dict[num] += 1
            # If the number is not in the dictionary, add it with a count of 1
            else:
                count_dict[num] = 1

        # Find the number with the maximum count
        max_count = 0
        majority_element = None
        for num, count in count_dict.items():
            if count > max_count:
                max_count = count
                majority_element = num

        return majority_element
    
nums = [3,2,1,3,4,5,3,3]
solution = Solution()
result = solution.majorityElement(nums)

print()
print(f"nums = {nums}, result = {result}")