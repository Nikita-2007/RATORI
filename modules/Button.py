import pygame as pg

class Button(object):
    pg.font.init()
    _font_ = pg.font.SysFont('Agency FB', 40)

    def __init__(self, posX, posY, name):
        '''КНОПКА'''
        self.name = name
        self.font_color = 'lightblue'
        self.active = True
        self.focus = False
        self.pressed = False
        self.rect = pg.Rect(posX, posY, 300, 100)

    def update(self):
        '''Обновление'''
        if self.active:
            self.font_color = 'lightblue'
            if self.focus:
                self.font_color = 'lightpink'
                if self.pressed:
                    self.font_color = 'white'
        else:
            self.font_color = 'black'

    def draw(self, g):
        '''Отрисовка кнопок'''
        pg.draw.rect(g, 'darkblue', self.rect, 10)
        pg.draw.rect(g, 'blue', self.rect)
        self.text_button = self._font_.render(self.name, True, self.font_color)
        self.text_rect = self.text_button.get_rect()
        self.text_rect.center = self.rect.center
        g.blit(self.text_button, self.text_rect)