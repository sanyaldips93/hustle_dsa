# https://www.geeksforgeeks.org/generate-binary-strings-without-consecutive-1s/?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=generate-binary-strings-without-consecutive-1s


class Solution:
  def genBinaryStrings(self, n):
    res = []
    def dfs(i, tmp):
      if i == n or len(tmp) == n:
        return res.append("".join(tmp))
      
      if len(tmp) > n:
        return

      if tmp[-1] == "1":
        tmp.append("0")
        dfs(i+1, tmp)
        tmp.pop()
      
      if tmp[-1] == "0":
        tmp.append("1")
        dfs(i+1, tmp)
        tmp.pop()
        tmp.append("0")
        dfs(i+1, tmp)
        tmp.pop()
    
    dfs(1, ["1"])
    dfs(1, ["0"])
    return res

print(Solution().genBinaryStrings(3))