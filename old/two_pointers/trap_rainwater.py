from typing import List


class Solution:
    
    # using 1 loop and no memory
    def trap(self, height: List[int]) -> int:
        lmax, rmax = height[0], height[-1]
        output = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                trap = lmax - height[l]
                output += trap if trap > 0 else 0 
                l += 1
            else:
                rmax = max(rmax, height[r])
                trap = rmax - height[r]
                output += trap if trap > 0 else 0 
                r -= 1
        return output
    

    # using 2 loops and memory
    def trap2(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        lmax, rmax = height[0], height[-1]
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            left[i] = lmax
            revidx = len(height) - i - 1
            rmax = max(rmax, height[revidx])
            right[revidx] = rmax
        
        output = 0
        for i in range(len(height)):
            trap = min(left[i], right[i]) - height[i]
            output += trap if trap > 0 else 0
        return output