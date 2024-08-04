from problems.abstract_problem import AbstractProblem

class ValidParentheses(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Valid Parentheses",
            difficulty = "easy",
            link = "https://leetcode.com/problems/valid-parentheses/description/",
            instructions = (
                "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', "
                "determine if the input string is valid.\n"
                "An input string is valid if:\n"
                "1. Open brackets must be closed by the same type of brackets.\n"
                "2. Open brackets must be closed in the correct order."
            ),
            tags = ["String", "Stack"]
        )
    def solution(self, s: str) -> bool:
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

        # Return True if the stack is empty (all parentheses are closed properly)
        return len(stack) == 0

    def test(self):
        # Test cases
        test_cases = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([)]", False),
            ("{[]}", True),
            ("", True),  # Edge case: empty string
            ("[", False)  # Unmatched opening bracket
        ]

        for s, expected in test_cases:
            result = self.solution(s)
            assert result == expected, f"Test failed: expected {expected}, got {result}"
            print(f"Test passed for s = '{s}': {result}")

    def __str__(self):
        return (
            f"Problem: Valid Parentheses\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

    def __str__(self):
            return super().__str__()
