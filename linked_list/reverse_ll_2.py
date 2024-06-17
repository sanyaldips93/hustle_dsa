# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev = cur
            cur = cur.next

        prev = None
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next
    
# 1 -> 2 -> 3 -> 4 -> 5 ( LL )
# 2, 4 (left, right)
# 1 -> 2; leftPrev = 1, cur = 2 (after first loop)
# 4 -> 3 -> 2; prev = 4 cur = 5 (after 2nd loop)
# leftPrev.next.next = 2.next = 5 
# leftPrev.next = 1.next = 4
# 1 -> 4 -> 3 -> 2 -> 5

        
        

        


                