import pygame as pg
from modules.Menu import Menu
from modules.Game import Game

class Main(object):

    #БАЗОВЫЙ ЗАПУСК
    def __init__(self):
        self.local_version = 1
        self.width = 1280
        self.hiegth = 720
        self.fps = 60
        self.menu_state = True

        pg.display.set_mode((self.width, self.hiegth))
        icon = pg.image.load("images\exit.png")
        pg.display.set_icon(icon)
        pg.display.set_caption("RATORI")

    #Новая игра
    def game_start(self):
        self.menu = Menu()
        self.game = Game()
        self.game_state = True
        self.game_cycle()

    #Игровой цикл
    def game_cycle(self):
        g = pg.display.get_surface()

        while self.game_state:
            for e in pg.event.get():
                #Выход из игры
                if e.type == pg.QUIT:
                    pg.quit()
                    quit()
                #Меню/игра
                if e.type == pg.KEYUP and e.key == pg.K_ESCAPE:
                    self.menu_state = not self.menu_state

            #Обновление меню
            if self.menu_state:
                self.menu.draw(g)
            #Обновление игры
            else:
                self.game.draw(g)

            pg.time.Clock().tick(self.fps)
            pg.display.update()