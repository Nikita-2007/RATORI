import sys
from random import randint
from modules.Terrain import Terrain

class Ground(object):
    def __init__(self):
        """Конструктор"""
        self.terrain = Terrain()

    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        """Отрисовка"""
        self.terrain.draw(g)
