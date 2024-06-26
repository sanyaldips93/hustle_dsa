from typing import List


def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    ans = 0
    # XOR all the elements
    for i in range(n):
        ans = ans ^ arr[i]
    return ans

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        
        l, r = 1, n - 2
        while l <= r:
            m = (l + r) // 2
            if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
                return nums[m]
            # if the mid index is odd, meaning its actually even (zero idx) - then if the left value and mid value are same,
            # we should look at the other side (l = m +1), which is actually odd, and result could be there.
            # OR if the mid index is even (actually odd) and the right most value and mid value are same, then as well,
            # we should look at the right side of m (l = m +1), as the result could be there.
            if (m % 2 == 1 and nums[m] == nums[m-1]) or (m % 2 == 0 and nums[m] == nums[m+1]):
                l = m + 1
            else:
                r = m - 1

arr = [1, 1, 2, 3, 3, 5, 5, 6, 6]
ans = Solution().singleNonDuplicate(arr)
print("The single element is:", ans)