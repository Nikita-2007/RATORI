import sys
from random import randint
import pygame as pg

class Terrain(object):

    _atlas_ = pg.image.load("images\sprite.bmp")
    _atlas_.set_colorkey((255, 255, 255))

    def __init__(self):
        """Конструктор"""
        self.image = self._atlas_
        self.rect = self.image.get_rect()

    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.image, self.rect)
