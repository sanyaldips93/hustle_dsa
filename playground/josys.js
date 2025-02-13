/**
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
[-1, -1, 0, 1, 2, 4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 */

function threeSum(arr) {
  arr.sort();
  const res = [];
  const cur = [];
  kSum(0, 3, 0);
  function kSum(start, k, target) {
    if(k!=2) {
      for(let i = start; i <arr.length; i++) {
        if(i > start && arr[i] === arr[i-1]) {
          continue;
        }
        cur.push(arr[i]);
        kSum(i+1, k-1, target-arr[i]);
        cur.pop();
      }
    } else {
      let l = start;
      let r = arr.length - 1;
      while(l < r) {
        if (arr[l] + arr[r] < target) {
          l += 1;
        } else if (arr[l] + arr[r] > target){
          r -= 1;
        } else {
          res.push([...cur, arr[l], arr[r]]);
          l += 1;
          while (l < r && arr[l] === arr[l+1]) {
            l += 1;
          }
        }
      }
    }
  }
  return res;
}

console.log(threeSum([0,0,0]));