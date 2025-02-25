from collections import deque
class Solution:
    def findOrder(words):
        # create a set of chars
        chars = set()
        for word in words:
            for ch in word:
                chars.add(ch)
        # create adjacency matrix from words
        adj = {ch:[] for ch in chars}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minlen = min(len(word1), len(word2))
            if word1[:minlen] == word2[:minlen] and len(word1) > len(word2):
                return ""
            for i in range(minlen):
                if word1[i] != word2[i]:
                    adj[word1[i]].append(word2[i])
                    break
        
        #create indegree
        indegree = {}
        for ch in chars:
            indegree[ch] = 0
        for key in adj:
            for ch in adj[key]:
                indegree[ch] += 1
        # create queue and attach indegree = 0
        q = deque()
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        #run kahn's algo to find the safe list
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "" if len(topo) != len(chars) else "".join(topo)