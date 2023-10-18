#Mark Ericson
#10/17/23
#This program imports image data and converts it to geometry.

#imports-----------------------------------

import rhinoscriptsyntax as rs
import System.Drawing.Bitmap as Bitmap
import box_tools as bt
import color_tools as ct
import viewport_tools as vt 


#definitions-------------------------------

def assign_material_color(object, color):
    rh_color = rs.CreateColor(color)
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, rh_color)
    rs.ObjectColor(object, rh_color)


def image_to_coordinates(file_path, resolution):
    
    locations = []
    colors = []
    
    img = Bitmap.FromFile(file_path)
    
    image_width = img.Width
    image_height = img.Height
    
    w_step = int(image_width/resolution)
    h_step = int(image_height/resolution)
    
    for i in range(0, image_width, w_step):
        for j in range(0, image_height, h_step):
            x = i
            y = j 
            r, g, b, a = img.GetPixel(x, y)
            
            locations.append((x, y, 0))
            colors.append((r , g, b, a))
    locations.reverse()
    return locations, colors


def image_to_geometry(file_path, resolution, geometry='point'):
    rs.EnableRedraw(False)
    
    image_data = image_to_coordinates(file_path, resolution)
    
    points = image_data[0]
    colors = image_data[1]
    
    for i in range(len(points)):
        if geometry == 'point':
            point = rs.AddPoint(points[i])
            assign_material_color(point, colors[i])
        if geometry == 'line':
            x, y, z = points[i]
            r, g, b, a = colors[i]
            point_a = (x, y, z)
            point_b = (x + r, y + g, z + b)
            line = rs.AddLine(point_a, point_b)
            assign_material_color(line, colors[i])

#main---------------------------------------------

def main():
    file_path = 'web_mountains_small.jpg'
    image_to_geometry(file_path, 50, 'line')

main()