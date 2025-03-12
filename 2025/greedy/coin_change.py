from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount
        res = 0
        coins.sort()
        for i in range(len(coins)-1, -1, -1):
            while amount >= coins[i]:
                amount -= coins[i]
                res += 1
        if i == 0 and amount != 0:
            return -1
        return res if res > 0 else -1
    
print(Solution().coinChange([186,419,83,408], 6249))