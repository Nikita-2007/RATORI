import pygame as pg
from modules.map import map as _map_

class Terrain(object):
    _atlas_ = pg.image.load("images\sprite.bmp")
    _atlas_.set_colorkey((255, 255, 255))
    _rate_ = 48

    def __init__(self):
        """Атлас"""
        self.map = _map_
        self.rate = self._rate_
        self.tile_atlas = {}
        self.tile_atlas = self.filling()
        self.start_point = (1536, 768)

    def filling(self):
        """Заполняет атлас"""
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        for row in range(atlas.get_height() // rate):
            for col in range(atlas.get_width() // rate):
                rect = (col * rate, row * rate)
                image = atlas.subsurface(rect, size)
                key = str(f'{row:0{2}}') + str(f'{col:0{2}}')
                self.tile_atlas[key] = image
        return self.tile_atlas