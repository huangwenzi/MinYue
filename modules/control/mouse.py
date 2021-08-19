# 系统模块

# 三方模块
import pygame
# 项目模块
import modules.config.enum as mouseEnumMd
import modules.control.instanceMgr as instanceMgrMd


# 鼠标事件的返回
class MouseState():
    x = 0
    y = 0
    last_down_x = 0
    last_down_y = 0
    def __init__(self):
        self.type = mouseEnumMd.mouse_click_free
        self.x = 0
        self.y = 0
        self.last_down_x = 0
        self.last_down_y = 0

# 鼠标事件处理
class Mouse():
    # 左键是否置位
    left_set = False
    # 右键是否置位
    right_set = False
    # 上次点击的位置
    last_down_x = 0
    last_down_y = 0

    # 初始化
    def __init__(self):
        self.left_set = False   # 左键是否置位
        self.right_set = False  # 右键是否置位

    # 鼠标事件
    # type : 0:无操作, 1:点击左键, 2:左键弹起
    def mouse_event(self):
        pressde = pygame.mouse.get_pressed()    # 获取鼠标按下信息
        position = pygame.mouse.get_pos()       # 获取鼠标位置
        ret = MouseState()
        ret.x = position[0]
        ret.y = position[1]
        if pressde[0]:
            # 鼠标点下
            if self.left_set == False:
                self.left_set = True
                ret.type = mouseEnumMd.mouse_click_down
                self.last_down_x = position[0]
                self.last_down_y = position[1]
            elif self.last_down_x != position[0] or self.last_down_y != position[1]:
                # 鼠标拖动
                ret.type = mouseEnumMd.mouse_click_drag
                ret.last_down_x = self.last_down_x
                ret.last_down_y = self.last_down_y
                self.last_down_x = position[0]
                self.last_down_y = position[1]
        elif pressde[0] == 0 and self.left_set == True:
            # 鼠标弹起
            self.left_set = False
            ret.type = mouseEnumMd.mouse_click_open
        return ret

