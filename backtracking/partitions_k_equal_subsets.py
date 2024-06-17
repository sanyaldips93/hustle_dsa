from typing import List
from datetime import datetime

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        reqSum = total // k
        subSets = [0] * k
        nums.sort(reverse = True)

        def recurse(i):
            if i == len(nums):    
                return True

            for j in range(k):
                if subSets[j] + nums[i] <= reqSum:
                    subSets[j] += nums[i]

                    if recurse(i + 1):
                        return True

                    subSets[j] -= nums[i]

                    # Important line, otherwise function will give TLE
                    if subSets[j] == 0:
                        break

                    """
                    Explanation:
                    If subSets[j] = 0, it means this is the first time adding values to that subset.
                    If the backtrack search fails when adding the values to subSets[j] and subSets[j] remains 0, it will also fail for all subSets from subSets[j+1:].
                    Because we are simply going through the previous recursive tree again for a different j+1 position.
                    So we can effectively break from the for loop or directly return False.
                    """

            return False

        return recurse(0)
    # print(Solution().canPartitionKSubsets([9,6,1,8,4,3,4,1,7,3,7,4,5,3,2,3], 10))
    '''
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        visit = [False] * len(nums)
        target = sum(nums) / k

        if sum(nums) % k:
            return False
        
        nums.sort(reverse=True)

        def bt(i, k, cur):
            if k == 0:
                return True
            if cur == target:
                return bt(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if visit[j] or cur + nums[j] > target:
                    continue
                visit[j] = True
                if bt(j+1, k, cur + nums[j]): return True
                visit[j] = False
            return False
        
        return bt(0, k, 0)
    '''
print(Solution().canPartitionKSubsets([9,6,1,8,4,3,4,1,7,3,7,4,5,3,2,3], 10))
