from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DeleteMiddleNode(AbstractProblem):
    def __init__(self):
        super().__init__(
            problem = "Delete the Middle Node of a Linked List",
            difficulty = "medium",
            link = "https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/",
            instructions = (
                "You are given the head of a linked list. Delete the middle node, "
                "and return the head of the modified linked list."
            ),
            tags = ["Linked List", "Two Pointers"]
        )

    def solution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            # If the list is empty or has only one node, return None
            return None

        # Initialize slow and fast pointers
        slow, fast = head, head
        prev = None

        # Move fast pointer twice as fast as slow pointer
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        if prev:
            prev.next = slow.next

        return head

    def test(self):
        # Helper function to convert linked list to Python list for easy comparison
        def list_to_array(head: Optional[ListNode]) -> list[int]:
            array = []
            current = head
            while current:
                array.append(current.val)
                current = current.next
            return array

        # Test cases
        test_cases = [
            (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [1, 2, 4, 5]),
            (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [1, 2, 4]),
            (ListNode(1), []),
        ]

        for head, expected in test_cases:
            result = self.solution(head)
            result_array = list_to_array(result)
            assert result_array == expected, f"Test failed: expected {expected}, got {result_array}"
            print(f"Test passed: {result_array}")

    def __str__(self):
        return super().__str__()
