class Board:
  def __init__(self):
    self.grid = [[""] * 3 for _ in range(3)]
  
  def isValidMove(self, row: int, col: int):
    return (0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == "")
  
  def isFull(self):
    for r in range(3):
      for c in range(3):
        if self.grid[r][c] == "":
          return False
    return True

  def getGrid(self):
    return self.grid
  
  def placeMove(self, row, col, symbol):
    self.grid[row][col] = symbol
  
  def displayBoard(self):
    for r in range(3):
      print(self.grid[r][0] + "|" + self.grid[r][1] + "|" + self.grid[r][2])
      if r < 2:
        print("----------")

class Player:
  def __init__(self, symbol, name):
    self.name = name
    self.symbol = symbol
  
  def getName(self):
    return self.name

  def getSymbol(self):
    return self.symbol
  
  def makeMove(self, board: Board):
      while True:
          try:
              row = int(input('Enter Row (0-2): '))
              col = int(input('Enter Col (0-2): '))
          except ValueError:
              print("Invalid input. Please enter a number.")
              continue
          if board.isValidMove(row, col):
              return row, col
          else:
              print("Invalid move. Try again.")

class Game:
  def __init__(self, board: Board, players: list[Player]):
    self.board = board
    self.players = players
    self.currentPlayerIndex = 0
  
  def start(self):
    while not self.board.isFull():
      self.board.displayBoard()
      currentPlayer = self.players[self.currentPlayerIndex]
      row, col = currentPlayer.makeMove(self.board)
      symbol = currentPlayer.getSymbol()
      self.board.placeMove(row, col, symbol)
      if self.checkWinner(symbol):
        print(currentPlayer.getName() + " with symbol: " + currentPlayer.getSymbol() + " wins.")
        break
      self.currentPlayerIndex = 1 - self.currentPlayerIndex
    
    print("Its a draw!!")
    self.board.displayBoard()
  
  def checkWinner(self, symbol):
    grid = self.board.getGrid()
    n = len(grid)
    if grid[0][0] == grid[1][1] == grid[2][2] == symbol: return True
    if grid[0][2] == grid[1][1] == grid[2][0] == symbol: return True

    for i in range(3):
      if grid[i][0] == grid[i][1] == grid[i][2] == symbol: return True
      if grid[0][i] == grid[1][i] == grid[2][i] == symbol: return True
    
    return False
  
p1 = Player('X', 'Dip')
p2 = Player('O', 'Suk')
board = Board()
game = Game(board, [p1, p2])
game.start()