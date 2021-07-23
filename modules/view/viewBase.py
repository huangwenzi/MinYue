

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
    # 点击事件执行函数
    click_func = None  
    # 点击事件参数
    click_argv = None
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, image_path):
        self.set_background(image_path)

    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj, pos):
        if not self.show:
            return
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

        
    # 回归初始位置
    def return_init_pos(self):
        self.set_pos(self.init_x, self.init_y)
        

    # 注册事件
    # 注册点击
    def set_click_event(self, func, argv = None):
        self.click_func = func
        self.click_argv = argv
    # 检查是否在鼠标点击范围内
    def check_click(self, click_pos, father_pos):
        if not self.show:
            return None
        x = father_pos[0] + self.x
        y = father_pos[1] + self.y
        if x < click_pos.x and (x + self.width) > click_pos.x and y < click_pos.y and (y + self.height) > click_pos.y:
            return self
        return None
    # 执行点击函数
    # self : 执行对象
    # argv : 传入参数
    def click_star(self):
        if not self.click_argv:
            self.click_func()
        else:
            self.click_func(self.click_argv)