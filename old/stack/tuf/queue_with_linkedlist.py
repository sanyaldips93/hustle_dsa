# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self): 
        self.head = None
        self.tail = None
    
    #Function to push an element into the queue.
    def push(self, item): 
        node = Node(item)
        if not self.head:
             self.head = node
             self.tail = node
        else:
            prev = self.tail
            self.tail.next = node
            self.tail = node
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.head:
            cur = self.head
            self.head = self.head.next
            return cur.data
        else:
            return -1