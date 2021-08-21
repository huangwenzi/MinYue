

# 三方模块
import pygame
import pygame.freetype
import modules.config.viewCfg as viewCfgMd


# 项目模块
import modules.view.viewBase as viewBaseMd

# label类
# 用于绘制文本
class Label(viewBaseMd.ViewBase):  
    # 文本
    text_str = "label"
    # 文本颜色
    text_colour = viewCfgMd.colour_black
    # 文字大小
    text_size = viewCfgMd.sys_font_size
    # 字体
    f1 = pygame.freetype.SysFont(viewCfgMd.sys_font, viewCfgMd.sys_font_size)
    
    
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, text_str = None, text_size = None, width = 0, height = 0, image_path = None):
        #调用父类的构函
        super().__init__(width, height, None)
        if text_str or text_str == "":
            self.text_str = text_str
        if text_size:
            self.text_size = text_size
        
    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj):
        # 父类绘制图片
        super().draw(view_obj)
        if self.text_str:
            # 取中间点
            abs_pos = self.get_abs_pos()
            text_str_size = len(self.text_str)*self.text_size
            middle_x = abs_pos[0] + (self.width - self.get_text_str_w()/2)/2
            middle_y = abs_pos[1] + (self.height - self.get_text_str_h()/2)/2
            self.f1.render_to(view_obj, (middle_x, middle_y), self.text_str, fgcolor = self.text_colour, size = self.text_size)
        # abs_pos = self.get_abs_pos()
        # self.f1.render_to(view_obj, abs_pos, self.text_str, fgcolor = self.text_colour, size = self.size)
    
    
    # 设置文本
    def set_text_str(self, text_str):
        self.text_str = text_str
    # 设置字体
    def set_font(self, font):
        self.f1 = pygame.freetype.SysFont(font, self.text_size)
    # 设置颜色
    def set_colour(self, colour):
        self.text_colour = colour
    # 获取文本长度
    def get_text_str_w(self):
        # 中文占两个位置
        if not self.text_str:
            return 0
        str_len = 0
        for ch in self.text_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                str_len += 2
            else:
                str_len += 1
        return str_len * self.text_size
    # 获取文本高度
    def get_text_str_h(self):
        for ch in self.text_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return 2 * self.text_size
        return self.text_size
        