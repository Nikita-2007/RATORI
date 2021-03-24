import sys
from random import randint
import pygame as pg

class Terrain(object):
    _atlas_ = pg.image.load("images\sprite.bmp")
    _atlas_.set_colorkey((255, 255, 255))
    _rate_ = 48

    def __init__(self):
        """Конструктор"""
        self.image = self._atlas_
        self.rect = (48, 48)
        self.image = self._atlas_.subsurface((0, 0), (48, 48))


    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.image, self.rect)
