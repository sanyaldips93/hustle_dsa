class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        arr = []
        for i in range(len(val)):
            arr.append([val[i], wt[i]])
        arr.sort(key = lambda x: x[0]/x[1], reverse=True)
        res = 0
        for val,wt in arr:
            amount = val / wt
            if wt <= capacity:
                capacity -= wt
                res += val
            else:
                new_cap = amount * capacity
                res += new_cap
                break
        return res
  
print(Solution().fractionalknapsack([60,100,120], [10,20,30], 50))