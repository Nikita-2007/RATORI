import pygame as pg

class Button(object):
    pg.font.init()
    _font_ = pg.font.SysFont('cambria', 30)

    def __init__(self, posX, posY, name):
        '''КНОПКА'''
        self.name = name
        self.active = True
        self.focus = False
        self.pressed = False
        self.rect = pg.Rect(posX, posY, 300, 100)

    def draw(self, g):
        '''Отрисовка кнопок'''
        pg.draw.rect(g, 'blue', self.rect)
        self.text_button = self._font_.render(self.name, True, 'lightblue')
        self.text_rect = self.text_button.get_rect()
        self.text_rect.center = self.rect.center
        g.blit(self.text_button, self.text_rect)