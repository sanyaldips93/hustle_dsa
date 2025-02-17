from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash = {}
        for i in range(len(order)):
            char = order[i]
            hash[char] = i
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if hash[w1[j]] > hash[w2[j]]:
                        return False
                    break
        return True
    
print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))