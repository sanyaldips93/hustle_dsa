/**
 * Find the smallest continuous subarray with sum greater than a given value
    arr[] = [1, 4, 45, 6, 0, 19]
    target  =  51
    Output is {4, 45, 6}
 */

function subArray(arr, target) {
  let left = 0;
  let right = 0;
  const length = arr.length;
  let tempSum = 0;
  const idxArr = [left, right];
  let minLength = 8888;
  while (right < length) {
    tempSum += arr[right];
    if (tempSum > target) {
      while(tempSum > target) {
        tempSum -= arr[left];
        left = left + 1;
      }
      if ((right - left + 1) < minLength) {
        minLength = right - left + 1;
        idxArr[0] = left - 1;
        idxArr[1] = right;
      }
    }
    right = right + 1;
  }
  
  const finalArray = [];
  for(let i = idxArr[0]; i <= idxArr[1]; i++) {
    finalArray.push(arr[i]);
  }
  return finalArray;
}  

console.log(subArray([ 20, 3,9,6, 21, 1, 2,0, 3, 6, 45, 4, 1, 35, 4,5, 1, 6, 20, 4 ] , 54));



/**
 * occurence = {5:1, 2:1, 6:3, 9:1, 11:1, 4:2, 3:2};
 * - [5, 2, 6, 3, 9, 11, 6, 4, 4, 3, 6] 
 * target = 9
 * hash[7] = 2;
 * hash[3] = 6;
 * hash[6] = 3;
 */

/**
 * Step 1 : we find the frequency of each number and store it in a hash table.
 * Step 2 : we travese through the input array to find pairs.
 * Step 3 : once we find a hit, we reduce the frequency of each numbers in the frequency hash table to weed out multiple duplicacies.
 * We also save the pair in a final list.
 * Step 4: repeat this process till the end of the array.
 * Step 5: return the final list.
 */