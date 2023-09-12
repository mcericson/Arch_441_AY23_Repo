import rhinoscriptsyntax as rs

#this program creates 3d grid
rs.EnableRedraw(False)



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
    rs.AddPoints(point_list)
    
#assigning variable
stop_x, stop_y, stop_z = (5, 5, 5)
step = 1
start_x, start_y, start_z = (0,0,0)
#calling the function
cubic_grid(start_x, start_y, start_z, step, stop_x, stop_y, stop_z)
cubic_grid(0, 0, 0, 2, 10, 10, 10)