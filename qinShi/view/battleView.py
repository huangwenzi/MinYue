

# 项目模块
import modules.view.viewVessel as viewVesselMd

# 初始位置
Init_pos = [0,0]
# 战斗图
Battle_background = "qinShi/resource/screen/battle.jpg"

# 战斗界面视图
class BattleView(viewVesselMd.viewVessel):
    pass

    # 初始化战斗界面
    def __init__(self, image_path):
        #调用父类的构函
        viewVesselMd.viewVessel.__init__(self, image_path)

        # 设置位置
        self.set_pos(self, Init_pos[0], Init_pos[1])

        # 设置鼠标事件
        self.set_click_event(self, BattleView.click_battle)

    # 事件函数
    # 点击战斗
    @staticmethod
    def click_battle(self):
        # 设置战斗背景图
        self.set_background(self, Battle_background)
        self.set_pos(self, Init_pos[0], Init_pos[1])
        # 设置退出按钮
