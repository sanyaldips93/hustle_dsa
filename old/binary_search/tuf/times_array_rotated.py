class Solution:
    def findKRotation(self,arr):
        l, r = 0, len(arr) - 1
        res = float("infinity")
        idx = 0
        while l <= r:
            if arr[l] <= arr[r]:
                if arr[l] <= res:
                    res = arr[l]
                    idx = l
                break
            m = (l + r) // 2
            if arr[m] <= res:
                  res = arr[m]
                  idx = m
            if arr[m] >= arr[l]:
                l = m + 1
            else:
                r = m - 1
        return idx

print(Solution().findKRotation([66, 67, 7, 10, 14, 19, 27, 33, 36, 40, 44, 54, 60]))