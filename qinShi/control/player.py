# 系统模块
import json
# 项目模块
import modules.control.instanceMgr as instanceMgrMd

# 保存数据地址
sava_path = "qinShi/playData/play_1.json"

# 玩家数据类
class Player():
    playInfo = None

    # 初始化
    def __init__(self):
        # 加载数据
        with open(sava_path, 'r', encoding='utf-8', errors='ignore') as f:
            self.playInfo = json.load(f)
    
    # 获取单例
    @staticmethod
    def getInstance():
        name = "Player"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = Player()
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins
        