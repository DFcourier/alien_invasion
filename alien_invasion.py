#使用sys模块里的工具来退出游戏
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        #初始化背景设置
        pygame.init()
        self.settings = Settings()

        #pygame.display.set_mode()创建一个显示窗口，游戏的所有元素都将在其中绘制
        #赋值给self.screen的对象是一个surface
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        #飞船实例
        self.ship = Ship(self)
        #存储子弹的编组
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        '''响应键盘和鼠标事件的事件循环'''
        #监听键盘和鼠标事件的事件循环
        for event in pygame.event.get():
            #如果按退出键,就退出游戏
            if event.type == pygame.QUIT: 
                sys.exit()
            #如果按下右方向键,设置飞船右移标志为True
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            #如果抬起右方向键,设置飞船右移标志为False
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''响应按下键盘'''
        #响应按下右方向键
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        #响应按下左方向键
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #响应按下空格键发射子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        #响应按下q退出游戏
        elif event.key == pygame.K_q:
            sys.exit()
 
    def _check_keyup_events(self,event):
        '''响应松开键盘'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''创建一颗子弹,并将其加入bullets编组中'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        '''更新子弹信息'''
        #更新子弹位置
        self.bullets.update()
        #删除消失的子弹
        self._remove_bullet()
 
    def _remove_bullet(self):
        '''如果子弹抵达屏幕顶端后,将其删除'''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
#        print('当前的子弹数:',len(self.bullets))

    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        #每次循环都要重新设置背景色绘制屏幕
        self.screen.fill(self.settings.bg_color)
        #调用shp.blitme()将飞船绘制在屏幕上
        self.ship.blitme()

        #绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        '''这个游戏由方法run_game()控制，开始游戏的主循环'''
        while True:
            self._check_events()
            #更新飞船位置
            self.ship.update()
            #更新子弹数据
            self.update_bullets()
            self._update_screen()  

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
