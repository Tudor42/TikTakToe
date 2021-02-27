from board import Board
import pygame

class Game:
  def __init__(self, surface, surfaceW, surfaceH, events):
    self.surface = surface
    self.surfaceH = surfaceH
    self.surfaceW = surfaceW
    self.board = Board()
    self.turn = 1
    self.click = True
    self.events = events

  def update(self, events):
    self.surface.fill((0,0,0))
    self.board.draw(self.surface, self.surfaceW, self.surfaceH)
    if not events.mousekeys[0]:
      self.click = True
    if events.mousekeys[0] and self.click:
      if self.board.update(self.turn, self.surfaceW, self.surfaceH, events.mousePos[0], events.mousePos[1]):
        print(self.board.board)
        if self.turn == 1:
          self.turn = 2
        else:
          self.turn = 1
      self.click = False
    pygame.display.flip()
    return self.board.winnerChecker()

  def run(self):
    while(True):
      self.events.update()
      winner = self.update(self.events)
      if winner != -1:
        return winner