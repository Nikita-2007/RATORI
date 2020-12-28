import pygame as pg

class Unit(object):
    pg.init()

    _image_ = pg.image.load("images\exit.png")

    #UNIT
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    #Отрисовка юнита
    def draw(self, g):
        g.blit(self.image, (self.rect.x, self.rect.y))