import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['Start', 'LoadGame', 'Option', 'Return', 'Language ', 'Respawn', 'Exit to Mneu', 'Exit']

    def __init__(self):
        '''MENU'''
        self.list_button = []
        for i in range (8):
            posY = 100
            posX = 330
            temp = i
            if i > 3:
                posX = 650
                temp = temp - 4
            self.button = Button(posX, posY*temp*1.2+100, self.button_name[i])
            self.list_button.append(self.button)

    def update(self, e):
        '''Обновление'''
        pass

    def draw(self, g):
        '''Отрисовка меню'''
        g.fill('lightgreen')
        for button in self.list_button:
            button.draw(g)