from modules.ground.Terrain import Terrain

class Ground(object):
    def __init__(self):
        """Конструктор"""
        self.terrain = Terrain()

    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        """Отрисовка"""
        g.fill('darkgreen')
        for y in range(10):
            for x in range(25):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                g.blit(tile, (x*48, y*48))
