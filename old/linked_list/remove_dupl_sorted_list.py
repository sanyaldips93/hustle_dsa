# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        prev = dummy
        cur = head
        while cur:
            if cur.val == prev.val :
                prev.next = cur.next
            else :
                prev = cur
            cur = cur.next
        return dummy.next