import pygame as pg
from modules.ground.Ground import Ground
from modules.unit.Unit import Unit
from modules.interface.Interface import Interface
from modules.unit.Hero import Hero

class Game(object):

    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.ground = Ground()
        self.unit = Unit()
        self.hero = Hero(self.size)
        self.interface = Interface(size)
        self.unit.rect.center = self.position(size)
        self.hero.rect.center = self.position(size)

    def update(self, e):
        """Обновление"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.unit.rect.center = self.position(size)
            self.hero.rect.center = self.position(size)
        if e.type == pg.KEYUP and e.key == pg.K_UP:
            self.hero.rect.y -= 1
        if e.type == pg.KEYUP and e.key == pg.K_DOWN:
            self.hero.rect.y += 1
        if e.type == pg.KEYUP and e.key == pg.K_LEFT:
            self.hero.rect.x -= 1
        if e.type == pg.KEYUP and e.key == pg.K_RIGHT:
            self.hero.rect.x += 1
        self.interface.update(size)

    def draw(self, g):
        """Отрисовка"""
        self.ground.draw(g)
        self.interface.draw(g)
        #self.unit.draw(g)
        self.hero.draw(g)

    def position(self, size):
        x = size[0]//2
        y = size[1]//2
        return x, y