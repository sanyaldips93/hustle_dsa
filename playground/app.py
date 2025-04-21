from collections import defaultdict, deque
from typing import List

# Play with your code
from typing import List
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        for tar in range(amount+1):
            if tar % coins[0] == 0:
                dp[tar] = tar // coins[0]
        for r in range(1,n):
            for tar in range(coins[r], amount+1):
                dp[r][tar] = dp[r][tar] + dp[r][tar-coins[r]]
        return dp[n-1][amount]

print(Solution().coinChange([1,2,5],11))