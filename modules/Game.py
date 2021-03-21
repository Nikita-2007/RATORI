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
        self.unit.rect = self.position()

    def update(self, e):
        """Обновление"""
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
        g.fill('red')
        self.unit.draw(g)

    def position(self):
        self.unit.rect.x = self.size[0]//2 - self.unit.rect.width//2
        self.unit.rect.y = self.size[1]//2 - self.unit.rect.height//2
        return self.unit.rect