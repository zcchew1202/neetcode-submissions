# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        carry = 0
        cur = dummyNode
        while l1 or l2 or carry:
            # in case carry is not 0 but l1/l2 is null
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            res = v1 + v2 + carry
            carry = res // 10
            res %= 10
            
            cur.next = ListNode(res)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyNode.next
            