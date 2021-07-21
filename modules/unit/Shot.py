import pygame as pg
from modules.unit.Abstract import Abstract


class Shot(Abstract):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.point_x, self.point_y = self.size[0] // 2 + 25, self.size[1] // 2 + 25
        self.unit_turn = 8

    def update(self, turn):
        """Обновление"""
        self.pos_unit(turn)

    def draw(self, g):
        """Отрисовка"""
        print(self.point_x)
        pg.draw.circle(g, 'Orange', (self.point_x, self.point_y), 4)

    def Shot(self):
        self.point_x = 100
        print(self.point_x)