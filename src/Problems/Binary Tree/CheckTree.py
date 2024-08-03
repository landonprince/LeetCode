from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CheckTree:
    def __init__(self):
        self.difficulty = "easy"
        self.link = "https://leetcode.com/problems/root-equals-sum-of-children/description/"
        self.instructions = (
            "You are given the root node of a binary tree with exactly 3 nodes: the root, its left child, and its right child.\n"
            "Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise."
        )
        self.tags = ["Binary Tree, Recursion"]

    def solution(self, root: Optional[TreeNode]) -> bool:
        # Check if the sum of left and right children is equal to the root's value
        if not root or not root.left or not root.right:
            return False
        return root.val == root.left.val + root.right.val

    def test(self):
        # Test case 1: root = 3, left = 2, right = 1, result = True
        root1 = TreeNode(3)
        root1.left = TreeNode(2)
        root1.right = TreeNode(1)
        result = self.solution(root1)
        assert result == True, f"Test failed: expected True, got {result}"
        print(f"Test passed for test case 1: result = {result}")

        # Test case 2: root = 10, left = 5, right = 5, result = True
        root2 = TreeNode(10)
        root2.left = TreeNode(5)
        root2.right = TreeNode(5)
        result = self.solution(root2)
        assert result == True, f"Test failed: expected True, got {result}"
        print(f"Test passed for test case 2: result = {result}")

        # Test case 3: root = 5, left = 3, right = 1, result = False
        root3 = TreeNode(5)
        root3.left = TreeNode(3)
        root3.right = TreeNode(1)
        result = self.solution(root3)
        assert result == False, f"Test failed: expected False, got {result}"
        print(f"Test passed for test case 3: result = {result}")

        # Test case 4: root = 6, left = 2, right = 4, result = True
        root4 = TreeNode(6)
        root4.left = TreeNode(2)
        root4.right = TreeNode(4)
        result = self.solution(root4)
        assert result == True, f"Test failed: expected True, got {result}"
        print(f"Test passed for test case 4: result = {result}")

    def __str__(self):
        return (
            f"Problem: Root Equals Sum of Children\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = CheckTree()
print(solution)  # Display problem information
solution.test()  # Run tests
