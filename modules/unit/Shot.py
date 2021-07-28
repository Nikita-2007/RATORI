import pygame as pg
from modules.unit.Abstract import Abstract


class Shot(Abstract):
    def __init__(self, size, turn):
        """Конструктор"""
        self.turn_shot = turn
        self.size = size
        self.point_x, self.point_y = self.size[0] // 2 + 25, self.size[1] // 2 + 25
        self.unit_turn = 8
        self.sound_reload = pg.mixer.Sound("sounds\Reload.mp3")
        self.sound_shots = pg.mixer.Sound("sounds\Shots.mp3")
        self.sound_shots2 = pg.mixer.Sound("sounds\Shots2.mp3")
        self.bullets = 7
        self.step = 0
        self.font = pg.font.Font(None, 36)
        self.text = self.font.render(str(self.bullets), True, 'Black')
        self.time_del = 210

    def update(self, turn):
        """Обновление"""
        self.pos_unit(turn)
        self.BAM()

    def BAM(self):
        """Позиция юнита"""
        if self.turn_shot == 'right_down':
            self.point_x += self.scroll*2
            self.point_y += self.scroll*2
        elif self.turn_shot == 'left_down':
            self.point_x -= self.scroll*2
            self.point_y += self.scroll*2
        elif self.turn_shot == 'left_up':
            self.point_x -= self.scroll*2
            self.point_y -= self.scroll*2
        elif self.turn_shot == 'right_up':
            self.point_x += self.scroll*2
            self.point_y -= self.scroll*2
        elif self.turn_shot == 'right' or self.turn_shot == 'stop':
            self.point_x += self.scroll_line*2
        elif self.turn_shot == 'left':
            self.point_x -= self.scroll_line*2
        elif self.turn_shot == 'down':
            self.point_y += self.scroll_line*2
        elif self.turn_shot == 'up':
            self.point_y -= self.scroll_line*2

        return self.point_x, self.point_y

    def draw(self, g):
        """Отрисовка"""
        pg.draw.circle(g, 'Orange', (self.point_x, self.point_y), 4)
        g.blit(self.text, (self.size[0] - 100, self.size[1] - 50))

    def Shot(self):
        self.step = 0
        if self.bullets > 0:
            pg.mixer.Sound.play(self.sound_shots)
            self.bullets -= 1
            self.BAM()
        else:
            pg.mixer.Sound.play(self.sound_shots2)
            self.bullets = 0
        return self.bullets

    def Reload(self):
        self.step = 0
        self.bullets = 7
        self.update(self.size)

    def __del__(self):
        pass
