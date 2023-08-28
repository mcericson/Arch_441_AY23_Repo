import rhinoscriptsyntax as rs

rs.EnableRedraw(False)

for i in range(0,10,1):
    x = i
    for j in range(0,10,1):
        y = j
        for p in range(0,10,1):
            z = p
            point  = rs.AddPoint(x,y,z)
            
print ("grid added to document")

