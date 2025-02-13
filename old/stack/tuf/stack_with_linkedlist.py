class StackNode: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None


class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    def __init__(self):
        self.head = None
        
    #Function to push an integer into the stack.
    def push(self, data):
        node = StackNode(data)
        node.next = self.head
        self.head = node
        

    #Function to remove an item from top of the stack.
    def pop(self):
        if self.head:
            next = self.head.next
            self.head.next = None
            cur = self.head.data
            self.head = next
            return cur
        else:
            return -1