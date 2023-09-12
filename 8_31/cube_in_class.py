#Mark Ericson
#This program will create a line of points

import rhinoscriptsyntax as rs


rs.EnableRedraw(False)

x_stop = 10
y_stop = 10
z_stop = 10
step = 4
message = "This program is complete"

for i in range(0, x_stop, step):
    x = i
    for j in range(0, y_stop, step):
        y = j
        for p in range(0, z_stop , step):
            z = p
            point = rs.AddPoint(x, y, z)
            radius = x/2 + 0.5
            rs.AddSphere(point, radius)
print(message)