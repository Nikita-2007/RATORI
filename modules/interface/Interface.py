from modules.interface.MiniMap import MiniMap
from modules.interface.Life import Life
from modules.interface.Score import Score


'''Пример "Фасад"'''
class Interface(object):

    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.minimap = MiniMap(self.size)
        self.score = Score(size)
        self.life = Life()

    def update(self, size, hero):
        """Обновление"""
        self.minimap.update(hero)
        self.score.update(size)
        self.life.update()

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)
        self.score.draw(g)
        self.life.draw(g)