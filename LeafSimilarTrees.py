from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Helper function to traverse the binary tree and collect the leaf values in a list
        def traverse(root: Optional[TreeNode], leaves: list):
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
        
        return leaves1 == leaves2

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

solution = Solution()
result = solution.leafSimilar(root1, root2)

print()
print(f"result = {result}")