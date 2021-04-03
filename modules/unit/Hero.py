import pygame as pg

class Hero(object):
    _atlas_ = pg.image.load("images\Sprite.png")
    _rate_ = 64

    def __init__(self, size):
        """Конструктор"""
        self.rate = self._rate_
        self.rect = pg.Rect(0, 0, self.rate, self.rate)
        self.tile_atlas = []
        self.tile_atlas = self.filling()

    def draw(self, g):
        rect = self.rect
        g.blit(self.tile_atlas[0][0], rect)
        g.blit(self.tile_atlas[4][0], rect)
        g.blit(self.tile_atlas[0][4], rect)
        g.blit(self.tile_atlas[4][4], rect)

    def filling(self):
        """Заполняет атлас"""
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        for row in range(atlas.get_height() // rate):
            self.tile_atlas.append([])
            for col in range(atlas.get_width() // rate):
                rect = (col * rate, row * rate)
                image = atlas.subsurface(rect, size)
                image = pg.transform.scale(image, (96, 96))
                self.tile_atlas[row].append(image)
        return self.tile_atlas