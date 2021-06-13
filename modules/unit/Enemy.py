import pygame as pg
import random as r


class Enemy(object):
    _atlas_ = pg.image.load("images\Enemy.png")
    _rate_ = 64

    def __init__(self, size):
        """Конструктор"""
        pg.init()
        self.size = size
        self.rate = self._rate_
        self.rect = pg.Rect(0, 0, self.rate, self.rate)
        self.tile_atlas = []
        self.enemy_start_point = (0, 0)
        self.tile_atlas = self.filling()
        self.row = 0
        self.col = 0
        self.step = 0
        self.speed = 1
        self.image = self.tile_atlas[self.row][self.col]
        self.random_target_x = 0
        self.random_target_y = 0

    def update(self, size):
        """Обновление"""
        self.select()

    def select(self):
        """Заполнение"""
        if self.step == 7:
            self.row += 1
            self.step = 0
        self.step += self.speed
        if self.row >= 4:
            self.row = 1

    def random_target(self, enemy_x, enemt_y, scrol_line, scrol):
        if (enemy_x+2463 > self.random_target_x) and (enemt_y > self.random_target_y):
            enemy_x -= scrol
            enemt_y -= scrol
        if (enemy_x+2463 > self.random_target_x) and (enemt_y+1803 < self.random_target_y):
            enemy_x -= scrol
            enemt_y += scrol
        if (enemy_x+2463 < self.random_target_x) and (enemt_y+1803 > self.random_target_y):
            enemy_x += scrol
            enemt_y -= scrol
        if (enemy_x+2463 < self.random_target_x) and (enemt_y+1803 < self.random_target_y):
            enemy_x += scrol
            enemt_y += scrol
        if (enemy_x == self.random_target_x) and (enemt_y == self.random_target_y):
            self.random_target_x = r.randint(100, 6000)
            self.random_target_y = r.randint(100, 4000)
        return enemy_x, enemt_y

    def draw(self, g):
        """Отрисовка"""
        self.image = self.tile_atlas[self.row][self.col]

        def select(self):
            """Заполнение"""
            if self.step == 7:
                self.row += 1
                self.step = 0
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
