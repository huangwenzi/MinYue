import random
 


# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.instanceMgr as instanceMgrMd
import qinShi.view.actorView as actorViewMd
import qinShi.control.player as playerMd

# 抽卡图标
_icon = "qinShi/resource/view/actor.png"
_battle_background = ""

# 英雄列表
class ActorListView(viewVesselMd.ViewVessel):
    pass

    # 初始化英雄列表界面
    def __init__(self):
        #调用父类的构函
        super().__init__(_icon)
        # # 设置位置
        # self.set_pos(_init_pos[0], _init_pos[1])
        # 设置鼠标事件
        self.set_click_event(self.click_event)
    
   # 点击事件
    def click_event(self):
        # 设置战斗背景图
        self.set_background(_battle_background)
        self.set_pos(0, 0)
        # 设置关闭按钮
        self.add_close_Button(self.click_exit, self)
        

        # 设置战斗
        # 添加玩家角色
        self.self_actor_obj = []
        player_ins = playerMd.getInstance()
        for tmp_actor in player_ins.playInfo["actor_arr"]:
            tmp_actor_obj = actorViewMd.ActorView(tmp_actor["id"], tmp_actor["lv"])
            self.self_actor_obj.append(tmp_actor_obj)
            self.add_son_view(tmp_actor_obj)

        # 添加敌对角色
        self.enemy_actor_obj = []


    # 点击退出
    def click_exit(self, battle_view):
        # 恢复背景图
        battle_view.set_background(_battle_icon)
        # 设置位置
        battle_view.return_init_pos()

        # 删除子视图
        del battle_view.son_view_arr
        battle_view.son_view_arr = []
        # 删除关闭按钮
        self.close_view = None