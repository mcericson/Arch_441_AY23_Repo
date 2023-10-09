import rhinoscriptsyntax as rs
import color_tools as ct
import viewport_tools as vt
import random 

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
                r, g, b = ct.point_to_rgb(grid_point,start_x, stop_x)
                color = rs.CreateColor(r, g, b)
                point_a = rs.AddPoint(grid_point)
                rs.ObjectColor(point_a, color)
                point_list.append(grid_point)

    return point_list

def color_curves(point_list):
    for i in range(len(point_list)):
        p_1 = point_list[i]
        p_2 = point_list[i-1]
        p_3 = point_list[i-2]
        p_4 = point_list[i-3]
        min = point_list[0][0]
        max = point_list[-1][0]
        r, g, b = ct.point_to_rgb(p_1, min, max)
        color = rs.CreateColor(r, g, b)
        curve_points = [p_1, p_2, p_3, p_4]
        curve = rs.AddCurve(curve_points, 3)
        rs.ObjectColor(curve, color)
def random_curves(point_list):
    for i in range(len(point_list)):
        min_index = 0
        max_index = len(point_list)-1
        index_1 = random.randint(min_index, max_index)
        index_2 = random.randint(min_index, max_index)
        index_3 = random.randint(min_index, max_index)
        index_4 = random.randint(min_index, max_index)
        p_1 = point_list[index_1]
        p_2 = point_list[index_2]
        p_3 = point_list[index_3]
        p_4 = point_list[index_4]
        min = point_list[0][0]
        max = point_list[-1][0]
        r, g, b = ct.point_to_rgb(p_1, min, max)
        color = rs.CreateColor(r, g, b)
        curve_points = [p_1, p_2, p_3, p_4]
        curve = rs.AddCurve(curve_points, 3)
        rs.ObjectColor(curve, color)

#-------------------------------------------------------------
#main

def main():
    
    vt.create_parallel_view('color_axo', (800, 800))
    vt.set_axon_view(45, 120, "color_axo")
    point = (0,0,0)
    rs.EnableRedraw(False)
    points = cubic_grid(point, 10, 10, 10, 10)
    random_curves(points)
    rs.ZoomExtents()
    vt.capture_view(2.0, "color_axo", "color_fun")

main()