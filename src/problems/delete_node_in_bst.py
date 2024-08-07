from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DeleteNodeInBST(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Delete Node in a BST",
            difficulty = "Medium",
            link = "https://leetcode.com/problems/delete-node-in-a-bst/description/",
            instructions = (
                "Given a root node reference of a BST and a key, delete the node with the given key in the BST. "
                "Return the root node reference of the updated BST."
            ),
            tags = ["Binary Tree", "Depth-First Search", "Recursion"]
        )
    def solution(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        # If the key to be deleted is smaller than the root's key, it lies in the left subtree
        if key < root.val:
            root.left = self.solution(root.left, key)
        
        # If the key to be deleted is greater than the root's key, it lies in the right subtree
        elif key > root.val:
            root.right = self.solution(root.right, key)
        
        # If key is same as root's key, this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.find_min(root.right)
            
            # Copy the inorder successor's content to this node
            root.val = temp.val
            
            # Delete the inorder successor
            root.right = self.solution(root.right, temp.val)

        return root

    def find_min(self, node: TreeNode) -> TreeNode:
        current = node
        # Loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left
        return current

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Helper function to print the in-order traversal of the tree
        def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

        # Test cases
        test_cases = [
            (TreeNode(5,
                left=TreeNode(3, TreeNode(2), TreeNode(4)),
                right=TreeNode(6, None, TreeNode(7))
            ), 3, [2, 4, 5, 6, 7]),  # Test case 1

            (TreeNode(5,
                left=TreeNode(3, TreeNode(2), TreeNode(4)),
                right=TreeNode(6, None, TreeNode(7))
            ), 7, [2, 3, 4, 5, 6]),  # Test case 2
        ]

        # Run each test case
        for root, delete_value, expected_result in test_cases:
            self.total_tests += 1
            modified_root = self.solution(root, delete_value)
            result = inorder_traversal(modified_root)
            if result == expected_result:
                self.tests_passed += 1


