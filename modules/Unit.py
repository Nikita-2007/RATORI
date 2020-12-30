import pygame as pg

class Unit(object):
    pg.init()

    _image_ = pg.image.load("images\exit.png")
    sound = pg.mixer.Sound("sounds\click.wav")

    #UNIT
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    #Отрисовка юнита
    def draw(self, g):
        self.rect.x += 1
        g.blit(self.image, self.rect)
        if self.rect.x == 300:
            pg.mixer.Sound.play(self.sound)