import pygame as pg
from random import randint as r


class Сivil(object):
    pg.init()
    _atlas_ = pg.image.load("images\Сivil.png")
    _rate_ = 64

    def __init__(self, size):
        """Конструктор"""
        self.rate = self._rate_
        self.size = size
        self.tile_atlas = []
        self.tile_atlas = self.filling()
        self.row = 0
        self.col = 0
        self.step = 0
        self.unit_turn = 8
        self.image = self.tile_atlas[self.row][self.col]
        self.point_x, self.point_y = (r(self.size[0] // 4, self.size[0] // 4 * 3)), (r(self.size[1] // 4, self.size[1] // 4 * 3))
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate, self.rate)
        self.scroll_line = 3
        self.scroll = round(self.scroll_line / 1.4)
        self.time_move = 60
        self.speed = 1

    def update(self, turn):
        """Обновление"""
        self.rect.x, self.rect.y = self.pos_unit(turn)
        if self.time_move < 1:
            self.unit_turn = r(0, 10)
            self.time_move = r(80, 160)
        self.time_move -= 1
        if self.unit_turn > 7:
            self.image = self.tile_atlas[0][0]
        else:
            self.col = self.unit_turn
            self.image = self.select()

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.image, self.rect)

    def pos_unit(self, turn):
        """Позиция юнита"""
        if turn == 'right_down':
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_down':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_up':
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif turn == 'right_up':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif turn == 'right':
            self.point_x -= self.scroll_line
        elif turn == 'left':
            self.point_x += self.scroll_line
        elif turn == 'down':
            self.point_y -= self.scroll_line
        elif turn == 'up':
            self.point_y += self.scroll_line

        return self.point_x, self.point_y


    def select(self):
        """Заполнение"""
        if self.step == 7:
            self.row += 1
            self.step = 0
        self.step += self.speed
        if self.row >= 4:
            self.row = 1
        return self.tile_atlas[self.row][self.col]

    def filling(self):
        """Заполняет атлас"""
        atlas = self._atlas_
        size = (self.rate, self.rate)
        for row in range(atlas.get_height() // self.rate):
            self.tile_atlas.append([])
            for col in range(atlas.get_width() // self.rate):
                rect = (col * self.rate, row * self.rate)
                image = atlas.subsurface(rect, size)
                image = pg.transform.scale(image, (96, 96))
                self.tile_atlas[row].append(image)
        return self.tile_atlas