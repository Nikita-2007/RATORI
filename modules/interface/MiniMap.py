import pygame as pg
from modules.ground.Terrain import Terrain


class MiniMap(object):
    def __init__(self, size):
        """Конструктор"""
        self.Terrain = Terrain()
        self.count_x = len(self.Terrain.map[0])
        self.count_y = len(self.Terrain.map)
        self.size = size
        self.rate = 0
        self.rect = self.position(size)

    def update(self, size):
        """Обновление"""
        self.rate = self.size[0] // (self.count_x * 3)
        self.rect = self.position(size)

    def draw(self, g):
        """Отрисовка"""
        for y in range(self.count_y):
            for x in range(self.count_x):
                key = self.Terrain.map[y][x]
                tile = self.Terrain.tile_atlas[key]
                g.blit(tile, (self.rate * x + self.rect[0], self.rate* y + self.rect[1], self.rate, self.rate))
        pg.draw.rect(g, 'pink', self.rect, 5)

    def position(self, size):
        x1 = 0
        y1 = size[1]//3*2
        x2 = self.rate * self.count_x
        y2 = size[1]
        return x1, y1, x2, y2