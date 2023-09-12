
import rhinoscriptsyntax as rs
from scriptcontext import escape_test
import random

points = []
while len(points) < 100:
    escape_test(True)
    cursor = rs.GetCursorPos()[0]
    points.append(rs.AddPoint(cursor))
    if len(points) >= 2:
        radius = rs.Distance(points[-2], cursor)
        try:
            circle =rs.AddCircle(cursor, radius)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color = rs.CreateColor(r, g, b)
            rs.ObjectColor(circle, color)
        except:
            pass

