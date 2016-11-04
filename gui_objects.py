import pygame
from pygame.locals import *


class GuiObjects():

    def __init__(self):
        pygame.init()

    def start_text(self, surface):
        myfont = pygame.font.Font(None, 15)
        label = myfont.render(
            "Press ENTER to start game", 1, (255, 255, 0)
        )
        surface.blit(label, (100, 100))
        pygame.display.flip()