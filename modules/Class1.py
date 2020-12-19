import pygame

class Class1(object):
    def draw(self, g):
        g.fill('pink')

        # pygame.draw.line(g, 'yellow', (50, 50), (500, 100), 1)
        # pygame.draw.aaline(g, 'yellow', (50, 150), (500, 200), 1)
        # pygame.draw.line(g, 'red', (250, 50), (300, 200), 1)
        # pygame.draw.rect(g, 'blue', (100, 100, 300, 300), 2)
        # pygame.draw.arc(g, 'black', (100, 100, 300, 300), 1, 3, 1)
        pygame.draw.ellipse(g, (255, 255, 255), (200, 200, 400, 200), 100)
        pygame.draw.circle(g, 'blue', (400, 300), 100, 90)
        pygame.draw.circle(g, 'black', (400, 300), 100, 5)
        pygame.draw.ellipse(g, 'purple', (200, 200, 400, 200), 9)
        pygame.draw.circle(g, 'black', (400, 300), 30)
        pygame.draw.ellipse(g, (255, 255, 255), (380, 280, 10, 10))
        # pygame.draw.arc(g, "red", (50, 200, 100, 150), 3.14, 6.28, 3)
        # pygame.draw.lines(g, 'blue', ((100, 100), (200, 200), (100, 200)), 1)
        # pygame.draw.polygon(g, "blue", ((100, 200), (350, 400), (500, 600), (600, 500)), 1)