class Actions():

    def __init__(self, surface, player):
        self.surface = surface
        self.player = player


    def draw_player(self, surface):
        surface.fill((0, 0, 0))
        player = pygame.image.load("Trireme.png")
        self.speed = 1.2
        self.player_x = SCREEN_SIZE[0] / 2 - 25
        self.player_y = SCREEN_SIZE[1] - 75
        self.surface.blit(self.player, (self.player_x, self.player_y))
        pygame.display.flip()