import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['Start', 'LoadGame', 'Option', 'Return', 'Language ', 'Respawn', 'Exit to Mneu', 'Exit']

    def __init__(self):
        '''MENU'''
        self.list_button = []
        for i in range (8):
            self.button = Button(50, i*30, self.button_name[i])
            self.list_button.add(self.button)

    def update(self, e):
        '''Обновление'''
        pass

    def draw(self, g):
        '''Отрисовка меню'''
        g.fill('blue')
        for i in range(8):
            #button = self.list_button[i]
            self.button.draw(g)