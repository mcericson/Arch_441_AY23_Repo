#loop studies

import rhinoscriptsyntax as rs
#point rows
#row 1 (0,0) ,(1,0) ,(2,0)
#row 2  (0,1) ,(1,1) , (2,1)

rs.EnableRedraw(False)

for i in range(1, 10, 2):
    x = i
    for j in range(1, 10, 2):
        y = j
        for p in range(1, 10, 2):
            z = p
            point = rs.AddPoint(x, y, z)
            rs.AddSphere(point, i/5)


