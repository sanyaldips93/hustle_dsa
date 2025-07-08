class Solution:
  def getUniqueKeys(self, s):
    keys = set()
    def recurse(s):
      if isinstance(s, list):
        for i in range(len(s)):
          recurse(s[i])
      elif isinstance(s, dict):
        for key, value in s.items():
          keys.add(key)
          recurse(value)
    recurse(s)
    res = []
    if keys:
      for item in keys:
        res.append(item)
    return res

data = [{"c": [{"d": 5,}]},"5",{"f": 7},{"e": {"c": [9, { "d": 9 }]}, "f": 5}]
print(Solution().getUniqueKeys(data))