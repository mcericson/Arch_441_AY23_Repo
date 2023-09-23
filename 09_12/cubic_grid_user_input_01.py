#mark ericson 9/12/23
#Program for interactive grid

import rhinoscriptsyntax as rs
import random 

def random_color(object_id):
    r = random.randint(0,100)
    g = random.randint(0,100)
    b = random.randint(0,255)
    color = rs.CreateColor(r, g, b)
    rs.ObjectColor(object_id, color)

def lines(point_list):
    for i in range(len(point_list)):
        point_1 = point_list[i-1]
        point_2 = point_list[i]
        line = rs.AddLine(point_1, point_2)
        random_color(line)

def cubic_grid(point, x_num, y_num, z_num, cell_size):
    point_list = []
    start = rs.AddPoint(point)
    sx, sy, sz = rs.PointCoordinates(start)
    start_x, start_y, start_z = int(sx), int(sy), int(sz)
    rs.DeleteObject(start)
    
    stop_x = start_x + (x_num * cell_size)
    stop_y = start_y + (y_num * cell_size)
    stop_z = start_z + (z_num * cell_size)
    
    for i in range(start_x, stop_x, cell_size):
        for j in range(start_y, stop_y, cell_size):
            for p in range(start_z, stop_z, cell_size):
                x, y, z = i, j, p
                grid_point = rs.AddPoint(x, y, z)
                random_color(grid_point)
                point_list.append(grid_point)
    return point_list


rs.EnableRedraw(False)
point = rs.GetPoint()

points = cubic_grid(point, 10, 10, 10, 10)
lines(points)