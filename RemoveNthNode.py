from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class RemoveNthFromEnd:
    def __init__(self):
        self.difficulty = "medium"
        self.link = "https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/"
        self.instructions = (
            "Given the head of a linked list, remove the nth node from the end of the list and return its head.\n"
            "Try to do this in one pass using two pointers."
        )
        self.tags = ["Linked List"]

    def solution(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0

        # Find the length of the linked list
        while cur:
            length += 1
            cur = cur.next
        
        indexDelete = length - n
        count = 1
        cur = head

        # If the node to be deleted is the head, update the head pointer
        if indexDelete == 0:
            head = head.next

        # Traverse the linked list and delete the node at the given index
        while cur:
            if count == indexDelete:
                cur.next = cur.next.next
            count += 1
            cur = cur.next

        return head
    
    def test(self):
        # Helper function to print the list
        def print_list(node: Optional[ListNode]) -> list:
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        # Test cases
        # Test case 1
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        n = 2
        expected = [1, 2, 3, 5]
        result = print_list(self.solution(head, n))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Test passed for test case 1: {result}")

        # Test case 2: Remove the head node
        head = ListNode(1)
        head.next = ListNode(2)

        n = 2
        expected = [2]
        result = print_list(self.solution(head, n))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Test passed for test case 2: {result}")

        # Test case 3: Single element list
        head = ListNode(1)

        n = 1
        expected = []
        result = print_list(self.solution(head, n))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Test passed for test case 3: {result}")

    def __str__(self):
        return (
            f"Problem: Remove Nth Node From End of List\nDifficulty: {self.difficulty}\nLink: {self.link}\n"
            f"Instructions: {self.instructions}\nTags: {', '.join(self.tags)}"
        )

# Create an instance of the problem
solution = RemoveNthFromEnd()
print(solution)  # Display problem information
solution.test()  # Run tests
