

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
    # 对齐规则
    # x轴
    text_x_pos_type = viewCfgMd.text_x_pos_middle
    # y轴
    text_y_pos_type = viewCfgMd.text_y_pos_middle
    # 对齐偏移参数
    text_pos_deviation = 0
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
            abs_pos = self.get_abs_pos()
            # 换行
            str_list = self.text_str.split("\n")
            # 获取y位置
            pos_y_list = self.get_text_y_pos_list(str_list)
            str_idx = 0 
            for tmp_pos_y in pos_y_list:
                tmp_str = str_list[str_idx]
                tmp_pos_x = self.get_text_x_pos(tmp_str)
                self.f1.render_to(view_obj, (tmp_pos_x, tmp_pos_y), tmp_str, fgcolor = self.text_colour, size = self.text_size)
                str_idx += 1
    
    
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
    def get_text_str_w(self, tmp_str):
        # 中文占两个位置
        if not tmp_str:
            return 0
        str_len = 0
        for ch in tmp_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                str_len += 1
            else:
                str_len += 0.5
        return str_len * self.text_size
    # 获取文本高度
    def get_text_str_h(self, tmp_str):
        for ch in tmp_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return 2 * self.text_size
        return self.text_size
    
    # 获取文本pos_y列表
    def get_text_y_pos_list(self, str_list):
        str_list_len = len(str_list)
        abs_pos = self.get_abs_pos()
        pos_y = abs_pos[1]
        if self.text_y_pos_type == viewCfgMd.text_y_pos_middle:
            # 居中
            pos_y += self.height/2    # y中间
            pos_y = pos_y - (self.text_size * str_list_len)/2 # 最上面的y
        elif self.text_y_pos_type == viewCfgMd.text_y_pos_top:
            # 顶部对齐
            pass
        elif self.text_y_pos_type == viewCfgMd.text_y_pos_bottom:
            # 底部对齐
            pos_y = pos_y + self.height - self.text_size * str_list_len
        pos_y_list = self.text_y_pos_list(str_list, pos_y)
        return pos_y_list
    
    # 向pos_y_list添加元素
    # pos_y:y起始位置
    def text_y_pos_list(self, str_list, pos_y):
        pos_y_list = []
        str_list_len = len(str_list)
        for idx in range(str_list_len):
            tmp_str = str_list[idx]
            tmp_str_h = self.get_text_str_h(tmp_str)
            if tmp_str_h == self.text_size: # 没有中文要向下偏移一行
                pos_y_list.append(pos_y + self.text_size/2)
            else:
                pos_y_list.append(pos_y)
            pos_y += self.text_size
        return pos_y_list

    # 获取x位置
    def get_text_x_pos(self, tmp_str):
        abs_pos = self.get_abs_pos()
        pos_x = abs_pos[0]
        str_w = self.get_text_str_w(tmp_str)
        if self.text_x_pos_type == viewCfgMd.text_x_pos_middle:
            # 居中
            pos_x = pos_x + (self.width - str_w)/2
            return pos_x
        elif self.text_x_pos_type == viewCfgMd.text_x_pos_left:
            # 左对齐
            return pos_x