import random
 


# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.instanceMgr as instanceMgrMd
import qinShi.view.actorView as actorViewMd
import qinShi.control.player as playerMd

# 初始位置
_init_pos = [80,0]
# 抽卡图标
_icon = "qinShi/resource/view/takeCard/takeCard.png"
_one = "qinShi/resource/view/takeCard/one.png"
_ten = "qinShi/resource/view/takeCard/ten.png"
_background = "qinShi/resource/view/takeCard/background.png"

# 抽卡图标
class TakeCardView(viewVesselMd.ViewVessel):
    pass

    # 初始化抽卡界面
    def __init__(self):
        #调用父类的构函
        viewVesselMd.ViewVessel.__init__(self, _icon)
        # 设置位置
        self.set_pos(_init_pos[0], _init_pos[1])
        # 设置鼠标事件
        self.set_click_event(self.click_event)

        # 抽卡展示图
        self.show_view_arr = None
    # 获取单例
    @staticmethod
    def getInstance():
        name = "TakeCardView"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = TakeCardView()
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins
    
    # 删除旧的展示图
    def remove_show_view(self):
        # 删除展示图像
        if self.show_view_arr:
            for tmp_show_view in self.show_view_arr:
                idx = 0
                for tmp_view in self.son_view_arr:
                    if tmp_view == tmp_show_view:
                        del self.son_view_arr[idx]
                        break
                    idx += 1
            self.show_view_arr = None
            

    # 事件函数
    # 点击事件
    def click_event(self):
        # 弹出抽卡界面
        # 设置战斗背景图
        self.set_background(_background)
        self.set_pos(0, 0)
        # 设置关闭按钮
        self.add_close_Button(self.click_exit)

        # 设置两个抽卡选项
        # 抽一次
        self.one_view = viewBaseMd.ViewBase(_one)
        self.one_view.set_click_event(self.click_take_card, {"obj":self, "count":1})
        x = 200
        y = 50
        self.one_view.set_pos(x, y)
        self.add_son_view(self.one_view)
        # 抽十次
        self.ten_view = viewBaseMd.ViewBase(_ten)
        self.ten_view.set_click_event(self.click_take_card, {"obj":self, "count":10})
        x = 400
        y = 50
        self.ten_view.set_pos(x, y)
        self.add_son_view(self.ten_view)
    # 点击退出
    def click_exit(self):
        # 恢复背景图
        self.set_background(_icon)
        # 设置位置
        self.set_pos(_init_pos[0], _init_pos[1])

        # 删除子视图
        del self.son_view_arr
        self.son_view_arr = []
        # 删除关闭按钮
        self.close_view = None
        self.remove_show_view()
    # 点击抽卡
    def click_take_card(self, argv):
        obj = argv["obj"]
        num = argv["count"]
        # 删除旧的展示图
        obj.remove_show_view()
        obj.show_view_arr = []
        for idx in range(0, num):
            # 随机抽取
            rand = random.randint(0,7)
            path = "qinShi/resource/view/actor/actor_%d/i_attack_0.png"%(rand)
            # 展示结果
            tmp_show_card_view = viewBaseMd.ViewBase(path)
            tmp_show_card_view.set_click_event(obj.click_take_card_close, {"obj":obj, "tmp_show_card_view":tmp_show_card_view})
            x = idx%5 * 60
            y = idx//5 * 80
            tmp_show_card_view.set_pos(x, y)
            obj.add_son_view(tmp_show_card_view)
            obj.show_view_arr.append(tmp_show_card_view)
    # 关闭卡牌展示
    def click_take_card_close(self, argv):
        obj = argv["obj"]
        tmp_show_card_view = argv["tmp_show_card_view"]
        # 删除展示图像
        idx = 0
        for tmp_view in obj.son_view_arr:
            if tmp_view == tmp_show_card_view:
                del obj.son_view_arr[idx]
                break
            idx += 1
        del tmp_show_card_view
        
