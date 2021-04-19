# 系统库
import os
# 第三方官方库
from PIL import Image

# 图像处理工具                  
# 修改图片大小
def change_size(file_arr, size):
    for tmp_file in file_arr:
        im = Image.open(tmp_file)
        out = im.resize( ( size[0],size[1]))
        file_name = os.path.basename(tmp_file)
        out.save("./tool/image/" + file_name)