import pygame
from modules.Class1 import Class1

local_version = 1

class1 = Class1()
pygame.init()
g = pygame.display.set_mode((800, 600))
pygame.display.set_caption("RATORI")
icon = pygame.image.load("images\Start.png")
pygame.display.set_icon(icon)
game_misic = pygame.mixer.music.load("sounds\Музыка.mp3")
sound = pygame.mixer.Sound("sounds\click.wav")
game_state = True
image = pygame.image.load("images\Start.png")
font = pygame.font.SysFont("serif", 32)
msg = "Hi!"
text = font.render(msg, True, "black")

def game_cycle():
    pygame.mixer.music.play(-1)
    pygame.mixer.Sound.play(sound)

    while game_state:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        class1.draw(g)
        g.blit(text, (300, 400))
        g.blit(image, (50, 50))

        pygame.time.Clock().tick(60)
        pygame.display.update()