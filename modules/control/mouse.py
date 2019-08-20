# 系统模块

# 三方模块
import pygame
# 项目模块
from modules.config.enum import mouse_enum
import modules.control.instanceMgr as instanceMgrMd

# 鼠标事件的返回
class Postion():
    def __init__(self):
        self.type = mouse_enum.click_free
        self.x = 0
        self.y = 0

# 鼠标事件处理
class Mouse():
    # 左键是否置位
    left_set = False
    # 右键是否置位
    right_set = False

    # 初始化
    def __init__(self):
        self.left_set = False   # 左键是否置位
        self.right_set = False  # 右键是否置位
    
    # 获取单例
    @staticmethod
    def getInstance():
        name = "Mouse"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = Mouse()
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins

    # 鼠标事件
    # type : 0:无操作, 1:点击左键, 2:左键弹起
    @staticmethod
    def mouse_event():
        ins = Mouse.getInstance()
        pressde = pygame.mouse.get_pressed()    # 获取鼠标按下信息
        position = pygame.mouse.get_pos()       # 获取鼠标位置
        ret = Postion()
        ret.x = position[0]
        ret.y = position[1]
        if pressde[0]:
            ins.left_set = True
            ret.type = mouse_enum.click_down
        elif pressde[0] == 0 and ins.left_set == True:
            ins.left_set = False
            ret.type = mouse_enum.click_open
        return ret
