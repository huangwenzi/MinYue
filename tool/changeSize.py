

# 修改图片大小
import tool.imageTool as imageToolMd
# 图标
icon_path = [
    # "qinShi/resource/view/actor.png",
    # "qinShi/resource/view/battle.png",
    # "qinShi/resource/view/formation.png",
    # "qinShi/resource/view/knapsack.png",
    # "qinShi/resource/view/save.png",
    # "qinShi/resource/view/takeCard/takeCard.png",
]
imageToolMd.change_size(icon_path, [50,50])

# 背景图
background_path = [
    # "qinShi/resource/view/takeCard/takeCard.png",
]
imageToolMd.change_size(background_path, [720,1136])

# 背景图——1
_background_path_1 = [
    # "qinShi/resource/view/takeCard/background.png",
]
imageToolMd.change_size(_background_path_1, [720,200])

# 
_192_56 = [
    "qinShi/resource/view/takeCard/ten.png",
]
imageToolMd.change_size(_192_56, [192,56])