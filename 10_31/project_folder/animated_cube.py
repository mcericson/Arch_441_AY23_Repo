#mark ericson
#Script to animate an rgb cube


#imports-----------------------------------------

import rhinoscriptsyntax as rs
import box_tools as bt
import color_tools as ct
import viewport_tools as vt
from scriptcontext import escape_test



def cubic_grid(x_num, y_num, z_num, cell_size):
    point_list = []
    for i in range(0, x_num * cell_size, cell_size):
        for j in range(0, y_num * cell_size, cell_size):
            for p in range(0, z_num * cell_size, cell_size):
                x = i
                y = j
                z = p
                point = (x, y, z)
                point_list.append(point)
    return point_list

def rgb_cube(point_list, cell_size):
    radius = cell_size/2
    min = point_list[0][0]
    max = point_list[-1][0]
    for i in point_list:
        cube = bt.center_cube(i, radius)
        color = ct.point_to_rgb(i, min, max)
        ct.assign_material_color(cube, color)



def main():
    rs.EnableRedraw(False)
    vt.create_parallel_view("rot_axo", (800,800))
    points = cubic_grid(10, 10, 10, 1)
    rs.ZoomExtents()
    rgb_cube(points, 1)
    frames = 0
    rs.EnableRedraw(True)
    while frames <= 10:
        escape_test(True)
        frames += 1
        rot_right = 1
        rot_up = 1
        file_name = str(frames) + 'rot_cube'
        vt.set_axon_view(rot_right, rot_up, "rot_axo")
        vt.capture_view(1.0, file_name, 'rot_cube')



main()