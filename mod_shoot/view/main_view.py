
# 项目模块
# 游戏引擎模块
import modules.view.mainView as mainViewMd
import modules.view.button as ButtonMd
import modules.control.instanceMgr as instanceMgrMd
# mod模块
import mod_shoot.config.view as ViewCfgMd

# 这是主界面
class MainView():
    # 主视图对象
    main_view = None
    # 连接按钮
    login_button = None

    # 下一个icon位置
    icon_x = 0
    icon_y = 0

    # 初始化
    def __init__(self):
        main_view = mainViewMd.MainView(ViewCfgMd.viem_main.screen)
        main_view.set_fps(ViewCfgMd.viem_main.fps)
        self.main_view = main_view

        # 初始化其他功能
        # 连接按钮
        login_button = ButtonMd.Button(text = "登录", width = 100, height = 100)
        self.login_button = login_button
        main_view.add_son_view(login_button)
        login_button.set_click_event(self.login_button_click_event, self)
        
    # 登录事件
    def login_button_click_event(obj, self):
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