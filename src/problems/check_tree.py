from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CheckTree(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Root Equals Sum of Children",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/root-equals-sum-of-children/description/",
            instructions = (
                "You are given the root node of a binary tree with exactly 3 nodes: the root, its left child, and its right child.\n"
                "Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise."
            ),
            tags = ["Binary Tree", "Recursion"],
        )

    def solution(self, root: Optional[TreeNode]) -> bool:
        # Check if the sum of left and right children is equal to the root's value
        if not root or not root.left or not root.right:
            return False
        return root.val == root.left.val + root.right.val

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test cases
        test_cases = [
            (TreeNode(3, TreeNode(2), TreeNode(1)), True),  # Test case 1
            (TreeNode(10, TreeNode(5), TreeNode(5)), True),  # Test case 2
            (TreeNode(5, TreeNode(3), TreeNode(1)), False),  # Test case 3
            (TreeNode(6, TreeNode(2), TreeNode(4)), True),   # Test case 4
        ]

        for i, (root, expected) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(root)
            if result == expected:
                self.tests_passed += 1

                