import sys
from random import randint
import pygame as pg
from modules.MiniMap import MiniMap

class Interface(object):

    def __init__(self, size):
        """Конструктор"""
        self.minimap = MiniMap(size)

    def update(self, size):
        """Обновление"""
        self.minimap.update(size)

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)