# 系统模块
import json

# 项目模块
import modules.control.instanceMgr as instanceMgrMd

# 配置管理器
class CfgMgr():
    # 角色配置
    actor_cfg = None

    # 初始化
    def __init__(self):
        self.actor_cfg = CfgMgr.load_json("qinShi/config/actor.json")
        

    # 获取单例
    @staticmethod
    def getInstance():
        name = "CfgMgr"
        ins = instanceMgrMd.instanceMgr.get_ins(name)
        if not ins:
            ins = CfgMgr()
            instanceMgrMd.instanceMgr.set_ins(name, ins)
        return ins

    # 加载json配置文件
    @staticmethod
    def load_json(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return json.load(f)