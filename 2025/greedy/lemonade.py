from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        map = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                map[5] += 1
            elif bill == 10:
                if map[5] < 1:
                    return False
                map[5] -= 1
                map[10] += 1
            else:
                if map[10] >= 1 and map[5] >= 1:
                    map[10] -= 1
                    map[5] -= 1
                elif map[5] >= 3:
                    map[5] -= 3
                else:
                    return False
        return True 