# 官方库
import json

# 项目模块
# 游戏引擎模块
import modules.view.mainView as mainViewMd
import modules.view.button as ButtonMd
import modules.view.inputBox as InputBoxMd
import modules.control.instanceMgr as instanceMgrMd
import modules.config.enum as mouseEnumMd
import modules.view.label as LabelMd
import modules.config.viewCfg as viewCfgMd


# mod模块
import jxgame.stage_excel.lib.excel_lib as ExcelLib



click_state_free = 0            # 空闲
click_state_select_node = 1     # 选节点



        

# 这是主界面
class MainView(mainViewMd.MainView):
    # 配置
    cfg = None

    # 初始界面
    # 关卡id label
    init_stage_label = None
    # 关卡输入
    init_in_put_stage = None
    # 确定按钮
    init_ok_button = None

    # 地图编辑界面
    # 更新按钮
    map_edit_update_button = None
    # 关卡id显示
    map_edit_stage_label = None
    map_edit_in_put_stage = None
    # 节点显示
    map_edit_node_label = None
    map_edit_in_put_node_id = None
    map_edit_set_node_id_button = None
    # 

    # 宽高
    w = 0
    h = 0

    # 数据
    excel_obj = None
    # 地格对象
    grid_list = []
    # 选择的关卡
    stage = 0

    # 当前点击状态
    click_state = click_state_free

    # 初始化
    def __init__(self):
        # 计算长宽
        # 加载配置
        file = open("jx_stage.json", "rb")
        cfg = json.load(file)
        # 留300给操作按钮
        view_width = cfg["w"] * cfg["ima_size"][0] + 300
        view_height = (cfg["h"] + 1) * cfg["ima_size"][1] // 2 # 穿插占用位置少一半
        self.cfg = cfg
        super().__init__(view_width, view_height)
        self.set_fps(0.05)
        self.stage = 0
        self.click_state = click_state_free
        self.excel_obj = None
        self.grid_list = []

        # 初始化其他功能
        # 关卡输入
        main_width = self.width
        self.init_stage_label = init_stage_label = LabelMd.Label(text_str = "关卡id:", width = 50, height = 50)
        init_stage_label.set_pos(main_width/2 - init_stage_label.width, 100)
        init_stage_label.text_size = 15
        self.add_son_view(init_stage_label)
        self.init_in_put_stage = init_in_put_stage = InputBoxMd.InputBox(text_str = "", width = 100, height = 50)
        init_in_put_stage.set_pos(main_width/2, 100)
        self.add_son_view(init_in_put_stage)
        # 按钮
        # 确定按钮
        self.init_ok_button = init_ok_button = ButtonMd.Button(text_str = "确定aa\na", width = 100, height = 100)
        init_ok_button.set_pos((main_width - init_ok_button.width)/2, 160)
        self.add_son_view(init_ok_button)
        init_ok_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.init_ok_button_click_event)
    


    # 绘制地图编辑界面
    def init_map_edit(self):
        # 初始化关卡数据
        self.init_map_edit_stage_data()
        # 初始化地图编辑界面组件
        self.init_map_edit_assembly()
    
    # 初始化关卡数据
    def init_map_edit_stage_data(self):
        # 删除旧数据
        self.clear_grid_list()
        # 提取关卡数据
        stage = self.stage
        data_map = {}
        stage_key = self.cfg["stage"]
        pos_key = self.cfg["pos"]
        for item in self.excel_obj.data:
            tmp_data = self.excel_obj.data[item]
            if tmp_data[stage_key] == stage:
                key = "{}_{}".format(tmp_data[pos_key][0], tmp_data[pos_key][1]) 
                data_map[key] = tmp_data
        # 添加地格数据
        for w in range(self.cfg["w"]):
            for h in range(self.cfg["h"]):
                key = "{}_{}".format(w, h) 
                tmp_data = {}
                if key in data_map:
                    tmp_data = data_map[key]
                else:
                    pos = [w, h]
                    tmp_data = ExcelLib.get_data_obj(self.excel_obj.key_list)
                    tmp_data[pos_key] = pos
                grid_obj = self.get_grid_obj(tmp_data)
                self.add_son_view(grid_obj)
                self.grid_list.append(grid_obj)


        
    # 初始化地图编辑界面组件
    def init_map_edit_assembly(self):
        # 关卡id
        self.map_edit_stage_label = map_edit_stage_label = LabelMd.Label(text_str = "关卡id:", width = 50, height = 50)
        map_edit_stage_label.set_pos(self.width - 200, 50)
        map_edit_stage_label.text_size = 15
        self.add_son_view(map_edit_stage_label)
        self.map_edit_in_put_stage = map_edit_in_put_stage = InputBoxMd.InputBox(text_str = str(self.stage), width = 50, height = 50)
        map_edit_in_put_stage.set_pos(self.width - 150, 50)
        self.add_son_view(map_edit_in_put_stage)
        # 当前节点id
        self.map_edit_node_label = map_edit_node_label = LabelMd.Label(text_str = "节点id:", width = 50, height = 50)
        map_edit_node_label.set_pos(self.width - 100, 50)
        map_edit_node_label.text_size = 15
        self.add_son_view(map_edit_node_label)
        map_edit_in_put_node_id = InputBoxMd.InputBox(text_str = str(1), width = 50, height = 50)
        map_edit_in_put_node_id.set_pos(self.width - 50, 50)
        self.map_edit_in_put_node_id = map_edit_in_put_node_id
        self.add_son_view(map_edit_in_put_node_id)
        # 设置节点id按钮
        self.map_edit_set_node_id_button = map_edit_set_node_id_button = ButtonMd.Button(text_str = "设置节点id:关闭", width = 200, height = 50)
        map_edit_set_node_id_button.set_pos(self.width - 200, 100)
        self.add_son_view(map_edit_set_node_id_button)
        map_edit_set_node_id_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.map_edit_set_node_id_button_click_event)

    
    
    
        
    # 获取地格对象
    def get_grid_obj(self, grid_data):
        grid_w = self.cfg["ima_size"][0]
        grid_h = self.cfg["ima_size"][1]
        grid_obj = LabelMd.Label(text_str = self.get_grid_show_str(grid_data), width = grid_w, height = grid_h)
        grid_obj.have_frame = True
        # 设置时菱形
        grid_obj.frame_figure_type = viewCfgMd.view_type_rhombus
        # 设置坐标
        pos_key = self.cfg["pos"]
        pos_x = grid_data[pos_key][1] * grid_w
        pos_y = grid_data[pos_key][0] // 2 * grid_h    # 第1和第3行上下相接
        # 单数行会错开
        if grid_data[pos_key][0] % 2 > 0:
            pos_x += grid_w/2
            pos_y += grid_h/2
        grid_obj.set_pos(pos_x, pos_y)
        grid_obj.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.rhombus_click_event, grid_obj)
        grid_obj.set_mouse_event(mouseEnumMd.mouse_click_move_in, self, self.rhombus_move_in_event, grid_obj)
        grid_obj.set_mouse_event(mouseEnumMd.mouse_click_move_out, self, self.rhombus_move_out_event, grid_obj)
        grid_obj.param = grid_data
        return grid_obj
    
    # 获取显示
    def get_grid_show_str(self, grid_data):
        show_str = ""
        for key in self.cfg["show_data"]:
            show_str += "{}:".format(grid_data[key])
        if show_str != "":
            show_str = show_str[:-1]
        return show_str


    # 初始化关卡数据
    def init_stage_data(self):
        w = self.cfg["w"]
        h = self.cfg["h"]
        pos_key = self.cfg["pos"]
        data_list = []
        for tmp_w in range(w):
            for tmp_h in range(h):
                pos = [tmp_w, tmp_h]
                tmp_data = ExcelLib.get_data_obj(self.excel_obj.key_list)
                tmp_data[pos_key] = pos
                data_list.append(tmp_data)
        return data_list





    # 清除数据
    def clear_old_data(self):
        self.clear_grid_list()
        self.son_view_arr = []

    # 清除地格数据
    def clear_grid_list(self):
        for item in self.grid_list:
            self.del_son_view(item)
        self.grid_list = []

    # 清除初始界面
    def clear_init_view(self):
        # 删除旧图像
        self.del_son_view(self.init_stage_label)
        self.del_son_view(self.init_in_put_stage)
        self.del_son_view(self.init_ok_button)






    # 确定事件
    def init_ok_button_click_event(self, ret_mouse):
        print("init_ok_button_click_event")
        # 提取excel数据
        self.excel_obj = ExcelLib.get_excel_data(self.cfg["excel_path"])
        # 保存关卡
        self.stage = int(self.init_in_put_stage.text_str)
        self.clear_init_view()
        # 绘制图像
        self.init_map_edit()

    # 菱形按钮
    def rhombus_click_event(self, ret_mouse, rhombus_obj):
        print("rhombus_click_event:" + rhombus_obj.text_str)
        # 设置节点id
        if self.click_state == click_state_select_node:
            now_node_id = int(self.map_edit_in_put_node_id.text_str)
            grid_data = rhombus_obj.param
            id_key = self.cfg["id"]
            grid_data[id_key] = now_node_id
            rhombus_obj.text_str = self.get_grid_show_str(grid_data)
            self.map_edit_in_put_node_id.text_str = str(now_node_id + 1)
        elif self.click_state == click_state_free:
            # 空闲时候点击
            # 修改节点属性
            pass    
    
    # 菱形移入
    def rhombus_move_in_event(self, ret_mouse, rhombus_obj):

        pass

    # 菱形移出
    def rhombus_move_out_event(self, ret_mouse, rhombus_obj):

        pass


    # 设置节点按钮
    def map_edit_set_node_id_button_click_event(self, ret_mouse):
        # 不是设置节点状态
        if self.click_state != click_state_select_node:
            self.click_state = click_state_select_node
            self.map_edit_set_node_id_button.text_str = "设置节点id:开启"
        elif self.click_state == click_state_select_node:
            self.click_state = click_state_free
            self.map_edit_set_node_id_button.text_str = "设置节点id:关闭"
        


# 获取单例
def getInstance():
    name = "MainView"
    ins = instanceMgrMd.instanceMgr.get_ins(name)
    if not ins:
        ins = MainView()
        instanceMgrMd.instanceMgr.set_ins(name, ins)
    return ins