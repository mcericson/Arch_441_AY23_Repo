import rhinoscriptsyntax as rs



def point_attractor(original_point, attractor_point, magnitude):
    new_point = rs.AddPoint(attractor_point)
    vector_1 = rs.VectorCreate(new_point, original_point)
    vector_2 = rs.VectorUnitize(vector_1)
    vector_3 = rs.VectorScale(vector_2, magnitude)
    moved_point = rs.MoveObject(original_point, vector_3)
    return moved_point
    
def main():

    point = rs.AddPoint(0,0,0)
    
    attractor_point = rs.GetPoint()
    
    point_attractor(point, attractor_point, 100)


main()