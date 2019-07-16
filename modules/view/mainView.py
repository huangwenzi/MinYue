
# 三方模块
import pygame

# 项目模块
import modules.view.viewVessel as viewVesselMd

# 图像设置函数
# draw: 主界面绘制
# set_background: 设置背景图
# add_son_view: 添加子视图

# 这是主界面
class MainView(viewVesselMd.viewVessel):
    # 视图对象
    view_obj = None    # 窗体对象


    # 初始化一个主界面
    def __init__(self, image_path):
        #调用父类的构函
        viewVesselMd.viewVessel.__init__(self, image_path)

        pygame.display.set_caption(self.name)
        self.set_background(self.image_path)
        self.view_obj = pygame.display.set_mode((self.height, self.wide))


    # 图像设置函数
    # 主界面绘制
    # 也是调用其他界面绘制的地方
    def draw(self):
        super(MainView, self).draw(self.view_obj, (0, 0))
        pygame.display.flip()


