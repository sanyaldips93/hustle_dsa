
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

        total = sum(arr)  # Step 1: total sum of array
        min_diff = float('inf')  # Step 2: initialize minimum difference to large value

        # Step 3: Explore all possible subset sums
        for s in range(range_size):
            if dp[n-1][s]:  # if it's possible to form a subset with sum (s - offset)
                subset_sum = s - offset  # recover actual subset sum (undo the shift)
                other_sum = total - subset_sum  # remaining elements' sum
                min_diff = min(min_diff, abs(subset_sum - other_sum))  # update minimum difference

        return min_diff  # Step 4: return the best (smallest) difference found

