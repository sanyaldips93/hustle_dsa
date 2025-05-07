from typing import List


class Solution:
    def candy(self, arr: List[int]) -> int:
        n = len(arr)
        res = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i-1]: res[i] = res[i-1] + 1
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]: res[i] = max(res[i], res[i+1] + 1)
        return sum(res)