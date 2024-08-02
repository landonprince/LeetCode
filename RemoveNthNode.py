from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
    
nums = ListNode(4)
nums.next = ListNode(2)
nums.next.next = ListNode(9)
nums.next.next.next = ListNode(6)
n = 2

solution = Solution()
result = solution.removeNthFromEnd(nums, n)
current = result

print()
while current is not None:
    print(current.val, end=" ")
    current = current.next
