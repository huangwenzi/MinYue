
# 三方模块
import pygame

# 项目模块
import modules.view.viewBase as viewBaseMd

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
    @staticmethod
    def draw(self, view_obj, pos):
        if not self.show:
            return
        super(viewVessel, self).draw(self, view_obj, pos)
        x = self.x + pos[0]
        y = self.y + pos[0]
        # 绘制子视图,从后面开始绘制
        son_len = len(self.son_view_arr)
        for idx in range(son_len):
            tmp_view = self.son_view_arr[son_len - idx - 1]
            tmp_view.draw(tmp_view, view_obj, [x, y])
    # 添加子视图
    # view_obj: 子视图对象
    @staticmethod
    def add_son_view(self, view_obj):
        self.son_view_arr.insert(0, view_obj)
    
    # 获取点击的对象
    @staticmethod
    def check_click(self, click_pos, father_pos):
        # 是否在范围内
        ret = super(viewVessel, self).check_click(self, click_pos, father_pos)
        if ret:
            # 是否在子视图内
            father_pos[0] += self.x
            father_pos[1] += self.y
            idx = 0
            for tmp_view in self.son_view_arr:
                tmp_ret = tmp_view.check_click(tmp_view, click_pos, father_pos)
                if tmp_ret:
                    if idx != 0:
                        tmp_obj = self.son_view_arr.pop(idx)
                        self.son_view_arr.insert(0, tmp_obj)
                    return tmp_ret
                idx += 1
            return ret
        
        return None