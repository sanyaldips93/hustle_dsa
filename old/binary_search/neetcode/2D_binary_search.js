var searchMatrix = function(matrix, target) {
  let row = matrix.length;
  let col = matrix[0].length;
  let top = 0;
  let bot = row - 1;
  while(top <= bot) {
      let mid = Math.trunc((top+bot)/2);
      if(target > matrix[mid][matrix[0].length - 1]) {
          top = mid + 1;
      } else if(target < matrix[mid][0]) {
          bot = mid - 1;
      } else {
          break;
      }
  }
  if(top > bot) {
      return false;
  }
  let l = 0;
  let r = col - 1;
  let currRow = Math.trunc((top+bot)/2);
  while(l <= r) {
      let m = Math.trunc((l+r)/2);
      if(target > matrix[currRow][m]) {
          l = m + 1;
      } else if(target < matrix[currRow][m]) {
          r = m - 1;
      } else { 
          return true;
      }
  }
  return false;
};

console.log(searchMatrix([[1],[3]], 3));