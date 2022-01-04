# 官方库
import json

# 项目模块
# 游戏引擎模块
import modules.view.mainView as mainViewMd
import modules.view.button as ButtonMd
import modules.view.inputBox as InputBoxMd
import modules.control.instanceMgr as instanceMgrMd
import modules.config.enum as mouseEnumMd


# mod模块



# 节点周围八点坐标偏移
pos_deviation = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [0, 1], [1, 1]
]


click_state_free = 0            # 空闲
click_state_set_node = 1        # 设置节点状态 可移动和不可移动切换
click_state_set_b_e = 2         # 设置起点和终点

# 格子边长
cfg_grid_side_size = 50
# 地图尺寸
cfg_node_w = 10
cfg_node_h = 10


# 节点对象
class Node(object):
    # 坐标
    x = 0
    y = 0
    # map_key
    map_key = ""
    
    f = 0   # 总距离
    g = 0   # 到起点距离
    h = 0   # 到终点距离
    def __init__(self):
        pass
        
        

# 这是主界面
class MainView(mainViewMd.MainView):
    # 宽高
    node_w = cfg_node_w
    node_h = cfg_node_h

    # 初始界面
    # 设置节点状态按钮
    set_node_state_button = None
    # 设置起点和终点按钮
    set_begin_end_button = None
    # 重置节点数据按钮
    reset_node_button = None
    # 开始寻路按钮
    begin_button = None

    # 当前点击状态
    click_state = click_state_free
    # 设置起点或终点
    

    # 节点map 对象
    node_map = {}

    # 初始化
    def __init__(self):
        # 计算长宽
        view_width = self.node_w * cfg_grid_side_size + 300 # 留300给操作按钮
        view_height = self.node_h *cfg_grid_side_size
        super().__init__(view_width, view_height)
        self.set_fps(0.05)
        self.click_state = click_state_free

        # 初始化
        # 按钮
        # 设置节点状态按钮
        self.set_node_state_button = set_node_state_button = ButtonMd.Button(text_str = "修改节点\n状态", width = 100, height = 100)
        set_node_state_button.set_pos(self.width - 200, 0)
        self.add_son_view(set_node_state_button)
        set_node_state_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.set_node_state_button_click_event)
        # 设置起点和终点按钮
        self.set_begin_end_button = set_begin_end_button = ButtonMd.Button(text_str = "起点和\n终点", width = 100, height = 100)
        set_begin_end_button.set_pos(self.width - 200, 100)
        self.add_son_view(set_begin_end_button)
        set_begin_end_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.set_begin_end_button_click_event)
        # 重置节点数据按钮
        self.reset_node_button = reset_node_button = ButtonMd.Button(text_str = "重置", width = 100, height = 100)
        reset_node_button.set_pos(self.width - 200, 200)
        self.add_son_view(reset_node_button)
        reset_node_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.reset_node_button_click_event)
        # 开始寻路按钮
        self.begin_button = begin_button = ButtonMd.Button(text_str = "开始寻路", width = 100, height = 100)
        begin_button.set_pos(self.width - 200, 300)
        self.add_son_view(begin_button)
        begin_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.begin_button_click_event)
        # 初始化节点数据
        self.init_node()
    
    # 初始化节点数据
    def init_node(self):
        # 删除旧节点数据
        for node_key in self.node_map:
            self.del_son_view(self.node_map[node_key])
        self.node_map = {}
        # 创建新节点数据
        for idx_x in range(self.node_w):
            for idx_y in range(self.node_h):
                # 节点对象
                node_button = ButtonMd.Button(text_str = "", width = cfg_grid_side_size, height = cfg_grid_side_size)
                node_button.set_pos(idx_x * cfg_grid_side_size, idx_y * cfg_grid_side_size)
                node_button.have_figure = True
                self.add_son_view(node_button)
                node_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.node_button_click_event)
                # 添加到node_map
                node_key = "{}_{}".format(idx_x, idx_y)
                node = Node()
                node.x = idx_x
                node.y = idx_y
                node.map_key = node_key
                node_button.param = node
                self.node_map[node_key] = node_button



    # 事件
    # 设置节点状态按钮
    def set_node_state_button_click_event(self, ret_mouse):
        self.click_state = click_state_set_node
    # 设置起点和终点按钮
    def set_begin_end_button_click_event(self, ret_mouse):
        self.click_state = click_state_set_b_e
    # 重置节点数据按钮
    def reset_node_button_click_event(self, ret_mouse):
        pass
    # 开始寻路按钮
    def begin_button_click_event(self, ret_mouse):
        pass
    # 节点点击
    def node_button_click_event(self, ret_mouse):
        pass
    

# 获取单例
def getInstance():
    name = "MainView"
    ins = instanceMgrMd.instanceMgr.get_ins(name)
    if not ins:
        ins = MainView()
        instanceMgrMd.instanceMgr.set_ins(name, ins)
    return ins