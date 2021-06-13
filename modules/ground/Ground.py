from modules.ground.Terrain import Terrain
from modules.unit.Enemy import Enemy
import pygame as pg


class Ground(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.terrain = Terrain()
        self.enemy = Enemy(self.size)
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()
        self.point_x, self.point_y = self.terrain.start_point
        self.enemy_x, self.enemy_y = self.enemy.enemy_start_point
        self.max_x = len(self.terrain.map[0]) * self.terrain.rate
        self.max_y = len(self.terrain.map) * self.terrain.rate
        self.raz_hero_x = 0
        self.raz_hero_y = 0
        # шрифт для кода
        pg.font.init()
        self.font = pg.font.SysFont('arial', 12, True)

    def update(self, size, turn, g):
        """Обновление"""
        scrol_line = 30
        scrol = round(scrol_line / 1.4)

        if turn == 'right_down':
            self.point_x += scrol
            self.point_y += scrol
            self.enemy_x -= scrol
            self.enemy_y -= scrol
        elif turn == 'left_down':
            self.point_x -= scrol
            self.point_y += scrol
            self.enemy_x += scrol
            self.enemy_y -= scrol
        elif turn == 'left_up':
            self.point_x -= scrol
            self.point_y -= scrol
            self.enemy_x += scrol
            self.enemy_y += scrol
        elif turn == 'right_up':
            self.point_x += scrol
            self.point_y -= scrol
            self.enemy_x -= scrol
            self.enemy_y += scrol
        elif turn == 'right':
            self.point_x += scrol_line
            self.enemy_x -= scrol_line
        elif turn == 'left':
            self.point_x -= scrol_line
            self.enemy_x += scrol_line
        elif turn == 'down':
            self.point_y += scrol_line
            self.enemy_y -= scrol_line
        elif turn == 'up':
            self.point_y -= scrol_line
            self.enemy_y += scrol_line
            pg.draw.rect(g, 'Red', (500, self.point_y, 550, 2000))
        # Разница между спавном персонажёём и его кординатами
        if self.terrain.start_point[0] > self.point_x:
            self.raz_hero_x = self.terrain.start_point[0] - self.point_x
        if self.terrain.start_point[0] < self.point_x:
            self.raz_hero_x = self.point_x - self.terrain.start_point[0]
        if self.terrain.start_point[1] > self.point_y:
            self.raz_hero_y = self.terrain.start_point[0] - self.point_y
        if self.terrain.start_point[1] < self.point_y:
            self.raz_hero_y = self.point_y - self.terrain.start_point[0]

        # self.enemy_x, self.enemy_y = self.enemy.random_target(self.enemy_x, self.enemy_y, scrol_line, scrol)
        print(self.point_x, self.point_x)
        print(self.enemy_x + 2463 - self.raz_hero_x, self.enemy_y + 1803 + self.raz_hero_y)

        # Ограничение крайв
        if self.point_x < size[0] // 2 + scrol_line:
            self.point_x = size[0] // 2 + scrol_line
        if self.point_x > self.max_x - size[0] // 2 - scrol_line:
            self.point_x = self.max_x - size[0] // 2 - scrol_line
        if self.point_y < size[1] // 2 + scrol_line:
            self.point_y = size[1] // 2 + scrol_line
        if self.point_y > self.max_y - size[1] // 2 - scrol_line:
            self.point_y = self.max_y - size[1] // 2 - scrol_line
        self.select()

    def draw(self, g):
        """Отрисовка"""
        g.fill('darkgreen')
        g.blit(self.surface, self.rect)
        g.blit(self.enemy.image, (self.enemy_x, self.enemy_y))

    def select(self):
        """Отрисовка Groud"""
        rate = self.terrain.rate
        # граница окна
        x_left = self.point_x - self.size[0] // 2
        x_right = x_left + self.size[0]
        y_top = self.point_y - self.size[0] // 2
        y_bottom = y_top + self.size[1]
        for y in range(y_top // rate, y_bottom // rate + 1):
            for x in range(x_left // rate, x_right // rate + 1):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                self.surface.blit(tile, (x * rate - x_left, y * rate - y_top, rate, rate))
                # коды tileоф
                text = self.font.render((str(y) + '-' + str(x)), True, 'red')
                text_rect = text.get_rect()
                # self.surface.blit(text, (x * rate - x_left + 4, y * rate - y_top + 16), text_rect)
