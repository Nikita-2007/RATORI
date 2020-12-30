import pygame as pg

class Button(object):

    _image_ = pg.image.load("images\Start.png")

    #BUTTODN
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    #Отрисовка кнопок
    def draw(self, g):
        g.blit(self.image, self.rect)