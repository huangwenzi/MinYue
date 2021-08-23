# 官方库
import pygame




# 图像辅助模块

# 图像点对象
class view_dot(object):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 图像点对象
class view_rect(object):
    x = 0
    y = 0
    w = 0
    h = 0
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h  
    


# 矩形
# 点是否在矩形内
# rect : (x,y,w,h)
def dot_in_rect(dot_pos, rect):
    if dot_pos.x > rect.x and (rect.x + rect.w) > dot_pos.x and dot_pos.y > rect.y and (rect.y + rect.h) > dot_pos.y:
        return True
    return False

# a矩形是否在b矩形内
def rect_in_rect(rect_a, rect_b):
    if rect_a.x > rect_b.x + rect_b.w \
        or rect_a.x + rect_a.w < rect_b.x \
        or rect_a.y > rect_b.y + rect_b.h\
        or rect_a.y + rect_a.h < rect_b.y:
        # 超出范围不绘制
        return False
    return True

# a矩形在b矩形内的部分
def get_rect_in_rect_part(rect_a, rect_b):
    ret_rect = view_rect(rect_a.x, rect_a.y, rect_a.w, rect_a.h)
    have_change = False
    # 修正超出范围的地方
    if rect_a.x < rect_b.x: # ret_rect.x的位置修正
        ret_rect.x = rect_b.x - rect_a.x
        ret_rect.w -= ret_rect.x
        have_change = True
    if rect_a.y < rect_b.y: # ret_rect.y的位置修正
        ret_rect.y = rect_b.y - rect_a.y
        ret_rect.h -= ret_rect.y
        have_change = True
    if rect_b.w - ret_rect.x < ret_rect.w: # ret_rect.w的位置修正
        ret_rect.w = rect_b.w - ret_rect.x
        have_change = True
    if rect_b.h - ret_rect.y < ret_rect.h: # ret_rect.w的位置修正
        ret_rect.h = rect_b.h - ret_rect.y
        have_change = True
    return have_change,ret_rect

# view_rect to pygame_rect
def view_rect_to_pygame_rect(rect):
    return pygame.Rect(rect.x, rect.y, rect.w, rect.h)




# 菱形
# 获取菱形的点坐标
def get_rhombus_pos(pos_dot, w, h):
    pos_1 = (pos_dot.x, pos_dot.y + h/2)
    pos_2 = (pos_dot.x + w/2, pos_dot.y)
    pos_3 = (pos_dot.x + w, pos_dot.y + h/2)
    pos_4 = (pos_dot.x + w/2, pos_dot.y + h)
    return pos_1,pos_2,pos_3,pos_4

# 点是否在菱形中
def dot_in_rhombus(pos_dot, rect):
    # 减去菱形的绝对坐标偏移，和中心点相对绝对坐标的偏移
    pos_abs_x = pos_dot.x - rect.x - rect.w/2   
    pos_abs_y = pos_dot.y - rect.y - rect.h/2
    return abs(pos_abs_x*rect.h/2) + abs(pos_abs_y*rect.w/2) < rect.h*rect.w/4

