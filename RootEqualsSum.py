from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # Check if sum of left and right subtrees is equal to root
        return root.val == root.left.val + root.right.val 
    
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(1)
solution = Solution()
result = solution.checkTree(root)

print()
print(f"result = {result}")