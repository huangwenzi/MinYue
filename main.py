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
    mainView = mainViewMd.MainView()

    while True:

        # 界面绘制
        mainView.draw()

run()