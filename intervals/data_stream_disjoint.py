from typing import List
from sortedcontainers import SortedDict # type: ignore

# Solution 1
class SummaryRanges:

    def __init__(self):
        self.treemap = SortedDict()

    def addNum(self, value: int) -> None:
        self.treemap[value] = True

    def getIntervals(self) -> List[List[int]]:
        res = []
        for n in self.treemap:
            if res and res[-1][1] + 1 == n:
                res[-1][1] = n
            else:
                res.append([n, n])
        return res

# Solution 2
class SummaryRanges:

    def __init__(self):
        self.set = set()

    def addNum(self, value: int) -> None:
        self.set.add(value)

    def getIntervals(self) -> List[List[int]]:
        arr = sorted(list(self.set))
        res = []
        for n in arr:
            if res and res[-1][1] + 1 == n:
                res[-1][1] = n
            else:
                res.append([n, n])
        return res



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()