# 系统模块

# 三方模块
import pygame
# 项目模块

# 热更模块
class HotUp():
    # 间隔时间
    space_time = 0
    # 上次更新时间
    last_time = 0

    def __init__(self):
        self.space_time = 0
        self.last_time = 0

    # 热更主函数
    @staticmethod
    def hot_up(self, parameter_list):
        pass