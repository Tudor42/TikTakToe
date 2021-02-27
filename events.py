import pygame
import sys

class Events:
  #class to use for keys and mouse events
  def __init__(self):
    self.mousekeys = pygame.mouse.get_pressed()
    self.keys = pygame.key.get_pressed()

  def update(self):
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