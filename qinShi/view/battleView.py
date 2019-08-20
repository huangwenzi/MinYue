

# 项目模块
import modules.view.viewVessel as viewVesselMd

# 战斗界面视图
class BattleView(viewVesselMd.viewVessel):
    pass

    # 初始化战斗界面
    def __init__(self, image_path):
        #调用父类的构函
        viewVesselMd.viewVessel.__init__(self, image_path)
