var findMedianSortedArrays = function(nums1, nums2) {
  let A = nums1;
  let B = nums2;
  if(nums1.length < nums2.length) {
      let C = A;
      A = B;
      B = C;
  }
  let total = A.length + B.length;
  let half = Math.floor(total/2);
  let l = 0;
  let r = B.length - 1;
  while(true) {
      let i = Math.floor((l+r)/2);
      let j = half - i - 2;

      let AL = j<0 ? Number.MIN_SAFE_INTEGER : A[j];
      let AR = j+1>A.length-1 ? Number.MAX_SAFE_INTEGER : A[j+1];
      let BL = i<0 ? Number.MIN_SAFE_INTEGER : B[i];
      let BR = i+1>B.length-1 ? Number.MAX_SAFE_INTEGER : B[i+1];

      if(AL <= BR && BL <= AR) {
          if(total%2) {
              return Math.min(AR,BR);
          } else {
              return ((Math.max(AL,BL) + Math.min(AR,BR))/2)
          }
      } else if(BL > AR) {
          r = i - 1;
      } else {
          l = i + 1;
      }
  }
};

console.log(findMedianSortedArrays([1,2],[3,4]));