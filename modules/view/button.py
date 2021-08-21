

# 三方模块

# 项目模块
import modules.view.label as LabelMd



# 按钮
class Button(LabelMd.Label):  
    # 图形
    
    
    # 初始化
    # image_path: 图片地址
    def __init__(self, text_str = None, text_size = None, width = 0, height = 0, image_path = None):
        #调用父类的构函
        super().__init__(text_str, text_size, width, height, image_path)
        # 设置边框
        self.have_frame = True
        
    # 图像相关函数
    # 绘制自身
    # view_obj: 调用绘制对象（一般为主视图）
    # pos: 上一层的坐标偏移
    def draw(self, view_obj):
        if not self.show:
            return
        # 父类绘制图片
        super().draw(view_obj)