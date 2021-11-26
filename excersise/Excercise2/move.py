import sys
import pygame

class Move:
    '''上下左右移动飞机,且不超过边界'''
    def __init__(self):
        pygame.init()

        self.bg_color = (230,230,230)

        self.screen = pygame.display.set_mode((500,500))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('../images/ship.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

        self.ship_moving_up = False
        self.ship_moving_down = False
        self.ship_moving_left = False
        self.ship_moving_right = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
        self.update()

    def _check_keydown_events(self,event):
        if event.key == pygame.K_UP:
            self.ship_moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship_moving_down = True
        if event.key == pygame.K_LEFT:
            self.ship_moving_left = True
        if event.key == pygame.K_RIGHT:
            self.ship_moving_right = True

    def _check_keyup_events(self,event):
        if event.key == pygame.K_UP:
            self.ship_moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship_moving_down = False
        if event.key == pygame.K_LEFT:
            self.ship_moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship_moving_right = False

    def update(self):
        if self.ship_moving_up and self.image_rect.top > 0:
            self.image_rect.y -= 1
        if self.ship_moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += 1
        if self.ship_moving_left and self.image_rect.left > 0:
            self.image_rect.x -= 1
        if self.ship_moving_right and self.image_rect.right < self.screen_rect.bottom:
            self.image_rect.x += 1

    def run(self):
        while True:
            self.check_events()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.image,self.image_rect)
            pygame.display.flip()

m = Move()
m.run()
