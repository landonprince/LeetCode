from typing import Optional
from problems.abstract_problem import AbstractProblem

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoSortedLists(AbstractProblem):
    def __init__(self):
        super().__init__(
            name = "Merge Two Sorted Lists",
            difficulty = "Easy",
            link = "https://leetcode.com/problems/merge-two-sorted-lists/description/",
            instructions = (
                "Merge two sorted linked lists and return it as a sorted list. "
                "The list should be made by splicing together the nodes of the first two lists."
            ),
            tags = ["Linked List"]
        )

    def solution(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to help simplify the merging process
        dummy = ListNode(-1)
        # This pointer will help build the new merged list
        current = dummy

        # Traverse both lists
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining elements from the non-empty list
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        # Return the merged list, which is the next node of the dummy
        return dummy.next

    def test(self):
        # Reset test counters
        self.tests_passed = 0
        self.total_tests = 0

        # Helper function to convert the list to a Python list
        def list_to_array(node: Optional[ListNode]):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        # Test case 1
        self.total_tests += 1
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(4)

        list2 = ListNode(1)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)

        expected = [1, 1, 2, 3, 4, 4]
        result = list_to_array(self.solution(list1, list2))
        if result == expected:
            self.tests_passed += 1

        # Test case 2: One list is empty
        self.total_tests += 1
        list1 = None
        list2 = ListNode(0)

        expected = [0]
        result = list_to_array(self.solution(list1, list2))
        if result == expected:
            self.tests_passed += 1

        # Test case 3: Both lists are empty
        self.total_tests += 1
        list1 = None
        list2 = None

        expected = []
        result = list_to_array(self.solution(list1, list2))
        if result == expected:
            self.tests_passed += 1

