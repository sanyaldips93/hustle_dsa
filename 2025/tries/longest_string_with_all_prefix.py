class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = Node()
        
    def longestValidWord(self, words):
        for word in words:
            cur = self.root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = Node()
                cur = cur.children[ch]
            cur.end = True
    
        res = ""
        for word in words:
            cur = self.root
            for ch in word:
                child = cur.children[ch]
                if child.end == False: break
                cur = child
            else:
                if len(res) < len(word) or (len(word) == len(res) and word < res):
                    res = word
        
        return res
        

print(Solution().longestValidWord(["p", "pr", "pro", "prob", "problem", "pros", "process", "processor"]))