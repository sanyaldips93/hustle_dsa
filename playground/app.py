from collections import deque
from typing import List


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.map:
            return res
        l, r = 0, len(self.map[key]) - 1
        res = self.map[key][l][0]
        while l < r:
            mid = (l + r) // 2
            val = self.map[key][mid][1]
            if val <= timestamp:
                res = self.map[key][mid][0]
                l = mid + 1
            else:
                r = mid
        return res


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("love","high",10)
obj.set("love","low",20)
param_2 = obj.get("love", 5)
print(param_2)
param_2 = obj.get("love", 10)
print(param_2)