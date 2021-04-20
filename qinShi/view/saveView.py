

# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.instanceMgr as instanceMgrMd
import qinShi.view.actorView as actorViewMd
import qinShi.control.player as playerMd

# 初始位置
Init_pos = [40,0]
# 保存图标
Save_icon = "qinShi/resource/view/save.png"

# 保存图标
class SaveView(viewBaseMd.ViewBase):
    pass

    # 初始化战斗界面
    def __init__(self):
        #调用父类的构函
        super().__init__(Save_icon)

        # 设置位置
        self.set_pos(Init_pos[0], Init_pos[1])

        # 设置鼠标事件
        self.set_click_event(self.click_event)

    # 事件函数
    # 点击事件
    def click_event(self):
        player_ins = playerMd.getInstance()
        player_ins.save_data()

# 获取单例
def getInstance():
    name = "SaveView"
    ins = instanceMgrMd.instanceMgr.get_ins(name)
    if not ins:
        ins = SaveView()
        instanceMgrMd.instanceMgr.set_ins(name, ins)
    return ins