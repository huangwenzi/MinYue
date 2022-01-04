

# 三方模块
import pygame
import copy


# 项目库
import modules.config.viewCfg as viewCfgMd
import modules.view.viewLib as ViewLibMd
import modules.config.enum as EnumMd


# 事件对象
class EventObj(object):
    # 事件状态 False:未开启
    state = False
    # 事件执行函数
    func = None  
    # 事件参数
    argv = None
    # 组件对象
    obj = None
    def __init__(self):
        self.state = False
        self.func = None
        self.argv = None
        self.obj = None
        


# 界面基类
class ViewBase():
    # 显示设置
    # 视图名
    name = "" 
    # 高
    height = 0  
    # 宽
    width = 0  
    # 相对父窗口左上角偏移
    x = 0   
    y = 0
    # 相对父窗口左上角偏移,初始位置
    init_x = 0   
    init_y = 0
    # 背景图
    image_path = "" 
    # 是否显示
    show = True

    # 图形
    have_figure = False
    figure_colour = viewCfgMd.colour_ash

    # 边框
    # 是否有边框
    have_frame = False
    # 图形类型
    frame_figure_type = 0
    # 边框颜色
    frame_colour = viewCfgMd.colour_black
    # 边框宽度
    frame_width = 0

    # 视图对象
    # 图片对象
    image_obj = None   
    # 父对象
    father_obj = None 

    # 事件
    # 鼠标事件
    mouse_event_list = []
    # 键盘事件
    keyboard_event = None

    # 额外参数
    param = None
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, width = 10, height = 10, image_path = None):
        if image_path:
            self.set_background(image_path)
        else:
            # self.image_obj = pygame.Surface((width,height))
            # self.image_obj.fill(viewCfgMd.colour_white)
            self.width = width
            self.height = height
        self.father_obj = None
        self.frame_colour = viewCfgMd.colour_black
        self.frame_width = viewCfgMd.view_frame_width
        self.frame_figure_type = viewCfgMd.view_type_rect
        self.keyboard_event = EventObj()
        self.mouse_event_list = []
        for idx in range(EnumMd.mouse_click_max+1):
            self.mouse_event_list.append(EventObj())
        self.param = None

    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图
    def draw(self, view_obj):
        if not self.show:
            return
        # 没有 father的是main_view, 退出
        if not self.father_obj:
            return 
        # 是否应超出范围需要改变
        self_figure = self.get_view_figure()
        father_figure = self.father_obj.get_view_figure()
        have_change,ret_rect = ViewLibMd.get_rect_in_rect_part(self_figure, father_figure)
        # 绘制图像
        self.draw_image_obj(view_obj, have_change, ret_rect)
        # 绘制图形
        self.draw_figure(view_obj, have_change, ret_rect, self_figure)
        # 绘制边框
        self.draw_frame(view_obj, have_change, ret_rect, self_figure)
    
    # 绘制图像
    def draw_image_obj(self, view_obj, have_change, ret_rect):
        if not self.image_obj:
            return
        if not self.father_obj:
            return
        # pygame.Surface.blit()
        # 只绘制在父对象范围内的图像
        if self.father_obj:
            # 是否超出范围
            self_figure = self.get_view_figure()
            father_figure = self.father_obj.get_view_figure()
            if not ViewLibMd.rect_in_rect(self_figure, father_figure):
                # 超出范围不绘制
                return
            else:
                abs_pos = self.get_abs_pos()
                # 是否应超出范围需要改变
                have_change,ret_rect = ViewLibMd.get_rect_in_rect_part(self_figure, father_figure)
                # 是否有修改
                if have_change:
                    # 绘制
                    view_obj.blit(self.image_obj, abs_pos, ViewLibMd.view_rect_to_pygame_rect(ret_rect))
                else:
                    # 正常绘制
                    view_obj.blit(self.image_obj, abs_pos)  

    # 绘制图形
    def draw_figure(self, view_obj, have_change, ret_rect, self_figure):
        # 没有图形退出
        if not self.have_figure:
            return
        if self.frame_figure_type == viewCfgMd.view_type_rect:
            # 矩形边框
            if have_change:
                abs_pos = self.get_abs_pos()
                frame_rect = copy.deepcopy(ret_rect)
                frame_rect.x = frame_rect.x + abs_pos[0]
                frame_rect.y = frame_rect.y + abs_pos[1]
                pygame.draw.rect(view_obj, self.figure_colour, ViewLibMd.view_rect_to_pygame_rect(frame_rect), 0)
            else:
                pygame.draw.rect(view_obj, self.figure_colour, ViewLibMd.view_rect_to_pygame_rect(self_figure), 0)
        elif self.frame_figure_type == viewCfgMd.view_type_rhombus:
            # 菱形边框  没考虑超范围问题
            # 先求出四个点
            pos_1,pos_2,pos_3,pos_4 = ViewLibMd.get_rhombus_pos(ViewLibMd.view_dot(self.x, self.y), self.width, self.height)
            # polygon支持多边形
            points = [pos_1,pos_2,pos_3,pos_4]
            pygame.draw.polygon(view_obj, self.figure_colour, points, 0)

    # 绘制边框
    def draw_frame(self, view_obj, have_change, ret_rect, self_figure):
        if not self.have_frame:
            return

        if self.frame_figure_type == viewCfgMd.view_type_rect:
            # 矩形边框
            if have_change:
                abs_pos = self.get_abs_pos()
                frame_rect = copy.deepcopy(ret_rect)
                frame_rect.x = frame_rect.x + abs_pos[0]
                frame_rect.y = frame_rect.y + abs_pos[1]
                pygame.draw.rect(view_obj, self.frame_colour, ViewLibMd.view_rect_to_pygame_rect(frame_rect), self.frame_width)
            else:
                pygame.draw.rect(view_obj, self.frame_colour, ViewLibMd.view_rect_to_pygame_rect(self_figure), self.frame_width)
        elif self.frame_figure_type == viewCfgMd.view_type_rhombus:
            # 菱形边框  没考虑超范围问题
            # 先求出四个点
            pos_1,pos_2,pos_3,pos_4 = ViewLibMd.get_rhombus_pos(ViewLibMd.view_dot(self.x, self.y), self.width, self.height)
            # pygame.draw.line(view_obj, self.frame_colour, pos_1, pos_2, self.frame_width)
            # pygame.draw.line(view_obj, self.frame_colour, pos_2, pos_3, self.frame_width)
            # pygame.draw.line(view_obj, self.frame_colour, pos_3, pos_4, self.frame_width)
            # pygame.draw.line(view_obj, self.frame_colour, pos_4, pos_1, self.frame_width)
            # polygon支持多边形
            points = [pos_1,pos_2,pos_3,pos_4]
            pygame.draw.polygon(view_obj, self.frame_colour, points, self.frame_width)
        

    # 设置背景图
    # image_path: 背景图地址
    def set_background(self, image_path):
        tmp_obj = pygame.image.load(image_path)
        if tmp_obj:
            self.image_path = image_path
            self.image_obj = tmp_obj
            self.height = tmp_obj.get_height()
            self.width = tmp_obj.get_width()
        
    # 获取绝对位置
    def get_abs_pos(self):
        # 判断是否有父节点
        if self.father_obj:
            father_abs_pos = self.father_obj.get_abs_pos()
            return (father_abs_pos[0] + self.x, father_abs_pos[1] + self.y)
        else:
            return (0,0)
    # 获取图形对象
    def get_view_figure(self):
        abs_pos = self.get_abs_pos()
        return ViewLibMd.view_rect(abs_pos[0], abs_pos[1], self.width, self.height)

    # 设置位置
    def set_pos(self, x, y):
        self.x = x
        self.y = y
    # 设置初始位置
    def set_init_pos(self, x, y):
        self.init_x = x
        self.init_y = y
    # 设置是否显示
    def set_show(self, show_type):
        self.show = show_type
    # 设置宽高
    def set_w_h(self, width, height):
        self.width = width
        self.height = height
    # 回归初始位置
    def return_init_pos(self):
        self.set_pos(self.init_x, self.init_y)
        
    # 检查函数
    # 检查是否在鼠标点击范围内
    def check_click(self, click_pos):
        if not self.show:
            return None
        self_figure = self.get_view_figure()
        if self.frame_figure_type == viewCfgMd.view_type_rect:
            # 矩形
            if ViewLibMd.dot_in_rect(ViewLibMd.view_dot(click_pos.x, click_pos.y), self_figure):
                return self
        elif self.frame_figure_type == viewCfgMd.view_type_rhombus:
            # 菱形
            if ViewLibMd.dot_in_rhombus(ViewLibMd.view_dot(click_pos.x, click_pos.y), self_figure):
                return self
        return None

    # 注册事件
    # 注册鼠标事件
    def set_mouse_event(self, mouse_type, obj, func, argv = None):
        mouse_event = self.mouse_event_list[mouse_type]
        mouse_event.obj = obj
        mouse_event.argv = argv
        mouse_event.func = func
        mouse_event.state = True
    # 删除鼠标事件
    def del_mouse_event(self, mouse_type):
        mouse_event = self.mouse_event_list[mouse_type]
        mouse_event.obj = None
        mouse_event.argv = None
        mouse_event.func = None
        mouse_event.state = False
    # 执行鼠标事件
    def mouse_event_star(self, ret_mouse):
        mouse_event = self.mouse_event_list[ret_mouse.type]
        if mouse_event and mouse_event.state:
            if not mouse_event.argv:
                mouse_event.func(ret_mouse)
            else:
                mouse_event.func(ret_mouse, mouse_event.argv)

    # 注册键盘事件
    def set_keyboard_event(self, obj, func, argv = None):
        self.keyboard_event.obj = obj
        self.keyboard_event.func = func
        self.keyboard_event.argv = argv
        self.keyboard_event.state = True
    # 删除键盘事件
    def del_keyboard_event(self):
        self.keyboard_event.obj = None
        self.keyboard_event.func = None
        self.keyboard_event.argv = None
        self.keyboard_event.state = False
    # 执行点击函数
    # self : 执行对象
    # argv : 传入参数
    def keyboard_star(self, keyboard):
        if self.keyboard_event.state:
            if not self.keyboard_event.argv:
                self.keyboard_event.func(keyboard)
            else:
                self.keyboard_event.func(keyboard, self.keyboard_event.argv)