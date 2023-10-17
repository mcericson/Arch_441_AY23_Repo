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
    
    for i in range(len(points)):
        if geometry == 'point':
            point = rs.AddPoint(points[i])
            assign_material_color(point, colors[i])
        if geometry == 'box':
            r, g, b, a  = colors[i]
            box = bt.base_box(points[i], b+ 10 , w, l)
            assign_material_color(box, colors[i])
        if geometry == 'line':
            r, g, b, a = colors[i]
            x, y, z = points[i]
            point_a = (x, y, z)
            point_b = (x + r, y + g, z + b)
            line = rs.AddLine(point_a, point_b)
            assign_material_color(line, colors[i])
            


#main---------------------------------------------------

def main():
    view_name = 'new_top'
    vt.create_parallel_view(view_name,(1000,1000))
    vt.set_axon_view(45, 120, view_name)
    file_path = 'web_mountains_small.jpg'
    image_to_geometry(file_path, 50, 'line')
    rs.ZoomExtents()
    vt.capture_view(2.0, 'line_test', 'line_tests')


main()