/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
  for(let i = 0; i < nums.length; i++) {
      for(let j = i+1; j < nums.length; j++) {
          if(nums[i] === nums[j] && (j-i) <= k) return true 
      }
  }
  return false;
};

// Python Solution
/**
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for K in range(len(nums)):
            if K - L > k:
                window.remove(nums[L])
                L += 1
            if nums[K] in window:
                return True
            window.add(nums[K])
        return False

 */