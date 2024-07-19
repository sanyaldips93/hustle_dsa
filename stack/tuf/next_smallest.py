class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
          stack = [A[0]]
          res = [-1] * len(A)
          for i in range(1,len(A)):
              num = A[i]
              if stack and stack[-1] < num:
                  res[i] = stack[-1]
              elif stack and stack[-1] > num:
                  stack.append(num)
          return res
    
print(Solution().prevSmaller([4, 5, 2, 10, 8]))