import cProfile

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if not s:
            return
        topElement = s[-1]
        s.pop()
        self.Sorted(s)
        self.findPlaceToInsert(topElement, s)
        return s
    
    def findPlaceToInsert(self, top, stack):
        if not stack or top >= stack[-1]:
            stack.append(top)
            return
        
        current = stack.pop()
        self.findPlaceToInsert(top, stack)
        stack.append(current)
        return


cProfile.run('Solution().Sorted([11,3,4,55,22])')
print(Solution().Sorted([11,3,4,55,22]))