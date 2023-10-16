#mark ericson
#10/17/2023
#This program translates images into geometry

#imports----------------------------------

import rhinoscriptsyntax as rs
import System.Drawing.Bitmap as Bitmap
import box_tools as bt
import color_tools as ct
import viewport_tools as vt
from imp import reload

reload(bt)


#definitions------------------------------

def assign_material_color(object, color):
    rh_color = rs.CreateColor(color)
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, rh_color)

def image_to_coordinates(file_path, resolution):
    img = Bitmap.FromFile(file_path)
    
    width  = img.Width
    height = img.Height
    
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    
    colors = []
    locations = []
    
    pixel_dim = w_step, h_step
    
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            r,g,b,a = img.GetPixel(x, y)
            location = (x, y, 0)
            locations.append(location)
            colors.append((r,g,b,a))
    nl = locations.reverse()
    return locations, colors, pixel_dim

def image_to_geometry(image_path, resolution, geometry='points'):

    rs.EnableRedraw(False)
    image_data = image_to_coordinates(image_path, resolution)
    
    points = image_data[0]
    colors = image_data[1]
    w, h = image_data[2]
    for i in range(len(points)):
        if geometry == 'points':
            point = rs.AddPoint(points[i])
            color = rs.CreateColor(colors[i])
            rs.ObjectColor(point, color)
        if geometry == 'box':
            height_value = colors[i][0]*10
            box = bt.base_box(points[i], height_value, w, h)
            assign_material_color(box, colors[i])
        if geometry == 'line':
            r,g,b,a = colors[i]
            x, y, z = points[i]
            point_a = (x, y, z)
            point_b = (x + r, y + g, z + b)
            line = rs.AddLine(point_a, point_b)
            color = rs.CreateColor(r,g,b,a)
            rs.ObjectColor(line, color)

    rs.EnableRedraw(True)

#main---------------------------------------------


def main():
   
    vt.create_parallel_view('new_top', (1000,1000))
    image_path = "web_mountains_small.jpg"
    image_to_geometry(image_path, 100, 'line')
    rs.ZoomExtents()
    vt.capture_view(2.0, 'tst_image', 'test_folder')


main()



