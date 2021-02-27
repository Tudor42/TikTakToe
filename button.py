import pygame

class Button:
  def __init__(self, image_pressed, image_released, width, height, xcoord, ycoord):
    self.image_pressed = pygame.transform.scale(pygame.image.load(image_pressed), (width, height))
    self.image_released = pygame.transform.scale(pygame.image.load(image_released), (width, height))
    self.image_rect = self.image_pressed.get_rect()
    self.image_rect.x = xcoord
    self.image_rect.y = ycoord
    self.use = 0

  def checkPress(self, x, y):
    if x>self.image_rect.x and y>self.image_rect.y and \
      x<(self.image_rect.x+self.image_rect.width) and \
      y<(self.image_rect.y+self.image_rect.height):
      return True
    else:
      return False

  def draw(self, surface):
    if self.use == 0:
      surface.blit(self.image_released, self.image_rect)
    else:
      surface.blit(self.image_pressed, self.image_rect)