from collections import deque, defaultdict
from typing import List, Tuple
class Solution:
    def findOrder(self, words):
        chars = set()
        for word in words:
            for ch in word:
                chars.add(ch)
        numberofchars = len(chars)
        
        adj = {i:[] for i in range(numberofchars)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            wordmin = min(len(word1), len(word2))
            equalcheck = 0
            for i in range(wordmin):
                if word1[i] != word2[i]:
                    adj[ord(word1[i]) - ord('a')].append(ord(word2[i]) - ord('a'))
                    break
                else:
                    equalcheck += 1
            if equalcheck == wordmin and len(word1) > len(word2):
                return ""
        
        indegree = [0] * numberofchars
        for i in range(len(adj)):
            for nei in adj[i]:
                indegree[nei] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(topo) != numberofchars:
            return ""
        
        for i in range(len(topo)):
            topo[i] = chr(topo[i] + ord('a'))
        
        return "".join(topo)



print(Solution().findOrder(["baa", "abcd", "abca", "cab", "cada"]))