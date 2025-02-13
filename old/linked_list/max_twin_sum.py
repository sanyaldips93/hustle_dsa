# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        maxVal = 0
        left = head
        right = prev
        while right:
            sum = left.val + right.val
            maxVal = max(maxVal, sum)
            left = left.next
            right = right.next
        return maxVal
    
node = ListNode(5)
node.next = ListNode(2)
node.next.next = ListNode(6)
node.next.next.next = ListNode(4)

result = Solution().pairSum(node)
print(result)