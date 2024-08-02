from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = []

    # In-order traversal of a binary tree and store the values in a list
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.result

    # Recursive function to perform in-order traversal on the binary tree
    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.result.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.preorderTraversal(root)

print(result)
