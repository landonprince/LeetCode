from typing import Optional, List
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PostorderTraversal(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Binary Tree Postorder Traversal",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/binary-tree-postorder-traversal/description/",
            instructions = (
                "Given the root of a binary tree, return the postorder traversal of its nodes' values."
            ),
            tags = ["Binary Tree", "Recursion"]
        )

    def solution(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result

    # Recursive function to perform post-order traversal on the binary tree
    def traverse(self, root: Optional[TreeNode], result: List[int]) -> None:
        if not root:
            return
        self.traverse(root.left, result)  # Traverse left subtree
        self.traverse(root.right, result)  # Traverse right subtree
        result.append(root.val)  # Visit node

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Construct the binary tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        # Test case 1
        self.total_tests += 1
        expected_result = [4, 5, 2, 6, 7, 3, 1]  # Expected postorder traversal
        result = self.solution(root)
        if result == expected_result:
            self.tests_passed += 1
            print(f"Test passed for test case 1: {result}")
        else:
            print(f"Test failed for test case 1: expected {expected_result}, got {result}")

