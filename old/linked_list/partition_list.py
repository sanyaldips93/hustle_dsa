from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        leftdum, rightdum = ListNode(0), ListNode(0)
        left, right = leftdum, rightdum
        root = head
        while root:
            if root.val < x:
                left.next = ListNode(root.val)
                left = left.next
            else:
                right.next = ListNode(root.val)
                right = right.next
            root = root.next
        left.next = rightdum.next
        return leftdum.next
        
arr = [1,4,3,2,5,2]
dummy = ListNode(arr[0])
node = dummy
for i in range(1, len(arr)):
    node.next = ListNode(arr[i])
    node = node.next

sol = Solution().partition(dummy, 2);
    