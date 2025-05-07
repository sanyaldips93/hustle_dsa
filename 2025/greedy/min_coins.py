class Solution:
    def minPartition(self, N):
        coins = [2000,500,200,100,50,20,10,5,2,1]
        target = N
        res = []
        for i in coins:
            if i > target:
                continue
            while i <= target:
                target -= i
                res.append(i)
            if target == 0:
                break
        return res


print(Solution().minPartition(43))