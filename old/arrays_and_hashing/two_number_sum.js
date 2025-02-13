var twoSum = function(nums, target) {
  const hash = {}; // initialising the hash.
  for(const idx in nums) { // picking up the index
      const element = nums[idx]; // finding the element in the index
      const targetElement = target - element; // getting the other element that makes up the target
      if(hash[targetElement]) { // finding if the other element already exists
          return [hash[targetElement], idx]; // if it does, return the index of both the eleemnts
      } else {
          hash[element] = idx; // store the index of the element in the loop in hash
      }
  }
};