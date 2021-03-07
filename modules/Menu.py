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
        self.button_action = None
        self.list_button[6].active = False

    def update(self, e):
        '''Обновление'''
        if e.type == pg.MOUSEMOTION:
            self.button_action = None
        pos = pg.mouse.get_pos()
        click = pg.mouse.get_pressed(3)
        for button in self.list_button:
            if button.active and button.rect.collidepoint(pos):
                button.focus = True
                if click[0]:
                    button.pressed = True
                    self.functions(button.name)
                else:
                    button.pressed = False
            else:
                button.focus = False
            button.update()

    def draw(self, g):
        '''Отрисовка меню'''
        g.fill('lightgreen')
        for button in self.list_button:
            button.draw(g)

    def functions(self, button_name):
        pass