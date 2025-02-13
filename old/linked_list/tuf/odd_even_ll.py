# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        i = 0
        cur = head
        l, r = ListNode(0), ListNode(0)
        odd, even = l, r
        while cur:
            if i % 2 == 0:
                odd.next = cur
                odd = cur
            else:
                even.next = cur
                even = cur
            cur = cur.next
            i += 1
        # print(odd.val, even.val, l.next.val, r.next.val)
        even.next = None
        odd.next = r.next
        return l.next