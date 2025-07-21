from collections import deque, defaultdict
from typing import List

# https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visit = set()
        q = deque()
        q.append(id)
        visit.add(id)
        count = defaultdict(int)

        while q and level:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in friends[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            level -= 1
        
        while q:
            node = q.popleft()
            for video in watchedVideos[node]:
                count[video] += 1
        
        return sorted(count, key=lambda x: (count[x], x))

print(Solution().watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 1))