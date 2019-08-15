# 鼠标枚举
class MouseEnum():
    # 无操作
    click_free = 0
    # 点击左键
    click_down = 1
    # 左键弹起
    click_open = 2

    def __init__(self):
        self.click_free = 0
        self.click_down = 1
        self.click_open = 2
mouse_enum = MouseEnum()