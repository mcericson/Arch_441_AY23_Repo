#mark ericson
#10/17/2023
#This program translates images into geometry.


#imports------------------------------------

import rhinoscriptsyntax as rs
import System.Drawing.Bitmap as Bitmap
import box_tools as bt
import color_tools as ct
import viewport_tools as vt
from imp import reload

reload(bt)


#definitions---------------------------------

def point_attractor(original_point, attractor_point, magnitude):
    new_point = rs.AddPoint(attractor_point)
    vector_1 = rs.VectorCreate(new_point, original_point)
    vector_2 = rs.VectorUnitize(vector_1)
    vector_3 = rs.VectorScale(vector_2, magnitude)
    moved_point = rs.MoveObject(original_point, vector_3)
    return moved_point


def assign_material_color(object, color):
    rh_color = rs.CreateColor(color)
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, rh_color)
    rs.ObjectColor(object, rh_color)

def image_to_coordinates(file_path, resolution):
    img = Bitmap.FromFile(file_path)
    
    width  = img.Width
    height = img.Height
    
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    
    pixel_dim = w_step, h_step
    
    colors = []
    locations = []
    for i in range(0, width, w_step):
        for j in range(0, height, h_step):
            x = i
            y = j
            location = (x, y, 0)
            r, g, b, a = img.GetPixel(x, y)
            locations.append(location)
            colors.append((r, g, b, a))
    locations.reverse()

    return locations, colors, pixel_dim

def image_to_geometry(image_path, resolution, geometry = 'point'):
    rs.EnableRedraw(False)
    image_data = image_to_coordinates(image_path, resolution)
    
    points = image_data[0]
    colors = image_data[1]
    w, l = image_data[2]
    attractor_point = rs.GetPoint()
    for i in range(len(points)):
        if geometry == 'point':
            point = rs.AddPoint(points[i])
            assign_material_color(point, colors[i])
        if geometry == 'box':
            r, g, b, a  = colors[i]
            point_a = rs.AddPoint(points[i])
            point_b = point_attractor(point_a, attractor_point, 1000)
            point_c = rs.PointCoordinates(point_b)
            box = bt.base_box(point_c, b+ 10 , w, l)
            assign_material_color(box, colors[i])
        if geometry == 'line':
            r, g, b, a = colors[i]
            x, y, z = points[i]
            point_a = (x, y, z)
            point_b = (x + r, y + g, z + b)
            line = rs.AddLine(point_a, point_b)
            assign_material_color(line, colors[i])
        if geometry == 'point_attractor':
            point_a = rs.AddPoint(points[i])
            point_b = point_attractor(point_a, attractor_point, 1000)
            np = rs.AddPoint(point_b)
            assign_material_color(point_b, colors[i])

#main---------------------------------------------------

def main():
    view_name = 'new_top'

    file_path = 'web_mountains_small.jpg'
    image_to_geometry(file_path, 50, 'box')
#    vt.create_parallel_view(view_name,(1000,1000))
#    vt.set_axon_view(45, 120, view_name)
#    rs.ZoomExtents()
#    vt.capture_view(2.0, 'line_test', 'line_tests')


main()