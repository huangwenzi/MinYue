
# 三方模块
import pygame

# 图像设置函数
# draw: 主界面绘制
# set_background: 设置背景图

# 这是主界面
class MainView(object):
    # 显示设置
    name = "minyue" # 视图名
    height = 600  # 高
    wide = 600  # 宽
    background_path = "modules/resource/bg.png" # 背景图

    # 视图对象
    view_obj = None    # 窗体对象
    background_obj = None   # 背景图对象
    son_view_arr = [] # 子视图数组


    # 初始化一个主界面
    def __init__(self):
        pygame.display.set_caption(self.name)
        self.set_background(self.background_path)
        self.view_obj = pygame.display.set_mode((self.height, self.wide))
        

    # 图像设置函数
    # 主界面绘制
    # 也是调用其他界面绘制的地方
    def draw(self):
        self.view_obj.blit(self.background_obj, (0, 0))
        for tmp_view in self.son_view_arr:
            tmp_view.draw(self.view_obj, [self.x, self.y])
        pygame.display.flip()
    # 设置背景图
    # image_path: 背景图地址
    def set_background(self, image_path):
        tmp_obj = pygame.image.load(image_path)
        if tmp_obj:
            self.background_path = image_path
            self.background_obj = tmp_obj
            self.height = tmp_obj.get_height()
            self.wide = tmp_obj.get_width()

