from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        def get2nodes(node):
            k = 0
            while node != None and k < 2:
                node = node.next
                k += 1
            return node

        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while(True):
            kth = get2nodes(groupPrev)
            if kth == None:
                break
            prev = kth.next
            groupNext = kth.next
            cur = groupPrev.next
            while(cur != groupNext):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp

        return dummy.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

result = Solution().swapPairs(node)
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")