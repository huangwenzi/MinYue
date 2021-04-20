

# 三方模块
import pygame
import pygame.freetype
import modules.config.viewCfg as viewCfgMd




# label类
# 用于绘制文本
class Label():  
    # 相对父窗口左上角偏移
    x = 0   
    y = 0
    # 是否显示
    show = True
    
    # 文本
    text = "label"
    # 文本颜色
    text_colour = viewCfgMd.sys_font_text_colour
    # 文字大小
    size = viewCfgMd.sys_font_size
    # 字体
    f1 = pygame.freetype.SysFont(viewCfgMd.sys_font, viewCfgMd.sys_font_size)
    
    
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, text = None, size = None):
        if text:
            self.text = text
        if size:
            self.size = size
        
    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj, pos):
        if not self.show:
            return
        x = self.x + pos[0]
        y = self.y + pos[1]
        self.f1.render_to(view_obj, (x, y), self.text, fgcolor = self.text_colour, size = self.size)
        
    # 检查是否在鼠标点击范围内
    # 兼容图像点击检查
    def check_click(self, click_pos, father_pos):
        return None
    
    
    # 设置文本
    def set_text(self, text):
        self.text = text
    # 设置字体
    def set_text(self, font):
        self.f1 = pygame.freetype.SysFont(font, self.size)
    # 设置颜色
    def set_text(self, colour):
        self.text_colour = colour
    # 设置位置
    def set_text(self, pos):
        self.x = pos[0]
        self.y = pos[1]