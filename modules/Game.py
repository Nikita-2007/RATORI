import pygame as pg
from modules.Ground import Ground
from modules.Unit import Unit
from modules.Interface import Interface

class Game(object):

    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.ground = Ground()
        self.unit = Unit()
        self.interface = Interface()
        self.unit.rect.center = self.position(size)

    def update(self, e):
        """Обновление"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.unit.rect.center = self.position(size)
        if e.type == pg.KEYUP and e.key == pg.K_UP:
            self.unit.rect.y -= 5
        if e.type == pg.KEYUP and e.key == pg.K_DOWN:
            self.unit.rect.y += 5
        if e.type == pg.KEYUP and e.key == pg.K_LEFT:
            self.unit.rect.x -= 5
        if e.type == pg.KEYUP and e.key == pg.K_RIGHT:
            self.unit.rect.x += 5

    def draw(self, g):
        """Отрисовка"""
        self.interface.draw(g)
        self.ground.draw(g)
        self.unit.draw(g)

    def position(self, size):
        x = size[0]//2
        y = size[1]//2
        return x, y