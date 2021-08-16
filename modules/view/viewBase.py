

# 三方模块
import pygame





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

    # 视图对象
    # 图片对象
    image_obj = None    

    # 事件
    # 点击事件
    # 是否有点击事件
    click_func_state = False
    # 点击事件执行函数
    click_func = None  
    # 点击事件参数
    click_argv = None

    # 键盘事件
    keyboard_func_state = False
    # 键盘事件执行函数
    keyboard_func = None  
    # 键盘事件参数
    keyboard_argv = None
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, image_path):
        if image_path:
            self.set_background(image_path)

    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj, pos):
        if not self.show:
            return
        # 是否有背景图
        if self.image_obj:
            x = self.x + pos[0]
            y = self.y + pos[1]
            view_obj.blit(self.image_obj, (x, y))

    # 设置背景图
    # image_path: 背景图地址
    def set_background(self, image_path):
        tmp_obj = pygame.image.load(image_path)
        if tmp_obj:
            self.image_path = image_path
            self.image_obj = tmp_obj
            self.height = tmp_obj.get_height()
            self.width = tmp_obj.get_width()

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
    def check_click(self, click_pos, father_pos):
        if not self.show:
            return None
        x = father_pos[0] + self.x
        y = father_pos[1] + self.y
        if x < click_pos.x and (x + self.width) > click_pos.x and y < click_pos.y and (y + self.height) > click_pos.y:
            return self
        return None

    # 注册事件
    # 注册点击事件
    def set_click_event(self, func, argv = None):
        self.click_func = func
        self.click_argv = argv
        self.click_func_state = True
    # 执行点击函数
    # self : 执行对象
    # argv : 传入参数
    def click_star(self):
        if self.click_func_state:
            if not self.click_argv:
                self.click_func()
            else:
                self.click_func(self.click_argv)

    # 注册键盘事件
    def set_keyboard_event(self, func, argv = None):
        self.keyboard_func = func
        self.keyboard_argv = argv
        self.keyboard_func_state = True
    # 执行点击函数
    # self : 执行对象
    # argv : 传入参数
    def keyboard_star(self, keyboard):
        if self.keyboard_func_state:
            if not self.keyboard_argv:
                self.keyboard_func(keyboard)
            else:
                self.keyboard_func(keyboard, self.keyboard_argv)