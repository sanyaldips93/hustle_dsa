from collections import defaultdict
import math
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                idx = len(self.tweetMap[followee]) - 1
                cnt, tweetId = self.tweetMap[followee][idx]
                heap.append([cnt, tweetId, followee, idx - 1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            cnt, tweetId, userId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                cnt, tweetId = self.tweetMap[userId][idx]
                heapq.heappush(heap, [cnt, tweetId, userId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)