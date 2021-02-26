import pygame
import sys

class Tetris:
  def __init__(self):
    pygame.display.init()
    self.screen = pygame.display.set_mode((800, 600))

  def keysHandle(self):
    if self.keys[pygame.K_a]:
      self.screen.fill((255,255,255))
    else:
      self.screen.fill((255,0,0))

  def update(self):
    pygame.display.flip()

  def eventsHandle(self):
    events = pygame.event.get()
    self.keys = pygame.key.get_pressed()
    for event in events:
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        self.keys = pygame.key.get_pressed()
      self.keysHandle()

  def run(self):
    while(True):
      self.eventsHandle()
      self.update()

if __name__=="__main__":
  game = Tetris()
  game.run()