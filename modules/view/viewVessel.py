
# 三方模块
import pygame

# 项目模块
import modules.view.viewBase as viewBaseMd

# draw: 主界面绘制
# add_son_view: 添加子视图

# 最基础的视图容器
class viewVessel(viewBaseMd.viewBase):
    
    # 视图对象
    son_view_arr = [] # 子视图数组

    # 初始化
    def __init__(self, image_path):
        #调用父类的构函
        viewBaseMd.viewBase.__init__(self, image_path)
        self.son_view_arr = []
        
    # 绘制
    # 重写子类绘制
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj, pos):
        super(viewVessel, self).draw(view_obj, pos)
        # 绘制子视图
        for tmp_view in self.son_view_arr:
            tmp_view.draw(view_obj, [pos[0], pos[1]])
    # 添加子视图
    # view_obj: 子视图对象
    def add_son_view(self, view_obj):
        self.son_view_arr.append(view_obj)