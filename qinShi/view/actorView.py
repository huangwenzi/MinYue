
# 三方模块
import pygame
# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.view.viewBase as viewBaseMd
import modules.control.instanceMgr as instanceMgrMd
import qinShi.control.cfgMgr as cfgMgrMd


# 角色视图
class ActorView(viewVesselMd.ViewVessel):
    # 左边的站立图像资源
    left_stand = None
    # 左边的战斗图像资源
    left_attack = None
    # 右边的站立图像资源
    right_stand = None
    # 右边的战斗图像资源
    right_attack = None

    # 初始化战斗界面
    # id : 角色id
    # lv : 角色等级
    def __init__(self, actor_id, lv):
        # 获取对应角色配置
        cfgMgr = cfgMgrMd.getInstance()
        str_id = str(actor_id)
        tmp_cfg = cfgMgr.actor_cfg[str_id]

        # 加载对应的图像资源
        # 加载站立图像资源
        left_stand = "qinShi/resource/actor/actor_%d/i_stand_%d.png"%(actor_id, 0)
        self.left_stand = pygame.image.load(left_stand)
        right_stand = "qinShi/resource/actor/actor_%d/d_stand_%d.png"%(actor_id, 0)
        self.right_stand = pygame.image.load(right_stand)
        # 加载战斗图像资源
        left_attack = []
        for idx in range(2):
            image_path = "qinShi/resource/actor/actor_%d/i_attack_%d.png"%(actor_id, idx)
            left_attack.append(pygame.image.load(image_path))
        self.left_attack = left_attack
        right_attack = []
        for idx in range(2):
            image_path = "qinShi/resource/actor/actor_%d/d_attack_%d.png"%(actor_id, idx)
            right_attack.append(pygame.image.load(image_path))
        self.right_attack = right_attack

        #调用父类的构函
        viewVesselMd.ViewVessel.__init__(self, left_stand)
        # 设置位置
        self.set_pos(0, 0)