from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Initialize parent and current node pointers
        parent = None
        cur = root

        # Find the node to be deleted and its parent node
        while cur is not None and cur.val != key:
            parent = cur
            if key < cur.val: # If key is less, search left subtree
                cur = cur.left
            else: # If right is greater, search right subtree
                cur = cur.right

        # Cur should now be node to be deleted
        if not cur:
            return root # node to be deleted does not exist
        
        # Node with two children
        if cur.left is not None and cur.right is not None:
            successorParent = cur
            successor = cur.right

            # find inorder successor (smallest in the right subtree)
            while successor.left is not None:
                successorParent = successor
                successor = successor.left
            
            # Copy the inorder successor's content to the node to be deleted
            cur.val = successor.val
            cur = successor
            parent = successorParent
            key = successor.val

        # Node with only one child or no child
        child = cur.left if cur.left is not None else cur.right

        # Node with no child (root)
        if not parent: 
            return child
        
        # Node with one child
        if parent.left == cur:
            parent.left = child
        else:
            parent.right = child
        return root

        
