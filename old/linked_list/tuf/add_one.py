class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        cur = head
        
        # reverse current list
        newhead = self.reverse(cur)

        # add 1 to the head and cascade
        cur = self.add(newhead)
        
        # reverse the result list.
        res = self.reverse(cur)
        return res
    
    def reverse(self, head):
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
    def add(self, head):
        cur = head
        carry = 1
        prev = None
        while cur:
            val = cur.data + carry
            cur.data = val % 10
            carry = val // 10
            prev = cur
            cur = cur.next
        if carry:
            prev.next = Node(carry)
        return head
            