# 官方模块
import time

# 三方模块
import pygame

# 项目模块
import modules.view.viewVessel as viewVesselMd

# 这是主界面
class MainView(viewVesselMd.viewVessel):
    # 设置
    fps = 1 # 帧率
    LastUpdate = 0  # 上次刷新界面时间

    # 视图对象
    view_obj = None    # 窗体对象


    # 初始化一个主界面
    def __init__(self, image_path):
        #调用父类的构函
        viewVesselMd.viewVessel.__init__(self, image_path)

        pygame.display.set_caption(self.name)
        self.set_background(self, self.image_path)
        self.view_obj = pygame.display.set_mode((self.width, self.height))
        self.fps = 0.5
        self.LastUpdate = time.time()
        


    # 图像设置函数
    # 主界面绘制
    # 也是调用其他界面绘制的地方
    @staticmethod
    def draw(self):
        # 根据帧率刷新
        now = time.time()
        if self.LastUpdate + self.fps > now:
            return
        super(MainView, self).draw(self, self.view_obj, (0, 0))
        pygame.display.flip()
        
        # 更新刷新时间
        self.LastUpdate = now

    # 获取点击的对象
    @staticmethod
    def check_click(self, click_pos, father_pos):
        # 是否在范围内
        ret = super(MainView, self).check_click(self, click_pos, father_pos)
        return ret
