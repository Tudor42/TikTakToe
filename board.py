import pygame
from pygame import gfxdraw
from math import sqrt

color = (30, 30, 200)

class Board:
  def __init__(self):
    self.board = [
      [0, 0, 0],
      [0, 0, 0], 
      [0, 0, 0]
    ]
    self.lineswidth = 5

  def update(self, turn, surfaceW, surfaceH, mouseposX, mouseposY):
    if(turn == 1):
      if self.putO(int(mouseposY/(surfaceH/3)),int(mouseposX/(surfaceW/3))):
        return True
    if(turn == 2):
      if self.putX(int(mouseposY/(surfaceH/3)),int(mouseposX/(surfaceW/3))):
        return True
    return False

  def draw(self, surface, surfaceW, surfaceH):
    stepW = (surfaceW)/3
    for i in range(4):
      pygame.draw.line(surface, color, (i*stepW, 0), (i*stepW, surfaceH), self.lineswidth)
    stepH = (surfaceH)/3
    for i in range(4):
      pygame.draw.line(surface, color, (0, i*stepH), (surfaceW, i*stepH), self.lineswidth)
    for i in range(3):
      for j in range(3):
        if self.board[i][j]==1:
          #print((int(i*stepH+stepH/2), int(j*stepW+stepW/2)), surface, int(stepW), int(stepH))
          self._drawO((i,j), surface, int(stepW), int(stepH))
        if self.board[i][j]==2:
          self._drawX((i, j), surface, int(stepW), int(stepH))
  def putO(self, x, y):
    if x<3 and x>=0 and y<3 and y>=0 and self.board[y][x]==0:
      self.board[y][x] = 1
      return True
    else:
      print("Err: board \n func putO()")
    return False

  def putX(self, x, y):
    if x<3 and x>=0 and y<3 and y>=0 and self.board[y][x]==0:
      self.board[y][x] = 2
      return True
    else:
      print("Err: board \n func putX()")
    return False

#draw functions copied from https://github.com/denis-svg/Tic-Tac-Toe/blob/main/client.py
  def _drawO(self, pos, surface, square_width, square_height):
    w = square_width
    h = square_height
    rx = square_width // 2 - int(0.15 * w)
    ry = square_height // 2 - int(0.15 * h)
    rx1 = rx - round(sqrt(2 * (int(0.22 * w) - int(0.15 * w)) ** 2))
    ry1 = ry - round(sqrt(2 * (int(0.22 * h) - int(0.15 * h)) ** 2))
    gfxdraw.aaellipse(surface, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx, ry, (255, 255, 255))
    gfxdraw.filled_ellipse(surface, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx, ry,
                               (255, 255, 255))
    gfxdraw.aaellipse(surface, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx1, ry1, (0, 0, 0))
    gfxdraw.filled_ellipse(surface, pos[0] * w + int(0.5 * w), pos[1] * h + int(0.5 * h), rx1, ry1, (0, 0, 0))

  def _drawX(self, pos, surface, square_width, square_height):
    w = square_width
    h = square_height
    points = [(pos[0] * w + int(0.15 * w), pos[1] * h + int(0.22 * h)),
              (pos[0] * w + int(0.22 * w), pos[1] * h + int(0.15 * h)),
              (pos[0] * w + int(0.85 * w), pos[1] * h + int(0.78 * h)),
                  (pos[0] * w + int(0.78 * w), pos[1] * h + int(0.85 * h))]
    pygame.draw.polygon(surface, (255, 255, 255), points)
    points = [(pos[0] * w + int(0.15 * w), pos[1] * h + int(0.78 * h)),
                  (pos[0] * w + int(0.22 * w), pos[1] * h + int(0.85 * h)),
                  (pos[0] * w + int(0.85 * w), pos[1] * h + int(0.22 * h)),
                  (pos[0] * w + int(0.78 * w), pos[1] * h + int(0.15 * h))]
    pygame.draw.polygon(surface, (255, 255, 255), points, 0)

  def winnerChecker(self):
    draw = True
    #check lines
    for j in range(3):
      winX = True
      winO = True
      for i in range(3):
        if self.board[j][i] == 0:
          draw = False
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
    if draw:
      return 0
    return -1 