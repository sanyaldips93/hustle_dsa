function insertionSort(nums) {
  for(let i=1;i<nums.length;i++) {
    let j=i;
    while(j>0 && nums[j-1]>nums[j]) {
      let tmp = nums[j-1];
      nums[j-1] = nums[j];
      nums[j] = tmp;
      j--;
    }
  }
  return nums;
}

console.log(insertionSort([3,1,5,8,2,6]));