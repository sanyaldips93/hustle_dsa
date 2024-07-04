def findLargestMinDistance(self, boards:list, k:int):
    l, r = max(boards), sum(boards)
    while l <= r:
        m = (l + r) // 2
        partitions = self.canSplit(m, boards)
        if partitions > k:
            l = m + 1
        else:
            r = m - 1
    return l

def canSplit(self, maxi, nums):
    splits = 1
    cursum = 0
    for num in nums:
        if cursum + num <= maxi:
            cursum += num
        else:
            splits += 1
            cursum = num
    return splits