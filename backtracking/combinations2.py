from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(pos, cur, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, target - candidates[i])
                cur.pop()

                prev = candidates[i]

        dfs(0, [], target)
        return res
  
print(Solution().combinationSum2([1,1,2], 2))

# Solution set must not contain duplicates.