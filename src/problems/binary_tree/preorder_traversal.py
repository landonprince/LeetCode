from typing import Optional, List
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PreorderTraversal(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Binary Tree Preorder Traversal",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/binary-tree-preorder-traversal/description/",
            instructions = (
                "Given the root of a binary tree, return the preorder traversal of its nodes' values.",
            ),
            tags = ["Binary Tree, Recursion"]
        )

    def solution(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result

    # Recursive function to perform pre-order traversal on the binary tree
    def traverse(self, root: Optional[TreeNode], result: List[int]) -> None:
        if not root:
            return
        result.append(root.val)  # Visit node
        self.traverse(root.left, result)  # Traverse left subtree
        self.traverse(root.right, result)  # Traverse right subtree

    def test(self):
        # Construct the binary tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        # Expected preorder traversal: [1, 2, 4, 5, 3, 6, 7]
        expected_result = [1, 2, 4, 5, 3, 6, 7]
        result = self.solution(root)
        assert result == expected_result, f"Test failed: expected {expected_result}, got {result}"
        print(f"Test passed: {result}")

    def __str__(self):
        return super().__str__()
