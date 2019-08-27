
# 三方模块
import pygame

# 项目模块
import modules.view.viewBase as viewBaseMd

Close_button_path = "modules/resource/exit.png"

# 最基础的视图容器
class ViewVessel(viewBaseMd.ViewBase):
    
    # 视图对象
    # 关闭按钮
    close_view = None
    # 子视图数组
    son_view_arr = [] 
    

    # 初始化
    def __init__(self, image_path):
        #调用父类的构函
        viewBaseMd.ViewBase.__init__(self, image_path)
        self.son_view_arr = []
        self.close_view = None
        
    # 绘制
    # 重写子类绘制
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    @staticmethod
    def draw(self, view_obj, pos):
        if not self.show:
            return
        super(ViewVessel, self).draw(self, view_obj, pos)
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
    # 设置关闭按钮
    @staticmethod
    def add_close_Button(self, func, argv = None):
        self.close_view = viewBaseMd.ViewBase(Close_button_path)
        if argv:
            viewBaseMd.ViewBase.set_click_event(self.close_view, func, argv)
        else:
            viewBaseMd.ViewBase.set_click_event(self.close_view, func)
        # 设置位置
        exit_width = self.close_view.width
        exit_height = self.close_view.height
        x = self.width - exit_width
        y = 0
        viewBaseMd.ViewBase.set_pos(self.close_view, x, y)
        ViewVessel.add_son_view(self, self.close_view)
    
    # 获取点击的对象
    @staticmethod
    def check_click(self, click_pos, father_pos):
        # 是否在范围内
        ret = super(ViewVessel, self).check_click(self, click_pos, father_pos)
        if ret:
            # 是否在子视图内
            father_pos[0] += self.x
            father_pos[1] += self.y
            idx = 0
            for tmp_view in self.son_view_arr:
                tmp_ret = tmp_view.check_click(tmp_view, click_pos, father_pos)
                if tmp_ret:
                    # 设置点击的视图在最上层
                    if idx != 0:
                        tmp_obj = self.son_view_arr.pop(idx)
                        self.son_view_arr.insert(0, tmp_obj)
                    return tmp_ret
                idx += 1
            return ret
        
        return None