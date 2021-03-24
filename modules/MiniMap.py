import sys
from random import randint
import pygame as pg


class MiniMap(object):
    def __init__(self, size):
        """Конструктор"""
        self.rect = self.position(size)

    def update(self, size):
        """Обновление"""
        self.rect = self.position(size)

    def draw(self, g):
        """Отрисовка"""
        pg.draw.rect(g, 'pink', self.rect, 5)

    def position(self, size):
        x1 = 0
        y1 = size[1]//3*2
        x2 = size[0]//3
        y2 = size[1]
        return x1, y1, x2, y2