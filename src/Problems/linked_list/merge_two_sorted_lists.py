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
            difficulty = "easy",
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
        # Helper function to print the list
        def print_list(node: Optional[ListNode]):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        # Test cases
        # Test case 1
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(4)

        list2 = ListNode(1)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)

        expected = [1, 1, 2, 3, 4, 4]
        result = print_list(self.solution(list1, list2))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Test passed for test case 1: {result}")

        # Test case 2: One list is empty
        list1 = None
        list2 = ListNode(0)

        expected = [0]
        result = print_list(self.solution(list1, list2))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Test passed for test case 2: {result}")

        # Test case 3: Both lists are empty
        list1 = None
        list2 = None

        expected = []
        result = print_list(self.solution(list1, list2))
        assert result == expected, f"Test failed: expected {expected}, got {result}"
        print(f"Test passed for test case 3: {result}")

    def __str__(self):
        return super().__str__()
