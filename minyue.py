# 系统模块
import sys

# 三方模块
import pygame
import pygame.freetype

pygame.init()
# pygame.freetype.init()

# 项目模块
# 游戏引擎模块
import modules.view.mainView as mainViewMd
# import modules.control.hotUp as hotUpMd
import modules.control.mouse as mouseMd
import modules.config.enum as mouseEnumMd
import modules.tool.time_tool as TimeToolMd


# 组件游戏模块
import qinShi.view.mainView as QSmainViewMd
import qinShi.control.cfgMgr as CfgMgrMd
cfg_mgr = CfgMgrMd.getInstance()
import qinShi.control.player as playerMd
player = playerMd.getInstance()

# 开始运行文件
def run():
    # 初始化界面功能
    qs_main_view = QSmainViewMd.getInstance()
    mouse = mouseMd.Mouse()
    # 初始化数据



    # 游戏循环
    qs_main_view.run()



run()