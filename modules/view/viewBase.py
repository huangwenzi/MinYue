

# 三方模块
import pygame





# 界面基类
class viewBase():
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
    # 背景图
    image_path = "" 
    # 是否显示
    show = False
    

    # 视图对象
    # 图片对象
    image_obj = None    

    # 事件
    # 点击事件
    click_func = None  
    # 执行的参数
    click_agv = None
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, image_path):
        tmp_obj = pygame.image.load(image_path)
        if tmp_obj:
            self.name = ""
            self.height = tmp_obj.get_height()
            self.width = tmp_obj.get_width()
            self.image_path = image_path
            self.x = 0
            self.y = 0
            self.image_obj = tmp_obj
            self.click_func = None
            self.show = True

    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    @staticmethod
    def draw(self, view_obj, pos):
        if not self.show:
            return
        x = self.x + pos[0]
        y = self.y + pos[0]
        view_obj.blit(self.image_obj, (x, y))
    # 设置背景图
    # image_path: 背景图地址
    @staticmethod
    def set_background(self, image_path):
        tmp_obj = pygame.image.load(image_path)
        if tmp_obj:
            self.image_path = image_path
            self.image_obj = tmp_obj
            self.height = tmp_obj.get_height()
            self.width = tmp_obj.get_width()
    # 设置位置
    @staticmethod
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    # 注册事件
    # 注册点击
    @staticmethod
    def set_click_event(self, func, agv = None):
        self.click_func = func
        self.click_agv = agv
    # 检查是否在鼠标点击范围内
    @staticmethod
    def check_click(self, click_pos, father_pos):
        if not self.show:
            return None
        x = father_pos[0] + self.x
        y = father_pos[1] + self.y
        if self.x < click_pos.x and (self.x + self.width) > click_pos.x and self.y < click_pos.y and (self.y + self.height) > click_pos.y:
            return self
        return None
    # 执行点击函数
    @staticmethod
    def click_star(self):
        self.click_func(self.click_agv)