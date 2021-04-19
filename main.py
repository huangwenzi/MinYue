# 系统模块
import time
import sys

# 三方模块
import pygame

# 项目模块
import modules.view.mainView as mainViewMd

# 开始运行文件
def run():
    # 初始化一个界面类
    mainView = mainViewMd.MainView("modules\\resource\\mainView.png")
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        # 界面绘制
        mainView.draw(mainView)

run()