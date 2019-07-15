

# 三方模块
import pygame





# 界面基类
class viewBase():
    # 显示设置
    name = "" # 视图名
    height = 0  # 高
    wide = 0  # 宽
    image_path = "" # 背景图
    x = 0   # 相对父窗口左上角偏移
    y = 0

    # 视图对象
    image_obj = None    # 图片对象

    
    # 初始化
    # image_path: 图片地址
    def __init__(self, image_path):
        tmp_obj = pygame.image.load(image_path)
        if tmp_obj:
            self.image_path = image_path
            self.image_obj = tmp_obj
            self.height = tmp_obj.get_height()
            self.wide = tmp_obj.get_width()

    # 绘制自身
    # blit_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, blit_obj, pos):
        x = self.x + pos[0]
        y = self.y + pos[0]
        blit_obj.blit(self.image_obj, (x, y))
