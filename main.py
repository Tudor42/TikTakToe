import pygame
import sys
from board import Board

class Tetris:
  def __init__(self):
    pygame.display.init()
    self.screenwidth = 600
    self.screenheight = 600
    self.screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
    self.mousekeys = pygame.mouse.get_pressed()
    self.keys = pygame.key.get_pressed()
    self.board = Board()

  def displayWinner(self):
    return

  def gamerestart(self):
    self.board = Board()

  def draw(self):
    self.board.draw(self.screen, self.screenwidth, self.screenheight)

  def keysHandle(self):
    if self.keys[pygame.K_a]:
      self.gamerestart()
    elif self.mousekeys[0]:
      self.board.update(1, self.screenwidth, self.screenheight, self.mousePos[0], self.mousePos[1])
    else:
      self.screen.fill((0,0,0))

  def update(self):
    self.draw()
    if self.board.winnerChecker() == 1:
      self.displayWinner()
      self.gamerestart()
    pygame.display.flip()

  def eventsHandle(self):
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        self.keys = pygame.key.get_pressed()
      if event.type == pygame.MOUSEMOTION:
        self.mousePos = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
        self.mousekeys = pygame.mouse.get_pressed()
      self.keysHandle()

  def run(self):
    while(True):
      self.eventsHandle()
      self.update()

if __name__=="__main__":
  game = Tetris()
  game.run()