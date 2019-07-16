# 系统模块
import time
import sys

# 三方模块
import pygame

# 项目模块
import modules.view.mainView as mainViewMd
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd


# 开始运行文件
def run():
    # 初始化一个界面类
    mainView = mainViewMd.MainView('modules/resource/mainView.png')
    viewVessel = viewVesselMd.viewVessel('modules/resource/viewVessel.png')
    viewBase = viewBaseMd.viewBase('modules/resource/viewBase.png')

    mainView.add_son_view(viewVessel)
    viewVessel.add_son_view(viewBase)

    
    while True:
        # 界面绘制
        mainView.draw()
        print(1)
        time.sleep(1)

run()