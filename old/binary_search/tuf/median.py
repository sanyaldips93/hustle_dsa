from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            mid = half - m - 2
            AL = A[m] if m >= 0 else float("-infinity")
            AR = A[m+1] if m + 1 < len(A) else float("infinity")
            BL = B[mid] if mid >= 0 else float("-infinity")
            BR = B[mid+1] if mid+1 < len(B) else float("infinity")

            if AL > BR:
                r = m - 1
            elif BL > AR:
                l = m + 1
            elif AL <= BR and BL <= AR:
                if total % 2 == 0:
                    return (max(AL, BL) + min(AR, BR)) / 2
                else:
                    return min(AR, BR)
            
print(Solution().findMedianSortedArrays([1,3], [2]))