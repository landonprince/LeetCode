class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)  # Initialize result list with zeros

        # Convert each number from 0 to n to binary 
        for i in range(n + 1):
            bits = bin(i)[2:]  # Remove '0b' prefix
            # Count the number of '1' bits in the binary representation
            for j in range(len(bits)):
                if bits[j] == '1':
                    result[i] += 1
        
        return result
    
n = 5
solution = Solution()
result = solution.countBits(n)

print()
print(f"n = {n}, result = {result}")
                
                
