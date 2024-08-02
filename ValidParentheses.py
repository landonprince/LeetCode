class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to keep track of opening parentheses
        stack = []

        # Create a dictionary to map closing parentheses to opening parentheses
        mapping = {')': '(', ']': '[', '}': '{'}

        # Iterate through the string and check if each closing parenthesis matches an opening parenthesis in the stack
        for char in s:
            # If the current character is an opening parenthesis, push it onto the stack
            if char in mapping.values():
                stack.append(char)
            # If the current character is a closing parenthesis, check if it matches the top of the stack
            elif not stack or mapping[char] != stack.pop():
                return False

        return len(stack) == 0
    

s = "()[]{}"
solution = Solution()
result = solution.isValid(s)

print()
print(f"s = {s}, result = {result}")
