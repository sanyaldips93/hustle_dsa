class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        if not self.size:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            self.size -= 1
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node
        self.size += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if self.cap < self.size:
            left = self.left.next
            self.remove(left)
            del self.cache[left.key]


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
param_1 = obj.get(1)
obj.put(2,3)
obj.put(1,3)