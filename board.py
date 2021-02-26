import pygame

color = (30, 30, 200)

class Board:
  def __init__(self):
    self.board = [
      [0, 0, 0],
      [0, 0, 0], 
      [0, 0, 0]
    ]
    self.lineswidth = 2

  def update(self, turn, surfaceW, surfaceH, mouseposX, mouseposY):
    if(turn == 1):
      self.putO(int(mouseposY/(surfaceH/3)),int(mouseposX/(surfaceW/3)))
    if(turn == 2):
      self.putX(int(mouseposY/(surfaceH/3)),int(mouseposX/(surfaceW/3)))

  def draw(self, surface, surfaceW, surfaceH):
    stepW = (surfaceW-self.lineswidth)/3
    for i in range(5):
      pygame.draw.line(surface, color, (i*stepW, 0), (i*stepW, surfaceH), self.lineswidth)
    stepH = (surfaceH-self.lineswidth)/3
    for i in range(5):
      pygame.draw.line(surface, color, (0, i*stepH), (surfaceW, i*stepH), self.lineswidth)
    for i in range(3):
      for j in range(3):
        if self.board[i][j]==1:
          pygame.draw.circle(surface, (255, 255, 255), (i*stepH+stepH/2, j*stepW+stepW/2), stepH/2, self.lineswidth)

  def putO(self, x, y):
    if x>2 or x<0 or y>2 or y<0:
      print("Err: board \n func putO()")
    else:
      self.board[y][x] = 1

  def putX(self, x, y):
    if x>3 or x<0 or y>3 or y<0:
      print("Err: board \n func putX()")
    else:
      self.board[y][x] = 2

  def winnerChecker(self):
    #check lines
    for j in range(3):
      winX = True
      winO = True
      for i in range(3):
        if self.board[j][i] != 1:
          winO = False
        if self.board[j][i] != 2:
          winX = False
      if winO:
        return 1
      if winX:
        return 2
    #check columns
    for i in range(3):
      winX = True
      winO = True
      for j in range(3):
        if self.board[j][i] !=1:
          winO = False
        if self.board[j][i] != 2:
          winX = False
      if winO:
        return 1
      if winX:
        return 2
    #check diagonals
    winX = True
    winO = True
    for i in range(3):
      if self.board[i][i] !=1:
        winO = False
      if self.board[i][i] != 2:
        winX = False
    if winO:
      return 1
    if winX:
      return 2
    winX = True
    winO = True
    for i in range(3):
      if self.board[i][2-i] !=1:
        winO = False
      if self.board[i][2-i] != 2:
        winX = False
    if winO:
      return 1
    if winX:
      return 2