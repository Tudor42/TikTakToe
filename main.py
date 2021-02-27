import pygame
import sys
from gameloop import Game
from events import Events
from button import Button

color_menu = (255,200,200)

class Tik_Tak_Toe:
  def __init__(self):
    pygame.display.init()
    self.screenwidth = 100
    self.screenheight = 100
    self.screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
    self.events = Events()

    if self.screenheight > self.screenwidth:
      calc = self.screenwidth
    else:
      calc = self.screenheight

    self.button_start = Button("images/buttons/start_pressed.png", "images/buttons/start_released.png", int(calc/3)*2, int(calc/3), (self.screenwidth-2*calc/3)/2, 10)

  def keysHandle(self):
    if self.events.mousekeys[0] and \
    self.button_start.checkPress(self.events.mousePos[0], self.events.mousePos[1]):
    #check button start
      self.button_start.use = 1
    elif self.button_start.use == 1:
      self.button_start.use = 0
      self.game = Game(self.screen, self.screenwidth, self.screenheight, self.events)
      print(self.game.run())
      while self.events.mousekeys[0]:
        self.events.update()


  def update(self):
    self.screen.fill(color_menu)
    self.button_start.draw(self.screen)
    self.keysHandle()
    pygame.display.flip()

  def run(self):
    while(True):
      self.events.update()
      self.update()

if __name__=="__main__":
  game = Tik_Tak_Toe()
  game.run()