

# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.instanceMgr as instanceMgrMd
import qinShi.view.actorView as actorViewMd
import qinShi.control.player as playerMd

# 初始位置
Init_pos = [0,0]
# 战斗图
Battle_background = "qinShi/resource/screen/battle.jpg"
# 退出图标
Exit_icon = "qinShi/resource/view/exit.png"
# 战斗图标
Battle_icon = "qinShi/resource/view/battle.png"

# 战斗界面视图
class BattleView(viewVesselMd.viewVessel):
    pass

    # 初始化战斗界面
    def __init__(self):
        #调用父类的构函
        viewVesselMd.viewVessel.__init__(self, Battle_icon)

        # 设置位置
        self.set_pos(self, Init_pos[0], Init_pos[1])

        # 设置鼠标事件
        self.set_click_event(self, BattleView.click_event, self)

    # 获取单例
    @staticmethod
    def getInstance():
        name = "BattleView"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = BattleView()
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins

    # 事件函数
    # 点击事件
    @staticmethod
    def click_event(self):
        # 设置战斗背景图
        self.set_background(self, Battle_background)
        self.set_pos(self, Init_pos[0], Init_pos[1])

        # 设置退出按钮
        # 设置退出图标和位置
        self.exit_image_obj = viewBaseMd.viewBase(Exit_icon)
        exit_width = self.exit_image_obj.width
        exit_height = self.exit_image_obj.height
        x = self.width - exit_width
        y = 0
        self.exit_image_obj.set_pos(self.exit_image_obj, x, y)
        self.add_son_view(self, self.exit_image_obj)
        # 设置退出函数
        self.exit_image_obj.set_click_event(self.exit_image_obj, self.click_exit, self)

        # 设置战斗
        # 添加玩家角色
        self.self_actor_obj = []
        player_ins = playerMd.Player.getInstance()
        for tmp_actor in player_ins.playInfo["actor_arr"]:
            tmp_actor_obj = actorViewMd.ActorView(tmp_actor["id"], tmp_actor["lv"])
            self.self_actor_obj.append(tmp_actor_obj)
            self.add_son_view(self, tmp_actor_obj)

    # 点击退出
    @staticmethod
    def click_exit(self):
        print("click_exit")
        # 恢复背景图
        self.set_background(self, Battle_icon)
        # 设置位置
        self.set_pos(self, Init_pos[0], Init_pos[1])

        # 删除子视图
        del self.son_view_arr
        self.son_view_arr = []
