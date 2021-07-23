

# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.instanceMgr as instanceMgrMd
import qinShi.view.actorView as actorViewMd
import qinShi.control.player as playerMd

# 保存图标
Save_icon = "qinShi/resource/view/save.png"

# 保存图标
class SaveView(viewBaseMd.ViewBase):
    pass

    # 初始化战斗界面
    def __init__(self):
        #调用父类的构函
        super().__init__(Save_icon)

        # 设置鼠标事件
        self.set_click_event(self.click_event)

    # 事件函数
    # 点击事件
    def click_event(self):
        player_ins = playerMd.getInstance()
        player_ins.save_data()

