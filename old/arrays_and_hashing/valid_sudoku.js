var isValidSudoku = function(board) {
  const hashCol = {};
  const hashRow = {};
  const hashGrid = {};

  for(let row=0; row<9; row++) {
      for(let col=0; col<9; col++) {
          const num = board[row][col];
          if(num === '.') continue;
          const gridPosition = `${Math.floor(row/3)}:${Math.floor(col/3)}`;

          if(!hashRow[row]) hashRow[row] = new Set();
          if(!hashCol[col]) hashCol[col] = new Set();
          if(!hashGrid[gridPosition]) hashGrid[gridPosition] = new Set();

          if(hashCol[col].has(num) 
          || hashRow[row].has(num) 
          || hashGrid[gridPosition].has(num)
          ) {
              return false;
          }
          
          hashRow[row].add(num);
          hashCol[col].add(num);
          hashGrid[gridPosition].add(num);
      }
      return true;
  }
};