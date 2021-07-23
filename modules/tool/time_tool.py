# 官方模块
import time

# 项目模块
import modules.control.instanceMgr as instanceMgrMd

# 时间工具模块
class TimeTool():
    # 时间消耗标志字典
    consume_time_dict = {}  # {key = begin_time}

    def __init__(self):
        self.consume_time_dict = {}

# 获取单例
def getInstance():
    name = "HotUp"
    ins = instanceMgrMd.instanceMgr.get_ins(name)
    if not ins:
        ins = TimeTool()
        instanceMgrMd.instanceMgr.set_ins(name, ins)
    return ins


# 消耗记时开始
def consume_time_begin(Type):
    ins = getInstance()
    ins.consume_time_dict[Type] = time.time()

# 消耗记时结束
def consume_time_end(Type):
    ins = getInstance()
    now = time.time()
    consume = now - ins.consume_time_dict[Type]
    ins.consume_time_dict[Type] = now
    # 大于0.01秒才打印
    if consume > 0.01:
        print("consume_time Type : {0}, {1}".format(Type, consume))














