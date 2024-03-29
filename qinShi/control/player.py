# 系统模块
import json
# 项目模块
import modules.control.instanceMgr as instanceMgrMd

# 保存数据地址
Save_path = "qinShi/playData/player_1.json"

# 玩家数据类
class Player():
    playInfo = None

    # 初始化
    def __init__(self):
        # 加载数据
        with open(Save_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
            self.playInfo = data
        
    # 保存数据
    def save_data(self):
        with open(Save_path, 'w', encoding='utf-8', errors='ignore') as f_out:
            f_out.write(json.dumps(self.playInfo, ensure_ascii=False, indent=2))

# 获取单例
def getInstance():
        name = "Player"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = Player()
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins