import pygame as pg

class Hero(object):
    _atlas_ = pg.image.load("images\Hero.png")
    _rate_ = 64

    def __init__(self, size):
        """Конструктор"""
        pg.init()
        self.rate = self._rate_
        self.rect = pg.Rect(0, 0, self.rate, self.rate)
        self.tile_atlas = []
        self.tile_atlas = self.filling()
        self.row = 0
        self.col = 0
        self.step = 0
        self.speed = 1
        self.image = self.tile_atlas[self.row][self.col]

    def update(self, turn):
        """Обновление"""
        self.turn = turn
        if self.turn == 'stop':
            self.image = self.tile_atlas[0][0]
        else:
            if self.turn == 'right_down':
                self.col = 1
            elif self.turn == 'left_down':
                self.col = 7
            elif self.turn == 'left_up':
                self.col = 5
            elif self.turn == 'right_up':
                self.col = 3
            elif self.turn == 'right':
                self.col = 2
            elif self.turn == 'left':
                self.col = 6
            elif self.turn == 'down':
                self.col = 0
            elif self.turn == 'up':
                self.col = 4
        self.select()

    def draw(self, g):
        """Отрисовка"""
        self.image = self.tile_atlas[self.row][self.col]
        g.blit(self.image, self.rect)

    def select(self):
        """Заполнение"""
        if self.step == 7:
            self.row += 1
            self.step = 0
            pg.mixer.Sound.play(pg.mixer.Sound("sounds\sound.wav"))
        self.step += self.speed
        if self.row >= 4:
            self.row = 1

    def filling(self):
        """Заполняет атлас"""
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        for row in range(atlas.get_height() // rate):
            self.tile_atlas.append([])
            for col in range(atlas.get_width() // rate):
                rect = (col * rate, row * rate)
                image = atlas.subsurface(rect, size)
                image = pg.transform.scale(image, (96, 96))
                self.tile_atlas[row].append(image)
        return self.tile_atlas