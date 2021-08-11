# 系统模块
import sys

# 三方模块
import pygame
import pygame.freetype

pygame.init()
# pygame.freetype.init()

# 项目模块
# 游戏引擎模块
# import modules.control.hotUp as hotUpMd
import modules.control.mouse as mouseMd
import modules.config.enum as mouseEnumMd
import modules.control.keyboard as KeyboardMd
import modules.tool.time_tool as TimeToolMd


# 组件游戏模块
import mod_shoot.view.main_view as ModMainViewMd


# 开始运行文件
def run():
    # 创建基础界面
    main_view = ModMainViewMd.getInstance()
    mouse = mouseMd.Mouse()
    keyboard = KeyboardMd.Keyboard()
    # 初始化数据

    # 最近的点击对象
    click_ret = None
    # 游戏循环
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
        # 界面绘制
        main_view.main_view.draw()

        # 处理鼠标事件
        ret_mouse = mouse.mouse_event()
        if ret_mouse.type == mouseEnumMd.mouse_click_open:
            click_ret = main_view.main_view.check_click(ret_mouse, [0,0])
            if click_ret:
                if hasattr(click_ret, "click_func"):
                    click_ret.click_star()

        # 键盘事件
        # new_dowm_map,new_up_map,now_dowm_map = keyboard.keyboard_event()
        # for item in new_dowm_map:
        #     print("new_dowm:" + item)
        # for item in new_up_map:
        #     print("new_up:" + item)
        if click_ret:
            if hasattr(click_ret, "keyboard_fun"):
                click_ret.keyboard_fun(keyboard)

        


        # 检查热更（可以分线程去检查）



run()