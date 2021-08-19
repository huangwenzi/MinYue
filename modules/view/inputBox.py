

# 三方模块
import pygame
import pygame.freetype
import modules.config.viewCfg as viewCfgMd

# 项目模块
import modules.view.viewBase as viewBaseMd



# 输入框
class InputBox(viewBaseMd.ViewBase):  
    # 文本
    text = ""
    # 文本颜色
    text_colour = viewCfgMd.sys_font_text_colour
    # 文字大小
    size = viewCfgMd.sys_font_size
    # 字体
    f1 = pygame.freetype.SysFont(viewCfgMd.sys_font, viewCfgMd.sys_font_size)
    
    # 图形
    # 矩形边缘宽度
    rect_width = viewCfgMd.input_box_rect_width
    
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, text = None, size = None, width = 0, height = 0):
        #调用父类的构函
        super().__init__(None)
        if text:
            self.text = text
        if size:
            self.size = size
        self.width = width
        self.height = height
        # 注册键盘事件
        self.set_keyboard_event(self, self.keyboard_fun)
        
    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj, pos):
        if not self.show:
            return
        # 绘制文本
        x = self.x + pos[0]
        y = self.y + pos[1]
        if self.text:
            # 取中间点
            middle_x = x + (self.width - (len(self.text)*self.size)/2)/2
            middle_y = y + (self.height - self.size)/2
            self.f1.render_to(view_obj, (middle_x, middle_y), self.text, fgcolor = self.text_colour, size = self.size)
        # 绘制边缘
        pygame.draw.rect(view_obj, self.text_colour, (x, y, self.width, self.height), self.rect_width)
        
    # 点击事件用父类的
    
    
    # 设置文本
    def set_text(self, text):
        self.text = text
    # 设置字体
    def set_font(self, font):
        self.f1 = pygame.freetype.SysFont(font, self.size)
    # 设置颜色
    def set_colour(self, colour):
        self.text_colour = colour

    # 键盘事件
    def keyboard_fun(self, keyboard):
        new_dowm_map,new_up_map,now_dowm_map = keyboard.keyboard_event()
        for key in new_dowm_map:
            # 删除键
            if key == "\b":
                self.text = self.text[:-1]
            else:
                self.text += key