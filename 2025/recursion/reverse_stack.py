from typing import List


class Solution:
  def reverseStack(self, stack: List[int]):
    if stack:
      temp = stack.pop()
      self.reverseStack(stack)
      self.insertAtBottom(stack, temp)
    return stack

  def insertAtBottom(self, stack: List[int], num):
    if not stack:
      stack.append(num)
    else:
      temp = stack.pop()
      self.insertAtBottom(stack, num)
      stack.append(temp)

print(Solution().reverseStack([1,2,3,4]))