

# 项目模块
import modules.view.viewBase as viewBaseMd

# 最基础的视图容器
class classname(viewBaseMd.viewBase):
    
    # 视图对象
    son_view_arr = [] # 子视图数组

    # 初始化
    def __init__(self, image_path):
        #调用父类的构函
        viewBaseMd.viewBase.__init__(self, image_path)
        
    # 绘制容器
    # blit_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, blit_obj, pos):
        x = self.x + pos[0]
        y = self.y + pos[0]
        blit_obj.blit(self.image_obj, (x, y))
        # 绘制子视图
        for tmp_view in self.son_view_arr:
            tmp_view.draw(self.view_obj, [x, y])