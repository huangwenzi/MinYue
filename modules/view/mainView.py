# 官方模块
import time

# 三方模块
import pygame

# 项目模块
import modules.view.viewVessel as viewVesselMd

# 这是主界面
class MainView(viewVesselMd.ViewVessel):
    # 设置
    fps = 1 # 帧率
    next_update = 0  # 下次刷新界面时间

    # 视图对象
    view_obj = None    # 窗体对象


    # 初始化一个主界面
    def __init__(self, image_path):
        #调用父类的构函
        super().__init__(image_path)
        pygame.display.set_caption(self.name)
        self.view_obj = pygame.display.set_mode((self.width, self.height))
        self.next_update = time.time()
        


    # 图像设置函数
    # 主界面绘制
    # 也是调用其他界面绘制的地方
    def draw(self):
        # 根据帧率刷新
        now = time.time()
        if now < self.next_update:
            return
        super().draw(self.view_obj, (0, 0))
        # update()绘制变化部分 flip()绘制全部
        # pygame.display.flip()
        pygame.display.update() 
        # 更新刷新时间
        self.next_update = now + self.fps

    # 获取点击的对象
    def check_click(self, click_pos, father_pos):
        # 是否在范围内
        ret = super().check_click(click_pos, father_pos)
        return ret

    # 设置帧率
    def set_fps(self, new_fps):
        self.fps = new_fps
