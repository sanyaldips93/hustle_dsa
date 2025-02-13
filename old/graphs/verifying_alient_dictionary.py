from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash = { c:i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w2[j] != w1[j]:
                    if hash[w2[j]] <= hash[w1[j]]:
                        return False
                    break
        return True
    
'''
There are two conditions at play here : 
1. If the alphabetical ordering do not match, we need to return true or false basis the ordering.
2. If the length of the second chosen word is less than length of first word, return false.

Another point, we choose 2 words at a time
'''