# 系统模块

# 三方模块
import pygame
import pygame.freetype

pygame.init()


# 组件游戏模块
import jxgame.a_star.main_view as AStarMd


# 开始运行文件
def run():
    # 创建基础界面
    main_view = AStarMd.getInstance()
    # 初始化数据

    # 游戏进入循环
    main_view.run()

        



run()