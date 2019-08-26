

# 修改图片大小
import tool.imageTool as imageToolMd
path = [
    "qinShi/resource/view/actor.png",
    "qinShi/resource/view/battle.png",
    "qinShi/resource/view/formation.png",
    "qinShi/resource/view/knapsack.png",
    "qinShi/resource/view/save.png",
]
imageToolMd.ImageTool.change_size(path, [50,50])