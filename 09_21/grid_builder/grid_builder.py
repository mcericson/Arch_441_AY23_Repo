
import random
from scriptcontext import escape_test
import viewport_tools as vt
import color_tools as ct
from imp import reload
reload(vt)
reload(ct)
import rhinoscriptsyntax as rs



#program definitions


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
                r, g, b = ct.point_to_rgb(grid_point, start_x, stop_x)
#                point = rs.AddPoint(x, y, z)
#                color = rs.CreateColor(r, g, b)
#                rs.ObjectColor(point, color)
                point_list.append(grid_point)

    return point_list


# main program all calls of other functions should be in here
def main():
    point = 0,0,0
    end_point = rs.GetPoint()
    rs.EnableRedraw(False)
    points = cubic_grid(point, 50, 50, 20, 10)
    for i in range(len(points)):
        max_index = len(points) - 1
        index_1 = random.randint(0, max_index)
        index_2 = random.randint(0, max_index)
        index_3 = random.randint(0, max_index)
        point_4 = end_point
        point_list = [points[index_1], points[index_2], points[index_3], point_4]
        
        rs.AddText
        curve = rs.AddCurve(point_list, 3)
        r, g, b = ct.point_to_rgb(points[index_1],0, 200)
        color = rs.CreateColor(r, g, b)
        text = str(r)+ "," +  str(g) + "," + str(b)
        label = rs.AddText(text, points[index_1], .5)
        rs.ObjectColor(curve, color)
        rs.ObjectColor(label, color)
    



main()
