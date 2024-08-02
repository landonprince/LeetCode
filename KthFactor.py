class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        # Find all factors of n and store them in the factors list
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)

        # If there are less than k factors, return -1
        if len(factors) < k:
            return -1
        
        # Return the kth factor in the factors list
        for i in range(len(factors)):
            if i + 1 == k:
                return factors[i]
        
        return -1
    
n = 12
k = 3
solution = Solution
result = solution.kthFactor(solution, n, k)

print()
print(f"n = {n}, k = {k}, result = {result}")