import rhinoscriptsyntax as rs

#this program creates 3d grid
rs.EnableRedraw(False)
import random



#defining the function. 
def cubic_grid(start_x, start_y, start_z, step, stop_x, stop_y, stop_z):
    point_list = []
    for i in range(start_x, stop_x + start_x, step):
        x = i
        for j in range(start_y, stop_y + start_y, step):
            y = j
            for p in range(start_z, stop_z + start_z, step):
                z = p
                point = (x, y, z)
                point_list.append(point)
    #rs.AddPoints(point_list)
    return(point_list)
    
#assigning variable
stop_x, stop_y, stop_z = (20, 20,20)
step = 1
start_x, start_y, start_z = (0,0,0)
#calling the function
points = cubic_grid(start_x, start_y, start_z, step, stop_x, stop_y, stop_z)


for i in range(len(points)):
    point_1 = points[i-1]
    point_2 = points[i]
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    line = rs.AddLine(point_1, point_2)
    color = rs.CreateColor(r,g,b)
    rs.ObjectColor(line, color)
