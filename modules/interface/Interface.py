from modules.interface.MiniMap import MiniMap

class Interface(object):

    def __init__(self, size):
        """Конструктор"""
        self.minimap = MiniMap(size)

    def update(self, size):
        """Обновление"""
        self.minimap.update()

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)