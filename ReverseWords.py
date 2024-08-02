class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()

        # Reverse the order of the words
        words.reverse()

        # Join the words back into a string
        reversed_string = " ".join(words)

        return reversed_string
        
s = "Hello my name is Landon"
solution = Solution()
result = solution.reverseWords(s)

print()
print(f"s = {s}, result = {result}")