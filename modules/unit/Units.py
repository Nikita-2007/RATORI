from modules.unit.Gangster import Gangster
from modules.unit.Сivil import Сivil
from modules.unit.Cat import Cat
from modules.unit.Adapter import Adapter

class Units(object):

    def __init__(self, size):
        """Конструктор"""
        tile_atlas_Gangster = Gangster.filling()
        tile_atlas_Сivil = Сivil.filling()
        tile_atlas_Сat = Cat.filling()
        tile_atlas_Dog = Adapter.filling()
        self.size = size
        self.list_unit = []
        self.count = 50
        for i in range(self.count):
            unit = Gangster(self.size, tile_atlas_Gangster)
            self.list_unit.append(unit)
        for i in range(self.count):
            unit = Сivil(self.size, tile_atlas_Сivil)
            self.list_unit.append(unit)
        for i in range(self.count):
            unit = Cat(self.size, tile_atlas_Сat)
            self.list_unit.append(unit)
        for i in range(self.count):
            unit = Adapter(self.size, tile_atlas_Dog)
            self.list_unit.append(unit)
        self.unit_speed_line = 2
        self.unit_speed = round(self.unit_speed_line / 1.4)

    def update(self, turn):
        """Обновление"""
        for unit in self.list_unit:
            self.move_unit(unit)
            unit.update(turn)

    def draw(self, g):
        """Отрисовка"""
        for unit in self.list_unit:
            unit.draw(g)

    def move_unit(self, unit):
        """Позиция юнита"""
        if unit.unit_turn == 0:
            unit.point_y += self.unit_speed_line
        elif unit.unit_turn == 1:
            unit.point_x += self.unit_speed
            unit.point_y += self.unit_speed
        elif unit.unit_turn == 2:
            unit.point_x += self.unit_speed_line
        elif unit.unit_turn == 3:
            unit.point_x += self.unit_speed
            unit.point_y -= self.unit_speed
        elif unit.unit_turn == 4:
            unit.point_y -= self.unit_speed_line
        elif unit.unit_turn == 5:
            unit.point_x -= self.unit_speed
            unit.point_y -= self.unit_speed
        elif unit.unit_turn == 6:
            unit.point_x -= self.unit_speed_line
        elif unit.unit_turn == 7:
            unit.point_x -= self.unit_speed
            unit.point_y += self.unit_speed
        return unit.point_x, unit.point_y