import sys
from random import randint
import pygame as pg

class Interface(object):

    def __init__(self):
        """Конструктор"""

    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        """Отрисовка"""
        pg.draw.rect(g, 'pink', (0, 480, 720, 426))