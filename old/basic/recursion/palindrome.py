class Solution:
  def palindrome(self, string):
    def check(string, s, e):
      if s <= e:
        if s == e:
          return True
        else:
          if string[s] != string[e]:
            return False
          return check(string, s+1, e-1) and True
    return check(string, 0, len(string) - 1)

print(Solution().palindrome("sames"))