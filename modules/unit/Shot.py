import pygame as pg


class Shot(object):
    def __init__(self):
        """Конструктор"""
        self.point_x, self.point_y = 100, 100
        self.unit_turn = 3

    def update(self, turn):
        """Обновление"""
        pass

    def draw(self, g):
        """Отрисовка"""
        pg.draw.circle(g, 'Orange', (self.point_x, self.point_y), 4)
