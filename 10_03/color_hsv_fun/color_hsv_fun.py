import rhinoscriptsyntax as rs
import color_tools as ct
import viewport_tools as vt
import random 
from math import radians, cos, sin, atan2, degrees
from imp import reload
import Rhino
reload(ct)



def cylindrical_points(radius, height, draw_points=False):
    points = []
    for i in range(0,360, 10):
        angle = radians(i)
        for j in range(int(radius)):
            x = cos(angle) * j
            y = sin(angle) * j
            for p in range(int(height)):
                z = p
                point_coord = (x, y, z)
                points.append(point_coord)
                if draw_points == True:
                    h, s, v = point_to_hsv(point_coord, radius, height)
                    r, g, b =  ct.hsv_to_rgb(h, s, v)
                    color = rs.CreateColor(abs(r),abs( g), abs(b))
                    point = rs.AddPoint(point_coord)
                    rs.ObjectColor(point,color)
                
    return points

def point_to_hsv(point, max_radius, max_height):
    x, y, z = point
    distance = rs.Distance(point, (0,0,0))
    s = ct.remap(distance, 0, max_radius, 0.0, 1.0)
    v = ct.remap(z, 0, max_height, 0.0, 1.0)
    angle = degrees(atan2(x, y))
    h = ct.remap(angle, 0, 360, 0.0, 1.0)
    return h, s, v 

def random_curves(point_list):
    for i in range(len(point_list)):
        min_index = 0
        max_index = len(point_list) -1
        index_1 = random.randint(min_index, max_index)
        index_2 = random.randint(min_index, max_index)
        index_3 = random.randint(min_index, max_index)
        index_4 = random.randint(min_index, max_index)
        p_1 = point_list[index_1]
        p_2 = point_list[index_2]
        p_3 = point_list[index_3]
        p_4 = point_list[index_4]
        curve_points = [p_1, p_2, p_3, p_4]
        min = point_list[0][0]
        max = point_list[-1][0]
        r, g, b = ct.point_to_rgb(p_1, min, max)
        color = rs.CreateColor(r, g, b)
        curve = rs.AddCurve(curve_points)
        rs.ObjectColor(curve, color)

def main():
    rs.EnableRedraw(False)
    points = cylindrical_points(10, 10, True)
    random_curves(points)

 
    


if __name__ == "__main__":
    main()