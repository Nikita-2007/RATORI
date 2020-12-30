import pygame as pg
from modules.Unit import Unit

class Game(object):

    #GAME
    def __init__(self):
        self.unit = Unit()

    # Обновление
    def update(self, e):
        if e.type == pg.KEYUP and e.key == pg.K_UP:
            self.unit.rect.y -= 5
        if e.type == pg.KEYUP and e.key == pg.K_DOWN:
            self.unit.rect.y += 5
        if e.type == pg.KEYUP and e.key == pg.K_LEFT:
            self.unit.rect.x -= 5
        if e.type == pg.KEYUP and e.key == pg.K_RIGHT:
            self.unit.rect.x += 5

    #Отрисовка игры
    def draw(self, g):
        g.fill('red')
        self.unit.draw(g)