class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l1, l2 = 0, 0
        while l1 < len(word1) and l2 < len(word2):
            res.append(word1[l1])
            res.append(word2[l2])
            l1 += 1
            l2 += 1
        
        if l1 < len(word1):
            res.append(word1[l1:len(word1)])
        if l2 < len(word2):
            res.append(word2[l2:len(word2)])
        
        return "".join(res)
  
print(Solution().mergeAlternately('abc', 'defgh'));