from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numNodes = 0
        cur = head
        
        # Count the number of nodes in the linked list
        while cur:
            numNodes += 1
            cur = cur.next
        
        # If head is only node, remove it 
        if numNodes == 1:
            head = None

        # calculate the middle node and remove it
        middle = numNodes // 2
        cur = head
        count = 1
        while cur:
            if count == middle:
                if cur.next:
                    cur.next = cur.next.next
            count += 1
            cur = cur.next

        return head

nums = ListNode(1)
nums.next = ListNode(2)
nums.next.next = ListNode(4)

solution = Solution()
result = solution.deleteMiddle(nums)
current = result

print()
while current is not None:
    print(current.val, end=" ")
    current = current.next