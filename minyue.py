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

    # 设置容器包含父子结构
    mainViewMd.MainView.add_son_view(mainView, viewVessel)
    viewVesselMd.viewVessel.add_son_view(viewVessel, viewBase)

    # 设置偏移
    viewVesselMd.viewVessel.setPos(viewVessel, 5,5)
    viewBaseMd.viewBase.setPos(viewBase, 5,5)
    
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
        # 界面绘制
        mainViewMd.MainView.draw(mainView)
        # time.sleep(1)
        # 处理鼠标事件
        # imageMgr.mouse_event()
        # 检查热更


run()