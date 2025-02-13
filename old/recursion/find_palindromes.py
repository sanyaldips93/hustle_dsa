# Find all possible palindromes of a given string

class Solution:
  def getAllPalindroms(self, string):
    res = []
    arr = []
    visit = set()
    for ch in string:
      arr.append(ch)
    # get all permutations
    permutations = (self.getAllPermutations(arr))
    # check if each permutation is a palindrome
    for permuation in permutations:
      permuation = "".join(permuation)
      if permuation in visit:
         continue
      visit.add(permuation)
      if self.checkPalindrome(permuation):
        res.append(permuation)
    # return res
    return res
  
  def checkPalindrome(self, string):
    l, r = 0, len(string) - 1
    while l <= r:
      if string[l] != string[r]:
        return False
      l += 1
      r -= 1
    return True
  
  def getAllPermutations(self, nums):
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.getAllPermutations(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
  
print(Solution().getAllPalindroms("aabb"))
# print(Solution().getAllPermutations([1,2]))
      