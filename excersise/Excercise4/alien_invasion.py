import sys
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船所发射的子弹的类'''
    def __init__(self,ai_game):
        '''在飞船当前位置创建一个子弹对象'''
        super().__init__()

        #设置子弹属性
        self.bullet_speed = 1.0 
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.screen = ai_game.screen

        #在(0,0)处创建一个表示子弹的矩形,再设置到正确的位置:飞船的右中央
        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.rect.midleft = ai_game.image_rect.midright

    def update(self):
        '''向右移动子弹'''
        self.rect.x += self.bullet_speed

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)

class Move:
    '''上下左右移动飞机,且不超过边界'''
    def __init__(self):
        pygame.init()

        self.bg_color = (230,230,230)

        #设置屏幕属性
        self.screen = pygame.display.set_mode((1500,600))
        self.screen_rect = self.screen.get_rect()

        #设置飞船图像属性
        self.image = pygame.image.load('../images/ship.bmp')
        #旋转图像 
        self.image = pygame.transform.rotate(self.image,270)
        self.image_rect = self.image.get_rect()
        self.image_rect.midleft = self.screen_rect.midleft

        #设置飞船移动标志
        self.ship_moving_up = False
        self.ship_moving_down = False
        self.ship_moving_left = False
        self.ship_moving_right = False

        #创建存储子弹的编组
        self.bullets = pygame.sprite.Group()

    def check_events(self):
        '''响应键盘事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_UP:
            self.ship_moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship_moving_down = True
        if event.key == pygame.K_LEFT:
            self.ship_moving_left = True
        if event.key == pygame.K_RIGHT:
            self.ship_moving_right = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_UP:
            self.ship_moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship_moving_down = False
        if event.key == pygame.K_LEFT:
            self.ship_moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship_moving_right = False

    def _fire_bullet(self):
        '''发射子弹方法'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def remove_bullet(self):
        '''删除消失的子弹'''
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def update_ship(self):
        '''更新飞船位置信息'''
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
            #响应键盘事件
            self.check_events()
            #更新飞船位置信息
            self.update_ship()
            #更新子弹位置信息
            self.bullets.update()
            #删除消失的子弹
            self.remove_bullet()
            #填充背景色
            self.screen.fill(self.bg_color)
            #绘制飞船
            self.screen.blit(self.image,self.image_rect)
            #绘制子弹
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            #显示画面
            pygame.display.flip()

m = Move()
m.run()
