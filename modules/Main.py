import pygame

class Main(object):
    local_version = 1

    pygame.init()
    g = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("RATORI")
    icon = pygame.image.load("images\Start.png")
    pygame.display.set_icon(icon)
    game_state = True

    def game_cycle(self):
        while self.game_state:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.time.Clock().tick(60)
            pygame.display.update()