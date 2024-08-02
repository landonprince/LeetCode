class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Initialize the left and right pointers
        left = 1
        right = n

        # Perform binary search until the left pointer is less than the right pointer
        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # If the middle version is bad, update the right pointer to be one less than the middle index
            if isBadVersion(mid):
                right = mid
            # If the middle version is good, update the left pointer to be one more than the middle index
            else:
                left = mid + 1

        # Return the left pointer, which represents the first bad version
        return left
    
def isBadVersion(version: int) -> bool:
    return version == 5

n = 1345
bad = 5
solution = Solution()
result = solution.firstBadVersion(n)

print()
print(f"n = {n}, bad = {bad}, result = {result}")
    

            