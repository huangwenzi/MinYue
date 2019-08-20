# 系统模块
import time
import sys

# 三方模块
import pygame

# 项目模块
import modules.view.mainView as mainViewMd
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.hotUp as hotUpMd
import modules.control.mouse as mouseMd
from modules.config.enum import mouse_enum
import qinShi.view.mainView as QSmainViewMd

# 开始运行文件
def run():
    # # 初始化一个界面类
    # mainView = mainViewMd.MainView('modules/resource/mainView.png')
    # viewVessel = viewVesselMd.viewVessel('modules/resource/viewVessel.png')
    # viewBase = viewBaseMd.viewBase('modules/resource/viewBase.png')

    # # 设置容器包含父子结构
    # mainViewMd.MainView.add_son_view(mainView, viewVessel)
    # viewVesselMd.viewVessel.add_son_view(viewVessel, viewBase)

    # # 设置偏移
    # viewVesselMd.viewVessel.setPos(viewVessel, 5,5)
    # viewBaseMd.viewBase.setPos(viewBase, 5,5)



    # 创建基础界面
    mainView = mainViewMd.MainView('qinShi/resource/screen/0.jpg')
    # 初始化界面功能
    QSmainView = QSmainViewMd.MainView(mainView)


    # 游戏循环
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
        # 界面绘制
        # mainViewMd.MainView.draw(mainView)
        QSmainView.main_view.draw(QSmainView.main_view)

        # 处理鼠标事件
        ret_mouse = mouseMd.Mouse.mouse_event()
        if ret_mouse.type == mouse_enum.click_open:
            click_ret = QSmainView.main_view.check_click(QSmainView.main_view, ret_mouse, [0,0])
            if click_ret.click_func:
                click_ret.click_func()

        # 检查热更


run()