from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l, res, total = 0, 0, 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1
            while len(count) > 2:
                fruit = fruits[l]
                total -= 1
                count[fruit] -= 1
                l += 1
                if count[fruit] == 0:
                    count.pop(fruit)
            res = max(res, total)
        return res