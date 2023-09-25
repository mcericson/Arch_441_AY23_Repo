import rhinoscriptsyntax as rs
import random
from scriptcontext import escape_test
import viewport_tools as vt

from imp import reload
reload(vt)

#program definitions
def random_color(object):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = rs.CreateColor(r,g,b)
    rs.ObjectColor(object, color)

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
                #create colors
                #random_color(grid_point)


    return point_list

def lines(point_list):
    for i in range(len(point_list)):
        point_1 = point_list[i-1]
        point_2 = point_list[i]
        line = rs.AddLine(point_1, point_2)
        random_color(line)


# main program all calls of other functions should be in here
def main():
    #create count at 0 outside of loop
    count = 0
    #set a stop value for the loop
    stop = 5
    #create view with properties
    view_name = "new_top"
    vt.create_parallel_view(view_name, (800, 800))
    vt.set_axon_view(45, 45, view_name)
    #loop
    while count < stop:
        #provide means of exiting the loop
        escape_test(True)
        #disable redraw while object is being created
        rs.EnableRedraw(False)
        #add to count 1 unit each time the loop runs
        count += 1
        #provide instructions to user
        point = rs.GetPoint("Select Point or hit Escape key")
        points = cubic_grid(point, 10, 10, 10, 20)
        lines(points)
        #enable redraw after object is created
        rs.EnableRedraw(True)
        rs.ZoomExtents()
    #save viewport to file
    vt.set_viewports_mode("Wireframe")
    rs.ZoomExtents()
    vt.capture_view(2.0, "test_grid", "grid_folder")
    
#call the main program

main()
