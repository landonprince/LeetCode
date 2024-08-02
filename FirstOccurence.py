class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
        
haystack = "hello world"
needle = "world"
solution = Solution()
result = solution.strStr(haystack, needle)

print()
print(f"haystack = {haystack}, needle = {needle}, result = {result}")