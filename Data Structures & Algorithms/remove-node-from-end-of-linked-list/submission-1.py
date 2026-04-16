# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if length == 1:
            return None
        nFront = length - n
        if nFront == 0:
            return head.next
        
        cur = head
        count = 0
        while cur:
            tmp = cur.next
            if count == nFront - 1:
                cur.next = cur.next.next
            count += 1
            cur = tmp
        return head
        