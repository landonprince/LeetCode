from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class ReverseLinkedList(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Reverse Linked List",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/reverse-linked-list/",
            instructions = (
                "Given the head of a singly linked list, "
                "reverse the list, and return the reversed list."
            ),
            tags = ["Linked List", "Two Pointers"]
        )
        
    def solution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous and current nodes as None
        prev = None
        cur = head
        
        while cur is not None:
            # Store the next node before updating the current node's next pointer
            next = cur.next
            cur.next = prev
            
            # Move to the next node
            prev = cur
            cur = next
            
        return prev
    
    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

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
            (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [5, 4, 3, 2, 1]),
            (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [4, 3, 2, 1]),
            (ListNode(1), [1]),
        ]

        # Run each test case
        for head, expected in test_cases:
            self.total_tests += 1
            result = self.solution(head)
            result_array = list_to_array(result)
            if result_array == expected:
                self.tests_passed += 1
        
