from typing import List

class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:  
        countDictionary = {} 

        # Count the occurrences of each number in the array
        for num in nums: 
            if num in countDictionary: 
                countDictionary[num] += 1 
            else:
                countDictionary[num] = 1 

        # Check if the count of each number is unique
        uniqueCount = set()  

        # Return False if there are duplicate counts, else True 
        for count in countDictionary.values(): 
            if count in uniqueCount: 
                return False 
            uniqueCount.add(count)  

        return True 
    
nums = [1,2,2,1,1,3]
solution = Solution()
result = solution.uniqueOccurrences(nums)

print()
print(f"nums = {nums}, result = {result}")