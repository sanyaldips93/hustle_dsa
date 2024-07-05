class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None

class Solution:
    def reverseDLL(self, head):
        dummy = Node(0)
        dummy.next = head
        curr = head
        
        pre = curr.prev
        nex = curr.next
        
        while curr:
            curr.next = pre
            curr.prev = nex
            pre = curr
            curr = nex
            nex = curr.next if curr else None
        
        tail = dummy.next
        tail.next = None
        
        return pre