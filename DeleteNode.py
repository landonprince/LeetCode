from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DeleteNodeInBST:
    def __init__(self):
        self.difficulty = "medium"
        self.link = "https://leetcode.com/problems/delete-node-in-a-bst/description/"
        self.instructions = (
            "Given a root node reference of a BST and a key, delete the node with the given key in the BST. "
            "Return the root node reference of the updated BST."
        )
        self.tags = ["Binary Search Tree, Depth-First Search"]

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
        # Helper function to print the in-order traversal of the tree
        def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

        # Test cases
        test_case_1 = TreeNode(5)
        test_case_1.left = TreeNode(3)
        test_case_1.right = TreeNode(6)
        test_case_1.left.left = TreeNode(2)
        test_case_1.left.right = TreeNode(4)
        test_case_1.right.right = TreeNode(7)

        # Perform test and verify output
        expected_result_1 = [2, 4, 5, 6, 7]
        modified_root_1 = self.solution(test_case_1, 3)
        result_1 = inorder_traversal(modified_root_1)
        assert result_1 == expected_result_1, f"Test failed: expected {expected_result_1}, got {result_1}"
        print(f"Test passed: {result_1}")

        test_case_2 = TreeNode(5)
        test_case_2.left = TreeNode(3)
        test_case_2.right = TreeNode(6)
        test_case_2.left.left = TreeNode(2)
        test_case_2.left.right = TreeNode(4)
        test_case_2.right.right = TreeNode(7)

        # Perform test and verify output
        expected_result_2 = [2, 3, 4, 5, 6]
        modified_root_2 = self.solution(test_case_2, 7)
        result_2 = inorder_traversal(modified_root_2)
        assert result_2 == expected_result_2, f"Test failed: expected {expected_result_2}, got {result_2}"
        print(f"Test passed: {result_2}")

    def __str__(self):
        return (
            f"Problem: Delete Node in a BST\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = DeleteNodeInBST()
print(solution)  # Display problem information
solution.test()  # Run tests
