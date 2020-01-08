



# 项目模块
import modules.control.instanceMgr as instanceMgrMd
import qinShi.view.battleView as battleViewMd
import qinShi.view.saveView as saveViewMd
import qinShi.view.takeCardView as takeCardViewMd
import qinShi.control.player as playerMd


# 这是主界面
class MainView():
    # 主视图对象
    main_view = None
    # 战斗视图对象
    battle_view = None

    # 初始化
    def __init__(self, main_view):
        self.main_view = main_view

        # 加载玩家数据
        playerMd.Player.getInstance()

        # 初始化其他功能
        # 战斗视图
        self.battle_view = battleViewMd.BattleView.getInstance()
        main_view.add_son_view(self.battle_view)
        # 保存功能
        self.save_view = saveViewMd.SaveView.getInstance()
        main_view.add_son_view(self.save_view)
        # 抽卡功能
        self.take_card_view = takeCardViewMd.TakeCardView.getInstance()
        main_view.add_son_view(self.take_card_view)

    # 获取单例
    @staticmethod
    def getInstance(main_view):
        name = "MainView"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = MainView(main_view)
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins