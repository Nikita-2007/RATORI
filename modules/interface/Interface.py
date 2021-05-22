from modules.interface.MiniMap import MiniMap
from modules.interface.Bullet import Bullet
class Interface(object):

    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.minimap = MiniMap(self.size)
        self.bullet = Bullet(self.size)

    def update(self, size, hero):
        """Обновление"""
        self.minimap.update(hero)
        self.bullet.update(size)

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)
        self.bullet.draw(g)