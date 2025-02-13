class Solution:
    def numTrees(self, n):
      numTree = [1] * (n + 1)
      m = []
      for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
          left = root - 1
          right = nodes - root
          m.append([left, right])
          total += numTree[left] * numTree[right]
        numTree[nodes] = total
      print(m)
      return numTree


print(Solution().numTrees(4))

# classic DP problem
# if n = 4, the sub-problems are:
# numt[0] * numt[3] +
# numt[1] * numt[2] +
# numt[2] * numt[1] +
# numt[3] * numt[0]
# we need to iteratively solve for these, and we will get the answer of numt[3]