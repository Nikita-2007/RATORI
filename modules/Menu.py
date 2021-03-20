import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['Start', 'LoadGame', 'Option', 'Return', 'Language ', 'Respawn', 'Exit to Mneu', 'Выход']

    def __init__(self, size):
        '''MENU'''
        self.size = size
        self.list_button = []
        for i in range (8):
            btn_pos = self.position(i)
            self.button = Button(btn_pos, self.button_name[i])
            self.list_button.append(self.button)
        self.button_action = None
        self.list_button[6].active = False

    def update(self, e):
        '''Обновление'''
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            for i in range(8):
                btn_pos = self.position(i)
                self.list_button[i].rect.x = btn_pos[0]
                self.list_button[i].rect.y = btn_pos[1]

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
                    self.button_action = None
            else:
                button.focus = False
            button.update()

    def draw(self, g):
        '''Отрисовка меню'''
        g.fill('lightgreen')
        for button in self.list_button:
            button.draw(g)

    def functions(self, button_name):
        if self.button_action != button_name:
            self.button_action = button_name
            if button_name == self.button_name[0]:
                print("Нажата кнопка", button_name)
            if button_name == self.button_name[1]:
                print("Нажата кнопка", button_name)
            if button_name == self.button_name[2]:
                print("Нажата кнопка", button_name)
            if button_name == self.button_name[3]:
                print("Нажата кнопка", button_name)
            if button_name == self.button_name[4]:
                print("Нажата кнопка", button_name)
            if button_name == self.button_name[5]:
                print("Нажата кнопка", button_name)
            if button_name == self.button_name[6]:
                print("Нажата кнопка", button_name)
            if button_name == self.button_name[7]:
                pg.quit()
                quit()

    def position(self, i):
        if i < 4:
            posX = self.size[0]//2-320
            posY = self.size[1]//2 + i * 120 - 250
        else:
            posX = self.size[0]//2
            posY = self.size[1]//2 + i * 120 - 730
        return posX, posY