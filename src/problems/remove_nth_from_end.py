from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class RemoveNthFromEnd(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Remove Nth Node From End of List",
            difficulty = "Medium",
            link = "https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/",
            instructions = (
                "Given the head of a linked list, remove the nth node from the end of the list and return its head.\n"
                "Try to do this in one pass using two pointers."
            ),
            tags = ["Linked List"]
        )

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
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Helper function to convert the list to a Python list
        def list_to_array(node: Optional[ListNode]) -> list:
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        # Test case 1
        self.total_tests += 1
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        n = 2
        expected = [1, 2, 3, 5]
        result = list_to_array(self.solution(head, n))
        if result == expected:
            self.tests_passed += 1

        # Test case 2: Remove the head node
        self.total_tests += 1
        head = ListNode(1)
        head.next = ListNode(2)

        n = 2
        expected = [2]
        result = list_to_array(self.solution(head, n))
        if result == expected:
            self.tests_passed += 1

        # Test case 3: Single element list
        self.total_tests += 1
        head = ListNode(1)

        n = 1
        expected = []
        result = list_to_array(self.solution(head, n))
        if result == expected:
            self.tests_passed += 1


