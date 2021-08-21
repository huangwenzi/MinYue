
# 三方模块
import pygame


# 项目模块
import modules.view.viewVessel as ViewVesselMd
import modules.view.button as ButtonMd
import modules.config.viewCfg as viewCfgMd
import modules.config.enum as mouseEnumMd


# 列表视图
class ViewList(ViewVesselMd.ViewVessel):
    
    # 视图对象
    # 滑块
    slider_view = None
    # 列表内容
    obj_list = []
    # 每行显示数量
    row_num = 0
    # 行距
    row_space = 0
    

    # 初始化
    def __init__(self, width = 100, height = 100, image_path=None):
        # 调用父类的构函
        super().__init__(width, height, image_path)
        self.obj_list = []
        # 初始化滑块
        self.slider_view = ButtonMd.Button(width=viewCfgMd.view_slider_width,height=viewCfgMd.view_slider_height)
        self.slider_view.rect_width = 0 # 0 填充内部
        self.slider_view.frame_colour = viewCfgMd.colour_ash 
        self.slider_view.text_str = ""
        self.slider_view.set_pos(width - self.slider_view.width, 0)
        self.slider_view.set_mouse_event(mouseEnumMd.mouse_click_drag, self, self.slider_drag_event)
        self.add_son_view(self.slider_view)
        # 设置边框
        self.have_frame = True
        # 行设置
        self.row_num = viewCfgMd.view_list_row_num
        self.row_space = viewCfgMd.view_list_row_space
    
    # 添加元素
    def add_element(self, add_obj):
        self.obj_list.append(add_obj)
        self.add_son_view(add_obj)
        # 更新位置
        self.update_pos()
        
    # 更新位置
    def update_pos(self):
        pass
        

    # 滑块移动事件
    def slider_drag_event(self, ret_mouse):
        # y是否变化
        if ret_mouse.y == ret_mouse.last_down_y:
            return

        # 是否在图形内  位置是父节点的绝对位置
        if not self.check_click(ret_mouse):
            return

        # 限制范围
        new_y = self.slider_view.y + (ret_mouse.y - ret_mouse.last_down_y)
        new_y = max(new_y, 0)
        new_y = min(new_y, self.height - self.slider_view.height)
        # 根据变化量修改滑块位置
        self.slider_view.y = new_y
    

        