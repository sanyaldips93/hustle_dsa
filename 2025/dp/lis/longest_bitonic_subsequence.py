from typing import List


def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    dp1 = [1] * n
    dp2 = [1] * n

    for i in range(1,n):
        for prev in range(i):
            if arr[prev] < arr[i] and 1+dp1[prev] > dp1[i]:
                dp1[i] = 1+dp1[prev]
    
    for i in range(n-2,-1,-1):
        for prev in range(n-1,i,-1):
            if arr[prev] < arr[i] and 1+dp2[prev] > dp2[i]:
                dp2[i] = 1+dp2[prev]
    
    maxi = 0
    for i in range(n):
        maxi = max(maxi, dp1[i]+dp2[i]-1)
    
    return maxi