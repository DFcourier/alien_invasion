import sys
import pygame

class Print:
    '''运行一个空窗口,按下键盘,查看输出'''
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((500,500))


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                
    def run(self):
        while True:
            self.check_events()

            pygame.display.flip()


p = Print()
p.run()

