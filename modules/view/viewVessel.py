
# 三方模块



# 项目模块
import modules.view.viewBase as viewBaseMd
import modules.config.viewCfg as viewCfgMd
import modules.config.enum as mouseEnumMd


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
        super().__init__(image_path)
        self.son_view_arr = [] 
        self.close_view = None 
        
    # 绘制
    # 重写子类绘制
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj, pos):
        if not self.show:
            return
        super().draw(view_obj, pos)
        x = self.x + pos[0]
        y = self.y + pos[1]
        # 绘制子视图,从后面开始绘制
        son_len = len(self.son_view_arr)
        for son_idx in range(son_len):
            son_view_arr_idx = son_len - (son_idx + 1)
            tmp_view = self.son_view_arr[son_view_arr_idx]
            tmp_view.draw(view_obj, [x, y])
        # 最后绘制关闭按钮
        if self.close_view:
            self.close_view.draw(view_obj, [x, y])
    # 添加子视图
    # view_obj: 子视图对象
    def add_son_view(self, view_obj):
        # 添加到最前面
        self.son_view_arr.insert(0, view_obj)
    # 设置关闭按钮
    def add_close_Button(self, obj, func):
        self.close_view = viewBaseMd.ViewBase(viewCfgMd.close_button_path)
        self.close_view.set_mouse_event(mouseEnumMd.mouse_click_open, obj, func)
        # 设置位置
        exit_width = self.close_view.width
        x = self.width - exit_width
        y = 0
        self.close_view.set_pos(x, y)
    
    # 获取点击的对象
    def check_click(self, click_pos, father_pos):
        # 自身是否在范围内
        ret = super().check_click(click_pos, father_pos)
        if ret:
            # 先判断关闭按钮
            new_x = father_pos[0] + self.x
            new_y = father_pos[1] + self.y
            if self.close_view:
                close_view_ret = self.close_view.check_click(click_pos, [new_x, new_y])
                if close_view_ret:
                    return close_view_ret
            
            # 是否在子视图内
            idx = 0
            for tmp_view in self.son_view_arr:
                son_ret = tmp_view.check_click(click_pos, [new_x, new_y])
                if son_ret:
                    # 设置点击的视图在最上层
                    if idx != 0:
                        tmp_obj = self.son_view_arr.pop(idx)
                        self.son_view_arr.insert(0, tmp_obj)
                    return son_ret
                idx += 1
            return ret
        
        return None