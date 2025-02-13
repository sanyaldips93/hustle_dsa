from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            result = limit - people[r]
            r -= 1
            res += 1
            if l <= r and result >= people[l]:
                l += 1
        return res