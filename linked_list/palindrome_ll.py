# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # reach the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second node
        prev = None
        cur = slow
        while(cur != None):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # check for palindrome
        left, right = head, prev
        while(right != None):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
    
a = ListNode(1, None)
b = ListNode(2, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)

print(Solution().isPalindrome(e))