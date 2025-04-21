
# Considering negative values and each subset array can be of any size.
class Solution:
    def minimumDifference(self, arr):
        n = len(arr)
        min_sum = sum(x for x in arr if x < 0)
        max_sum = sum(x for x in arr if x > 0)
        offset = -min_sum
        range_size = max_sum - min_sum + 1
        
        dp = [[False] * range_size for _ in range(n)]
        dp[0][arr[0] + offset] = True
        dp[0][offset] = True  # zero sum is always possible by picking nothing

        for i in range(1, n):
            for s in range(range_size):
                # don't pick current item
                not_pick = dp[i-1][s]
                
                # pick current item if valid
                pick = False
                new_sum = s - arr[i]  # reverse the shift
                if 0 <= new_sum < range_size:
                    pick = dp[i-1][new_sum]
                
                dp[i][s] = pick or not_pick

        total = sum(arr)
        min_diff = float('inf')
        for s in range(range_size):
            if dp[n-1][s]:
                subset_sum = s - offset
                other_sum = total - subset_sum
                min_diff = min(min_diff, abs(subset_sum - other_sum))
        return min_diff
