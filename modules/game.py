import pygame

local_version = 1

pygame.init()
g = pygame.display.set_mode((800, 600))
pygame.display.set_caption("RATORI")
#icon = pygame.image.load("RATORI\images\icon.ico")
#pygame.display.set_icon(icon)

game_state = True

def game_cycle():
    while game_state:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        g.fill('pink')
        #pygame.draw.line(g, 'yellow', (50, 50), (500, 100), 1)
        #pygame.draw.aaline(g, 'yellow', (50, 150), (500, 200), 1)
        #pygame.draw.line(g, 'red', (250, 50), (300, 200), 1)
        #pygame.draw.rect(g, 'blue', (100, 100, 300, 300), 2)
        # pygame.draw.arc(g, 'black', (100, 100, 300, 300), 1, 3, 1)
        pygame.draw.ellipse(g, (255, 255 ,255), (200, 200, 400, 200), 100)
        pygame.draw.circle(g, 'blue', (400, 300), 100, 90)
        pygame.draw.circle(g, 'black', (400, 300), 100, 5)
        pygame.draw.ellipse(g, 'purple', (200, 200, 400, 200), 9)
        pygame.draw.circle(g, 'black', (400, 300), 30)
        pygame.draw.ellipse(g, (255, 255 ,255), (380, 280, 10, 10))

        pygame.time.Clock().tick(60)
        pygame.display.update()