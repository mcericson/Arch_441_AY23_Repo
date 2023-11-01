import rhinoscriptsyntax as rs
import color_tools as ct
import box_tools as bt
import viewport_tools as vt
import random 
from scriptcontext import escape_test

from imp import reload
reload(ct)

#------------------------------------------------------------
#definitions

def cubic_grid(point, x_num, y_num, z_num, cell_size):
    #create empty list to store point values
    point_list = []
    #get point coordinates
    start = rs.AddPoint(point)
    sx, sy, sz = rs.PointCoordinates(start)
    rs.DeleteObject(start)
    #create start values as integers
    start_x, start_y, start_z = int(sx), int(sy), int(sz)
    #create stop values
    stop_x = start_x + (x_num*cell_size)
    stop_y = start_y + (y_num*cell_size)
    stop_z = start_z + (z_num*cell_size)
    #create loops to generate points
    for i in range(start_x, stop_x, cell_size):
        for j in range(start_y, stop_y, cell_size):
            for p in range(start_z, stop_z, cell_size):
                x, y, z = i, j, p
                grid_point = (x, y, z)
                point_list.append(grid_point)
    return point_list

def cull_points(point_list, max):
    new_list = []
    for i in point_list:
        distance = rs.Distance((0,0,0), i)
        if distance > max:
            new_list.append(i)
    return new_list

def rgb_cube(point_list, cell_size):
    for i in point_list:
        box_radius = cell_size/2.0
        box = bt.center_cube(i, box_radius)
        #get min and max values from list
        min = point_list[0][0]
        max = point_list[-1][0]
        color = ct.point_to_rgb(i, min, max)
        ct.assign_material_color(box, color)

def main():
    view_name = "rotate_axon"
    frames = 0
    vt.create_parallel_view(view_name,(1000,1000))
    rs.EnableRedraw(False)
    cell_size = 5
    points = cubic_grid((0,0,0), 10, 10, 10, cell_size)
    culled_points = cull_points(points, 20)
    rgb_cube(culled_points, cell_size)
    rs.ZoomExtents()
    vt.zoom_scale(.5, view_name)
    rs.EnableRedraw(True)
    while frames <= 359:
        escape_test(True)
        rs.Sleep(1)
        frames += 1
        rot_right = 1
        rot_up = 1
        vt.set_axon_view(rot_right, rot_up, view_name)
        file_name = str("%04d"%frames) + "rot_cube"
        #vt.capture_view(1.0, file_name, "rot_cube")


main()