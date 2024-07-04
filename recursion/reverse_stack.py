from typing import List

class Solution:
    def reverse(self,stack): 
        #code here
        if stack:
            last = stack.pop()
            self.reverse(stack)
            self.reverseStack(last, stack)
        
    def reverseStack(self, last, stack):
        if not stack:
            stack.append(last)
        else:
            ele = stack.pop()
            self.reverseStack(last, stack)
            stack.append(ele)
    
print(Solution().reverse([1,2]))