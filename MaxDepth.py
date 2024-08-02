from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        
        # Recursively calculate the depth of the left and right subtrees and return the maximum depth plus 1 for the current node's depth
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # Return the maximum depth of the left and right subtrees plus 1 for the current node's depth
        return max(leftDepth, rightDepth) + 1
    
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.right = TreeNode(4)

solution = Solution()
result = solution.maxDepth(root1)

print()
print(f"result = {result}")