

# 三方模块
import pygame
import pygame.freetype
import modules.config.viewCfg as viewCfgMd

# 项目模块
import modules.view.viewBase as viewBaseMd
import modules.view.label as LabelMd


# 输入框
class InputBox(LabelMd.Label):  
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, text_str = None, text_size = None, width = 50, height = 10, image_path = None):
        #调用父类的构函
        super().__init__(text_str, text_size, width, height, image_path)
        self.have_frame = True
        # 注册键盘事件
        self.set_keyboard_event(self, self.keyboard_fun)
        
    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj):
        if not self.show:
            return
        super().draw(view_obj)

    # 键盘事件
    def keyboard_fun(self, keyboard):
        new_dowm_map,new_up_map,now_dowm_map = keyboard.keyboard_event()
        for key in new_dowm_map:
            # 删除键
            if key == "\b":
                self.text_str = self.text_str[:-1]
            else:
                self.text_str += key