class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert n to binary and count 1s
        count = 0
        binary = bin(n)
        for num in binary:
            if num == '1':
                count += 1

        return count
    
n = 42
solution = Solution()
result = solution.hammingWeight(n)

print()
print(f"n = {n}, result = {result}")
        