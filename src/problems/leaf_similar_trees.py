from typing import Optional, List
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LeafSimilarTrees(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Leaf-Similar Trees",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/leaf-similar-trees/description/",
            instructions = (
                "Consider all the leaves of a binary tree, from left to right order, the values of those leaves "
                "form a leaf value sequence.\n"
                "Two binary trees are considered leaf-similar if their leaf value sequence is the same.\n"
                "Return true if and only if the two given trees with root nodes root1 and root2 are leaf-similar."
            ),
            tags = ["Binary Tree", "Recursion"]
        )

    def solution(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Helper function to traverse the binary tree and collect the leaf values in a list
        def traverse(root: Optional[TreeNode], leaves: List[int]):
            if not root:
                return
            # If the current node is a leaf, add its value to the list of leaves
            if not root.left and not root.right:
                leaves.append(root.val)
            # Recursively traverse the left and right subtrees of the current node
            traverse(root.left, leaves)
            traverse(root.right, leaves)

        # Traverse both binary trees and collect the leaf values in separate lists
        leaves1 = []
        traverse(root1, leaves1)
        leaves2 = []
        traverse(root2, leaves2)

        # Compare the leaf sequences
        return leaves1 == leaves2

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Test case 1
        self.total_tests += 1
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)

        if self.solution(root1, root2) == True:
            self.tests_passed += 1

        # Test case 2
        self.total_tests += 1
        root1 = TreeNode(3)
        root1.left = TreeNode(5)
        root1.right = TreeNode(1)
        root1.left.left = TreeNode(6)
        root1.left.right = TreeNode(2)
        root1.right.left = TreeNode(9)
        root1.right.right = TreeNode(8)
        root1.left.right.left = TreeNode(7)
        root1.left.right.right = TreeNode(4)

        root2 = TreeNode(3)
        root2.left = TreeNode(5)
        root2.right = TreeNode(1)
        root2.left.left = TreeNode(6)
        root2.left.right = TreeNode(7)
        root2.right.left = TreeNode(4)
        root2.right.right = TreeNode(2)
        root2.right.right.left = TreeNode(9)
        root2.right.right.right = TreeNode(8)

        if self.solution(root1, root2) == True:
            self.tests_passed += 1

        # Test case 3
        self.total_tests += 1
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.left.left = TreeNode(4)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        root2.right.right = TreeNode(4)

        if self.solution(root1, root2) == False:
            self.tests_passed += 1




