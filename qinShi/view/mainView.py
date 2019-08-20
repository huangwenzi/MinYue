



# 项目模块
import qinShi.view.battleView as battleViewMd

# 这是主界面
class MainView():
    # 主视图对象
    main_view = None
    # 战斗视图对象
    battle_view = None

    # 初始化
    def __init__(self, main_view):
        self.main_view = main_view

        # 初始化其他功能
        # 战斗视图
        self.battle_view = battleViewMd.BattleView("qinShi/resource/view/战斗.png")
        main_view.add_son_view(main_view, self.battle_view)
