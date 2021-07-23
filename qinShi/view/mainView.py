



# 项目模块
import modules.control.instanceMgr as instanceMgrMd
import modules.view.label as labelMd
import qinShi.view.battleView as battleViewMd
import qinShi.view.saveView as saveViewMd
import qinShi.view.takeCardView as takeCardViewMd
import qinShi.view.actorListView as actorListViewMd
import qinShi.control.player as playerMd
import qinShi.control.cfgMgr as CfgMgrMd
cfg_mgr = CfgMgrMd.getInstance()

# 这是主界面
class MainView():
    # 主视图对象
    main_view = None
    # 战斗视图对象
    battle_view = None

    # 下一个icon位置
    icon_x = 0
    icon_y = 0

    # 初始化
    def __init__(self, main_view):
        self.main_view = main_view

        # 初始化其他功能
        # 战斗视图
        self.battle_view = battleViewMd.BattleView()
        self.self_add_son_view(self.battle_view)
        # 保存功能
        self.save_view = saveViewMd.SaveView()
        self.self_add_son_view(self.save_view)
        # 抽卡功能
        self.take_card_view = takeCardViewMd.TakeCardView()
        self.self_add_son_view(self.take_card_view)
        # 英雄
        self.take_card_view = actorListViewMd.ActorListView()
        self.self_add_son_view(self.take_card_view)
        # # label
        # label = labelMd.Label()
        # self.self_add_son_view(label)
    
    # 本对象添加子视图
    def self_add_son_view(self, son_view):
        self.main_view.add_son_view(son_view)
        x,y = self.get_next_pos()
        son_view.set_pos(x,y)
        son_view.set_init_pos(x,y)

    # 下一个icon位置
    def get_next_pos(self):
        next_x = self.icon_x
        next_y = self.icon_y

        width = self.main_view.width
        self.icon_x += cfg_mgr.game_cfg["main_icon_size"]["date"][0]
        # 是否要另起一行
        if self.icon_x > width:
            self.icon_x = 0
            self.icon_y = self.icon_y + cfg_mgr.game_cfg["main_icon_size"]["date"][1]
        return next_x,next_y
        
        

# 获取单例
def getInstance(main_view):
    name = "MainView"
    ins = instanceMgrMd.instanceMgr.get_ins(name)
    if not ins:
        ins = MainView(main_view)
        instanceMgrMd.instanceMgr.set_ins(name, ins)
    return ins