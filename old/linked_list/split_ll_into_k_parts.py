# Definition for singly-linked list.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, cur = 0, head
        while cur:
            cur = cur.next
            length += 1
        cur = head
        base, rem = length // k, length % k
        # base determines what the equal list partition will be and remainder 
        # defines what more values needs to be fit in the first few lists.
        # for ex if the list was 1->2->3->4->5 and k was 3 -- base would be 2, and rem would be 1
        # res would be [[1,2,3],[4,5]]
        res = []
        for i in range(k):
            res.append(cur)
            for j in range(base - 1 + (1 if rem else 0)):
                if not cur: break
                cur = cur.next
            rem -= (1 if rem else 0)
            if cur:
                tmp = cur.next
                cur.next = None
                cur = tmp
        return res
