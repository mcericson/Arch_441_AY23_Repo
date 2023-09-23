import rhinoscriptsyntax as rs
from scriptcontext import escape_test

count = 0

while count <= 10:
    count += 1
    escape_test(True)
    center = rs.GetPoint()
    radius = rs.Distance((0,0,0), center)
    rs.AddCircle(center, 300)