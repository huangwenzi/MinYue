
# 项目模块
# 游戏引擎模块
import modules.view.mainView as mainViewMd
import modules.view.button as ButtonMd
import modules.view.inputBox as InputBoxMd
import modules.control.instanceMgr as instanceMgrMd
import modules.config.enum as mouseEnumMd
import modules.view.viewList as viewListMd
# mod模块
import mod_shoot.config.view as ViewCfgMd

# 这是主界面
class MainView(mainViewMd.MainView):
    # 账号输入框
    in_put_account = None
    # 密码
    in_put_password = None
    # 连接按钮
    login_button = None
    # 服务器列表
    ser_view_list = None

    # 下一个icon位置
    icon_x = 0
    icon_y = 0

    # 初始化
    def __init__(self):
        # super().__init__(image_path = ViewCfgMd.viem_main_screen)
        super().__init__(500, 500)
        self.set_fps(ViewCfgMd.viem_main_fps)

        # 初始化其他功能
        # # 输入框
        # # 账号
        # main_width = self.width
        # # main_height = main_view.height
        # in_put_account = InputBoxMd.InputBox(text = "", width = 100, height = 30)
        # in_put_account.set_pos((main_width - in_put_account.width)/2, 100)
        # self.in_put_account = in_put_account
        # self.add_son_view(in_put_account)
        # # 密码
        # in_put_password = InputBoxMd.InputBox(text = "", width = 100, height = 30)
        # in_put_password.set_pos((main_width - in_put_password.width)/2, 130)
        # self.in_put_password = in_put_password
        # self.add_son_view(in_put_password)
        # # 按钮
        # # 连接按钮
        # login_button = ButtonMd.Button(text = "登录", width = 100, height = 100)
        # login_button.set_pos((main_width - login_button.width)/2, 160)
        # self.login_button = login_button
        # self.add_son_view(login_button)
        # login_button.set_mouse_event(mouseEnumMd.mouse_click_open, self, self.login_button_click_event)
        # 列表
        # 服务器列表
        ser_view_list = viewListMd.ViewList(200, 200)
        ser_view_list.set_pos(100, 200)
        self.ser_view_list = ser_view_list
        self.add_son_view(ser_view_list)
        
    # 登录事件
    def login_button_click_event(self, ret_mouse):
        print("login_button_click_event")
        # 连接服务器
        pass
        

# 获取单例
def getInstance():
    name = "MainView"
    ins = instanceMgrMd.instanceMgr.get_ins(name)
    if not ins:
        ins = MainView()
        instanceMgrMd.instanceMgr.set_ins(name, ins)
    return ins