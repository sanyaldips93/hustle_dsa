class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        arr = [[val[i], wt[i]] for i in range(len(val))]
        arr.sort(key=lambda x: x[0]/x[1], reverse=True)
        curVal = 0
        for i in range(len(arr)):
            if arr[i][1] <= capacity:
                capacity -= arr[i][1]
                curVal += arr[i][0]
            else:
                curVal += (arr[i][0] // arr[i][1]) * capacity
                break

        return curVal
  
print(Solution().fractionalknapsack([60,100,120], [10,20,30], 50))