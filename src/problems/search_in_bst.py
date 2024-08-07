from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SearchInBST(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Search in a Binary Search Tree",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/search-in-a-binary-search-tree/description/",
            instructions = (
                "You are given the root of a binary search tree (BST) and an integer val.\n"
                "Find the node in the BST that the node's value equals val and return the subtree rooted with that node.\n"
                "If such a node does not exist, return null."
            ),
            tags = ["Binary Tree", "Recursion"]
        )

    def solution(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursive search for the value in the binary search tree (BST)
        if not root:
            return None
        if val < root.val:
            return self.solution(root.left, val)
        elif val > root.val:
            return self.solution(root.right, val)
        else:
            return root

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Helper function to print the tree in-order for debugging
        def print_in_order(node: Optional[TreeNode]) -> list:
            return (
                print_in_order(node.left) + [node.val] + print_in_order(node.right)
                if node else []
            )

        # Construct a binary search tree for testing
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)

        # Test case 1: Search for a value that exists
        self.total_tests += 1
        val1 = 2
        expected = [1, 2, 3]
        result = self.solution(root, val1)
        result_values = print_in_order(result)
        if result_values == expected:
            self.tests_passed += 1

        # Test case 2: Search for a value that does not exist
        self.total_tests += 1
        val2 = 5
        expected = None
        result = self.solution(root, val2)
        result_values = result.val if result else None
        if result_values == expected:
            self.tests_passed += 1

        # Test case 3: Search for the root value
        self.total_tests += 1
        val3 = 4
        expected = [1, 2, 3, 4, 6, 7]
        result = self.solution(root, val3)
        result_values = print_in_order(result)
        if result_values == expected:
            self.tests_passed += 1


