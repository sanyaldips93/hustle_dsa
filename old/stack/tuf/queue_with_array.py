class MyQueue:
    
    def __init__(self):
        self.arr=[]
        self.left = 0
        self.right = 0
    
    #Function to push an element x in a queue.
    def push(self, x):
         self.arr.append(x)
         self.right += 1
     
    #Function to pop an element from queue and return that element.
    def pop(self):
        if self.left == self.right:
            return -1
        temp = self.left
        self.left += 1
        return self.arr[temp]