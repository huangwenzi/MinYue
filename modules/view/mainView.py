# 官方模块
import time
import sys

# 三方模块
import pygame

# 项目模块
import modules.view.viewVessel as viewVesselMd
import modules.control.mouse as mouseMd
import modules.config.enum as mouseEnumMd
import modules.control.keyboard as KeyboardMd
import modules.tool.time_tool as TimeToolMd


        

# 这是主界面
class MainView(viewVesselMd.ViewVessel):
    # 控制对象
    mouse = None
    keyboard = None

    # 设置
    fps = 1 # 帧率
    next_update = 0  # 下次刷新界面时间

    # 视图对象
    view_obj = None    # 窗体对象


    # 初始化一个主界面
    def __init__(self, image_path):
        #调用父类的构函
        super().__init__(image_path)
        pygame.display.set_caption(self.name)
        self.view_obj = pygame.display.set_mode((self.width, self.height))
        self.next_update = time.time()
        
    # 游戏循环
    def run(self):
        # 最近的点击对象
        click_ret = None
        mouse = mouseMd.Mouse()
        keyboard = KeyboardMd.Keyboard()
        

        # 游戏循环
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)

            # 界面绘制
            self.draw()

            # 处理鼠标事件
            ret_mouse = mouse.mouse_event()
            new_click_ret = self.check_click(ret_mouse, [0,0])
            # 鼠标点下
            if ret_mouse.type == mouseEnumMd.mouse_click_down:  
                if new_click_ret:
                    click_ret = new_click_ret
                    click_ret.mouse_event_star(ret_mouse)  
            elif ret_mouse.type == mouseEnumMd.mouse_click_open:  # 鼠标弹起
                if click_ret == new_click_ret:  # 点下和弹起是同一对象
                    click_ret.mouse_event_star(ret_mouse)
            elif ret_mouse.type == mouseEnumMd.mouse_click_drag:  # 鼠标拖动
                # 左键点下，且位置变化
                click_ret.mouse_event_star(ret_mouse)
              
                        

            # 键盘事件
            # new_dowm_map,new_up_map,now_dowm_map = keyboard.keyboard_event()
            # for item in new_dowm_map:
            #     print("new_dowm:" + item)
            # for item in new_up_map:
            #     print("new_up:" + item)
            if click_ret:
                click_ret.keyboard_star(keyboard)
                       

            # 检查热更（可以分线程去检查）

    # 图像设置函数
    # 主界面绘制
    # 也是调用其他界面绘制的地方
    def draw(self):
        # 根据帧率刷新
        now = time.time()
        if now < self.next_update:
            return
        super().draw(self.view_obj, (0, 0))
        # update()绘制变化部分 flip()绘制全部
        # pygame.display.flip()
        pygame.display.update() 
        # 更新刷新时间
        self.next_update = now + self.fps

    # 获取点击的对象
    def check_click(self, click_pos, father_pos):
        # 是否在范围内
        ret = super().check_click(click_pos, father_pos)
        return ret

    # 设置帧率
    def set_fps(self, new_fps):
        self.fps = new_fps
