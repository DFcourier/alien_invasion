import sys
import pygame

class BlueBackground:
    '''创建一个蓝色背景的窗口'''
    def __init__(self):
        pygame.init()
        
        #定义窗口参数
        self.screen = pygame.display.set_mode((500,500))
        self.bg_color = (0,43,54)

        #得到窗口rect
        self.screen_rect = self.screen.get_rect()
        #得到图像surface和图像rect
        self.image = pygame.image.load('1.bmp')
        self.image_rect = self.image.get_rect()

        self.image_rect.center = self.screen_rect.center

    def display(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #绘制窗口
            pygame.display.flip()
            self.screen.fill(self.bg_color)

            #绘制图像
            self.screen.blit(self.image,self.image_rect)


if __name__ == '__main__':
    bg = BlueBackground()
    bg.display()
