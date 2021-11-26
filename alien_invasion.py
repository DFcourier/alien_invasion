#使用sys模块里的工具来退出游戏
import sys
import pygame

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        #初始化背景设置
        pygame.init()

        #pygame.display.set_mode()创建一个显示窗口，游戏的所有元素都将在其中绘制
        #赋值给self.screen的对象是一个surface
        self.screen = pygame.display.set_mode((1200,800))

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        '''这个游戏由方法run_game()控制，开始游戏的主循环'''
        while True:
            #监听键盘和鼠标事件的事件循环
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
