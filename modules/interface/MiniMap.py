import pygame as pg
from modules.ground.Terrain import Terrain


class MiniMap(object):
    def __init__(self, size):
        """Конструктор"""
        self.terrain = Terrain()
        self.count_x = len(self.terrain.map[0])
        self.count_y = len(self.terrain.map)
        self.size = size
        self.rate = self.size[0] // (self.count_x * 3)
        self.rect = self.position()
        self.hero = self.pos_hero(self.terrain.start_point)

    def update(self):
        """Обновление"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.rate = self.size[0] // (self.count_x * 3)
            self.rect = self.position()
        self.hero = self.pos_hero(self.hero)


    def draw(self, g):
        """Отрисовка"""
        for y in range(self.count_y):
            for x in range(self.count_x):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                tile = pg.transform.scale(tile, (self.rate, self.rate))
                g.blit(tile, (self.rate * x + self.rect[0], self.rate* y + self.rect[1], self.rate, self.rate))
        pg.draw.rect(g, 'pink', self.rect, 5)
        pg.draw.circle(g, 'red', self.hero, 5)

    def position(self):
        x1 = 3
        x2 = self.rate * self.count_x
        y2 = self.rate * self.count_y
        y1 = self.size[1] - y2
        return x1, y1, x2, y2

    def pos_hero(self, hero):
        '''Расчёт позиции героя'''
        x = hero[0] * (self.rate // (self.count_x * 48))
        y = 200
        return x, y