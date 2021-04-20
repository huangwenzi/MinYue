# 系统模块
import sys

# 三方模块
import pygame

# 项目模块
# 游戏引擎模块
import modules.view.mainView as mainViewMd
# import modules.control.hotUp as hotUpMd
import modules.control.mouse as mouseMd
import modules.config.enum as mouseEnumMd
# 组件游戏模块
import qinShi.view.mainView as QSmainViewMd

# 开始运行文件
def run():
    # 创建基础界面
    main_view = mainViewMd.MainView('qinShi/resource/screen/main.jpg')
    # 初始化界面功能
    qs_main_view = QSmainViewMd.getInstance(main_view)
    mouse = mouseMd.Mouse()

    # 游戏循环
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
        # 界面绘制
        qs_main_view.main_view.draw()

        # 处理鼠标事件
        ret_mouse = mouse.mouse_event()
        if ret_mouse.type == mouseEnumMd.mouse_click_open:
            click_ret = qs_main_view.main_view.check_click(ret_mouse, [0,0])
            if click_ret and click_ret.click_func:
                click_ret.click_star()

        # 检查热更（可以分线程去检查）


run()