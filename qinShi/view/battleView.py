

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
class BattleView(viewVesselMd.ViewVessel):

    # 图像对象
    # 退出按钮
    exit_image_obj = None
    # 玩家角色
    self_actor_obj = None
    # 敌对角色
    enemy_actor_obj = None

    # 初始化战斗界面
    def __init__(self):
        #调用父类的构函
        viewVesselMd.ViewVessel.__init__(self, Battle_icon)

        # 设置位置
        BattleView.set_pos(self, Init_pos[0], Init_pos[1])

        # 设置鼠标事件
        BattleView.set_click_event(self, BattleView.click_event)

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
        BattleView.set_background(self, Battle_background)
        BattleView.set_pos(self, Init_pos[0], Init_pos[1])
        # 设置关闭按钮
        BattleView.add_close_Button(self, self.click_exit, self)
        

        # 设置战斗
        # 添加玩家角色
        self.self_actor_obj = []
        player_ins = playerMd.Player.getInstance()
        for tmp_actor in player_ins.playInfo["actor_arr"]:
            tmp_actor_obj = actorViewMd.ActorView(tmp_actor["id"], tmp_actor["lv"])
            self.self_actor_obj.append(tmp_actor_obj)
            BattleView.add_son_view(self, tmp_actor_obj)

        # 添加敌对角色
        self.enemy_actor_obj = []


    # 点击退出
    @staticmethod
    def click_exit(self, battle_view):
        print("click_exit")
        # 恢复背景图
        battle_view.set_background(battle_view, Battle_icon)
        # 设置位置
        battle_view.set_pos(battle_view, Init_pos[0], Init_pos[1])

        # 删除子视图
        del battle_view.son_view_arr
        battle_view.son_view_arr = []
        # 删除关闭按钮
        self.close_view = None
