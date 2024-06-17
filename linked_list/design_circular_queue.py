class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, self.left, None)
        self.left.next = self.right
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        node = ListNode(value, None, None)
        tmp = self.right.prev
        self.right.prev, tmp.next = node, node
        node.next, node.prev = self.right, tmp
        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        tmp = self.left.next
        self.left.next, tmp.next.prev = tmp.next, self.left
        self.space += 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.space == 0:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()