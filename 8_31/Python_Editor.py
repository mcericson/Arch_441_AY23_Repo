import rhinoscriptsyntax as rs


center_point = (0, 0, 0)
radius = 100.0
message = "A circle has been added to the document"

#This program creates a circle
rs.AddCircle(center_point, radius)
print(message)




