function bubbleSort(nums) {
  while(true) {
    let flag = false;
    for(let i=0; i<nums.length-1; i++) {
      if(nums[i] > nums[i+1]) {
        flag = true;
        let tmp = nums[i];
        nums[i] = nums[i+1];
        nums[i+1] = tmp;
      }
    }
    if(!flag) break;
  }
  return nums;
}

console.log(bubbleSort([3,6,2,1,8,4]));