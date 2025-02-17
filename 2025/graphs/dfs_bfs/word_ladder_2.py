from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        
        visit = set([beginWord])
        level_visit = set()
        q = deque([(beginWord, [beginWord])])
        res = []

        while q:
            for i in range(len(q)):
                [word, cur] = q.popleft()
                if word == endWord:
                    res.append(cur)
                else:
                    for j in range(len(word)):
                        pattern = word[:j] + "*" + word[j+1:]
                        for item in nei[pattern]:
                            if item not in visit:
                                level_visit.add(item)
                                q.append((item, cur + [item]))
            visit.update(level_visit)
        return res
    
# This will hit Memory Limit Exceeded as in worst case, BFS short paths can grow to exponenial limit