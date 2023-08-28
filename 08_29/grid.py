import rhinoscriptsyntax as rs

rs.EnableRedraw(False)

for i in range(0,10,1):
    x = i
    for j in range(0,10,1):
        y = j
        point  = rs.AddPoint(x,y,0)
            
print ("grid added to document")

#(0,0,0), (1,0,0)
#(0,1,0 , (1,1,0)