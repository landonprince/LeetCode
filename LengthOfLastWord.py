class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string into words
        words = s.split()

        # If the list is empty, return 0
        if len(words) == 0:
            return 0

        # Return the length of the last word
        return len(words[-1])
    
s = "Hello World"
solution = Solution()
result = solution.lengthOfLastWord(s)

print()
print(f"string = {s}, result = {result}")