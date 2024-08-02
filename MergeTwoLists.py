from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
    
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

solution = Solution()
result = solution.mergeTwoLists(list1, list2)
current = result

print()
while current is not None:
    print(current.val, end=" ")
    current = current.next
