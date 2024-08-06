from typing import Optional, List
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InorderTraversal(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Binary Tree Inorder Traversal",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/binary-tree-inorder-traversal/description/",
            instructions = (
                "Given the root of a binary tree, return the inorder traversal of its nodes' values."
            ),
            tags = ["Binary Tree", "Recursion"]
        )

    def solution(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []  # Reset result list for each traversal
        self.traverse(root)
        return self.result

    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.traverse(root.left)  # Traverse left subtree
        self.result.append(root.val)  # Visit node
        self.traverse(root.right)  # Traverse right subtree

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

        # Test cases
        test_cases = [
            (root, [4, 2, 5, 1, 6, 3, 7]),  # In-order traversal result
        ]

        # Run each test case
        for i, (tree, expected_result) in enumerate(test_cases, start=1):
            self.total_tests += 1
            result = self.solution(tree)
            if result == expected_result:
                self.tests_passed += 1


