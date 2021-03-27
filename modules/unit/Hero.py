import pygame as pg

class Hero(object):
    _atlas_ = pg.image.load("images\Sprite.png")
    _rate_ = 48

    def __init__(self, size):
        """Конструктор"""
        self.rate = self._rate_
        self.rect = pg.Rect(0, 0, self.rate, self.rate)

    def update(self, e):
        """Обновление"""


    def draw(self, g):
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        rect = (0, 0)
        image = atlas.subsurface(rect, size)
        image = pg.transform.scale(image, (96, 96))
        rect = self.rect
        g.blit(image, rect)
