import pygame as pg
from modules.Menu import Menu
from modules.Game import Game

class Main(object):

    #БАЗОВЫЙ ЗАПУСК
    def __init__(self):
        self.local_version = 1
        self.flag = pg.RESIZABLE
        self.size = self.width, self.hiegth = 1280, 720
        self.fps = 60
        self.menu_state = True

        pg.display.set_mode((self.width, self.hiegth), self.flag)
        icon = pg.image.load("images\exit.png")
        pg.display.set_icon(icon)
        pg.display.set_caption("RATORI")

    #Новая игра
    def game_start(self):
        self.menu = Menu(self.size)
        self.game = Game()
        self.game_state = True
        self.game_cycle()

    #Игровой цикл
    def game_cycle(self):
        g = pg.display.get_surface()


        while self.game_state:
            #СОБЫТИЯ
            for e in pg.event.get():
                #Выход из игры
                if e.type == pg.QUIT:
                    pg.quit()
                    quit()
                if e.type == pg.KEYDOWN and e.key == pg.K_F11:
                    if g.get_flags() & pg.FULLSCREEN:
                        self.flag = pg.RESIZABLE
                    else:
                        self.flag = pg.FULLSCREEN
                    pg.display.set_mode((self.width, self.hiegth), self.flag)
                #Меню/игра
                if e.type == pg.KEYUP and e.key == pg.K_ESCAPE:
                    self.menu_state = not self.menu_state

            if self.menu_state == True:
                self.menu.update(e)
            else:
                self.game.update(e)

            #Обновление меню
            if self.menu_state:
                self.menu.draw(g)
            #Обновление игры
            else:
                self.game.draw(g)

            pg.time.Clock().tick(self.fps)
            pg.display.flip()