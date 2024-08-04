from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaxDepthBinaryTree(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Maximum Depth of Binary Tree",
            difficulty = "easy",
            link = "https://leetcode.com/problems/maximum-depth-of-binary-tree/description/",
            instructions = (
                "Given the root of a binary tree, return its maximum depth.\n"
                "A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."
            ),
            tags = ["Binary Tree", "Depth-First Search"]
        )

    def solution(self, root: Optional[TreeNode]) -> int:
        # Base case: if the node is None, the depth is 0
        if root is None:
            return 0

        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.solution(root.left)
        right_depth = self.solution(root.right)

        # Return the maximum depth of the left and right subtrees plus 1 for the current node's depth
        return max(left_depth, right_depth) + 1

    def test(self):
        # Construct a binary tree for testing
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.right.right = TreeNode(4)

        # Test case 1
        expected_result = 3
        result = self.solution(root1)
        assert result == expected_result, f"Test failed: expected {expected_result}, got {result}"
        print(f"Test passed for test case 1: {result}")

        # Test case 2: Single node
        root2 = TreeNode(1)
        expected_result = 1
        result = self.solution(root2)
        assert result == expected_result, f"Test failed: expected {expected_result}, got {result}"
        print(f"Test passed for test case 2: {result}")

        # Test case 3: Empty tree
        root3 = None
        expected_result = 0
        result = self.solution(root3)
        assert result == expected_result, f"Test failed: expected {expected_result}, got {result}"
        print(f"Test passed for test case 3: {result}")

        # Test case 4: More complex tree
        root4 = TreeNode(3)
        root4.left = TreeNode(9)
        root4.right = TreeNode(20)
        root4.right.left = TreeNode(15)
        root4.right.right = TreeNode(7)
        expected_result = 3
        result = self.solution(root4)
        assert result == expected_result, f"Test failed: expected {expected_result}, got {result}"
        print(f"Test passed for test case 4: {result}")

    def __str__(self):
        return super().__str__()

    