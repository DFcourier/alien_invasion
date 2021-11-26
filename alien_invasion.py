#使用sys模块里的工具来退出游戏
import sys
import pygame
from settings import Settings
from ship import Ship

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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
 
    def _check_keyup_events(self,event):
        '''响应松开键盘'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


 
    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        #每次循环都要重新设置背景色绘制屏幕
        self.screen.fill(self.settings.bg_color)
        #调用shp.blitme()将飞船绘制在屏幕上
        self.ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()




    def run_game(self):
        '''这个游戏由方法run_game()控制，开始游戏的主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()  

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
