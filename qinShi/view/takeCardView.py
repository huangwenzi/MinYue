

# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.instanceMgr as instanceMgrMd
import qinShi.view.actorView as actorViewMd
import qinShi.control.player as playerMd

# 初始位置
_init_pos = [40,0]
# 保存图标
_Icon = "qinShi/resource/view/takeCard.png"

# 保存图标
class takeCardView(viewBaseMd.ViewBase):
    pass

    # 初始化抽卡界面
    def __init__(self):
        #调用父类的构函
        viewVesselMd.ViewVessel.__init__(self, _Icon)
        # 设置位置
        self.set_pos(_init_pos[0], _init_pos[1])
        # 设置鼠标事件
        self.set_click_event(takeCardView.click_event)

    # 获取单例
    @staticmethod
    def getInstance():
        name = "takeCardView"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = takeCardView()
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins

    # 事件函数
    # 点击事件
    def click_event(self):
        player_ins = playerMd.Player.getInstance()
        player_ins.save_data()
