import pygame as pg
from modules.Button import Button

class Menu(object):

    #MENU
    def __init__(self):
        self.button = Button()

    #Обновление
    def update(self, e):
        pass

    #Отрисовка меню
    def draw(self, g):
        g.fill('blue')
        self.button.draw(g)