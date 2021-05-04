from modules.ground.Terrain import Terrain
import pygame as pg


class Ground(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.terrain = Terrain()
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()
        self.point_x, self.point_y = self.terrain.start_point
        # шрифт для кода
        pg.font.init()
        self.font = pg.font.SysFont('arial', 12, True)

    def update(self, size, turn):
        """Обновление"""
        self.select()
        scrol = 5
        if turn == 'right_down':
            self.point_x += scrol
            self.point_y += scrol
        elif turn == 'left_down':
            self.point_x -= scrol
            self.point_y += scrol
        elif turn == 'left_up':
            self.point_x -= scrol
            self.point_y -= scrol
        elif turn == 'right_up':
            self.point_x += scrol
            self.point_y -= scrol
        elif turn == 'right':
            self.point_x += scrol
        elif turn == 'left':
            self.point_x -= scrol
        elif turn == 'down':
            self.point_y += scrol
        elif turn == 'up':
            self.point_y -= scrol


    def draw(self, g):
        """Отрисовка"""
        g.fill('darkgreen')
        g.blit(self.surface, self.rect)

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
                #self.surface.blit(text, (x * rate - x_left + 4, y * rate - y_top + 16), text_rect)