# 系统模块

# 三方模块
import pygame
# 项目模块
import modules.config.enum as EnumMd
import modules.control.instanceMgr as instanceMgrMd

# 键盘事件处理
class Keyboard():
    # 已按下的键
    down_list = {}

    # 初始化
    def __init__(self):
        self.down_list = {}

    # 键盘事件
    # type : 0:无操作, 1:点击左键, 2:左键弹起
    def keyboard_event(self):
        # 新按下的键
        new_dowm_map = {}
        # 新弹起的键
        new_up_map = {}
        # 在按下的键
        now_dowm_map = {}

        key_list = pygame.key.get_pressed()
        # ascii范围
        ascii_range = [32, 126]
        List = list(range(ascii_range[0], ascii_range[1])) + [8]
        for idx in List:
            # ascii转字符
            in_char = chr(idx)
            if idx == 8:
                in_char = "\b"
            # 按下的键
            if key_list[idx]:
                # 在按下的键
                now_dowm_map[in_char] = 1
                # 新按下的键
                if in_char not in self.down_list:
                    new_dowm_map[in_char] = 1
                self.down_list[in_char] = 1
            elif in_char in self.down_list:    # 弹起的键
                del self.down_list[in_char]
                new_up_map[in_char] = 1
        
        return new_dowm_map,new_up_map,now_dowm_map


