
# 三方模块



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

    # 初始化
    def __init__(self, width, height, image_path=None):
        # 调用父类的构函
        super().__init__(image_path)
        self.set_w_h(width, height)
        # 初始化滑块
        self.slider_view = ButtonMd.Button(width=viewCfgMd.view_slider_width,height=viewCfgMd.view_slider_height)
        self.slider_view.rect_width = 0 # 0 填充内部
        self.slider_view.frame_colour = viewCfgMd.view_slider_colour 
        self.slider_view.text = ""
        self.slider_view.set_pos(width - self.slider_view.width, 0)
        self.slider_view.set_mouse_event(mouseEnumMd.mouse_click_drag, self, self.slider_drag_event)
        self.add_son_view(self.slider_view)
        # 设置边框
        self.have_frame = True

    # 绘制
    def draw(self, view_obj, pos):
        if not self.show:
            return
        super().draw(view_obj, pos)


        
    # 滑块移动事件
    def slider_drag_event(self, ret_mouse):
        # y是否变化
        if ret_mouse.y == ret_mouse.last_down_y:
            return

        # 是否在图形内  位置是父节点的绝对位置
        if not self.check_click(ret_mouse, self.get_father_abs_pos()):
            return

        # 限制范围
        new_y = self.slider_view.y + (ret_mouse.y - ret_mouse.last_down_y)
        new_y = max(new_y, 0)
        new_y = min(new_y, self.height - self.slider_view.height)
        # 根据变化量修改滑块位置
        self.slider_view.y = new_y

        pass

        