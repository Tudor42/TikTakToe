import pygame
import sys
from gameloop import Game
from events import Events

class Tik_Tak_Toe:
  def __init__(self):
    pygame.display.init()
    self.screenwidth = 800
    self.screenheight = 800
    self.screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
    self.events = Events()

  def keysHandle(self):
    if self.events.keys[pygame.K_a]:
      self.game = Game(self.screen, self.screenwidth, self.screenheight, self.events)
      print(self.game.run())
      return
    if self.events.keys[pygame.K_q]:
      return

  def update(self):
    self.keysHandle()
    self.screen.fill((0,0,0))
    pygame.display.flip()

  def run(self):
    while(True):
      self.events.update()
      self.update()

if __name__=="__main__":
  game = Tik_Tak_Toe()
  game.run()