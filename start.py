from sys import exit

import pygame
from pygame.locals import *
from  gui_objects import GuiObjects

SCREEN_SIZE = (800, 600)


class SpaceInvadersGame(object):
    player_x = SCREEN_SIZE[0] / 2 - 25
    player_y = SCREEN_SIZE[1] - 75
    event_num = 0

    def __init__(self):
        self.gui_obj = GuiObjects()
        pygame.init()
        flag = DOUBLEBUF
        self.surface = pygame.display.set_mode(SCREEN_SIZE, flag)
        self.gamestate = 1
        self.surface.fill((0, 0, 0))
        self.set_start_info()
        self.ship_action()
        self.loop()

    def set_start_info(self):
        myfont = pygame.font.Font(None, 15)
        label = myfont.render(
            "Press ENTER to start game", 1, (255, 255, 0)
        )
        self.surface.blit(label, (100, 100))
        pygame.display.flip()

    def clear_screen(self):
        self.surface.fill((0, 0, 0))

    def draw_player(self):
        self.clear_screen()
        self.player = pygame.image.load('Trireme.png')
        self.surface.blit(self.player, (self.player_x, self.player_y))
        pygame.display.flip()
        print('new_player', self.player_x, self.player_y)

    def move_left(self):
        self.player_x = self.player_x - 100
        if self.player_x < 0:
            self.player_x = 0

    def move_right(self):
        self.player_x = self.player_x + 100
        if self.player_x > SCREEN_SIZE[0]:
            self.player_x = SCREEN_SIZE[0] - 50

    def ship_action(self):
        while True:
            event = pygame.event.wait()
            if event.type == KEYDOWN and event.key == K_LEFT:
                self.move_left()
                self.gamestate = 1
            elif event.type == KEYDOWN and event.key == K_RETURN:
                self.draw_player()
                self.gamestate = 1
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.move_right()
                self.gamestate = 1
            elif (event.type == QUIT or
                  (event.type == KEYDOWN and event.key == K_ESCAPE)
                  ):
                exit()
            self.draw_player()

    def game_exit(self):
        """ funkcja przerywa dzialanie gry i wychodzi do systemu"""
        exit()

    def loop(self):
        """ glowna petla gry """
        while self.gamestate == 1:
           for event in pygame.event.get():
               if (event.type == QUIT or
                   (event.type == KEYDOWN and event.key == K_ESCAPE)
               ):
                   self.gamestate = 0
        self.game_exit()



if __name__ == '__main__':
   SpaceInvadersGame()