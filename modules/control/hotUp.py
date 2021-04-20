# 系统模块
from imp import reload
# 三方模块

# 项目模块
import modules.control.instanceMgr as instanceMgrMd

# 热更模块
class HotUp():
    # 实例管理器
    example_dict = {}

    def __init__(self):
        self.example_dict = {}

    # 热更主函数
    @staticmethod
    def hot_up(self, path_arr):
        for tmp_path in path_arr:
            obj = reload(tmp_path)
            # 下面是对加入实例管理器的实例热更
            # 热更需要对象带有热更名字段
            if "hot_up_name" in obj and obj.hot_up_name in self.example_dict:
                fun_arr = obj.fun_arr
                for tmp_obj in self.example_dict[obj.hot_up_name]:
                    for fun_name in fun_arr:
                        setattr(tmp_obj, fun_name, obj.__dict__[fun_name])
    
    # 加入热更实例管理器
    @staticmethod
    def app_mgr(obj, name):
        ins = getInstance()
        if name in ins.example_dict:
            ins.example_dict[name].append(obj)
        else:
            ins.example_dict[name] = [obj]
            
        
# 获取单例
def getInstance():
    name = "HotUp"
    ins = instanceMgrMd.instanceMgr.get_ins(name)
    if not ins:
        ins = HotUp()
        instanceMgrMd.instanceMgr.set_ins(name, ins)
    return ins