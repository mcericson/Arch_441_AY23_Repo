import rhinoscriptsyntax as rs
import math
import random 
import color_tools as ct
def chunk_list(items, size):
    return [items[i:i + size] for i in range(0 ,len(items), size)]


def distance(point_a, point_b):
    x1, y1, z1 = point_a
    x2, y2, z2 = point_b
    
    x_diff = (x2 - x1)**2
    y_diff = (y2 - y1)**2
    z_diff = (z2 - z1)**2
    
    distance = math.sqrt(x_diff + y_diff + z_diff)
    return distance

def grid(start_point,x_num, y_num, space):
    sx, sy, sz = start_point
    point_list = []
    for i in range(sx, x_num * space + sx, space):
        for j in range(sy, y_num * space + sy, space):
            x = i
            y = j
            point = (x, y, 0)
            point_list.append(point)
    return point_list


def project_to_sphere(points, sphere_radius, sphere_center):
    sphere_points = []
    for i in points:
        x, y, z = i
        """Below is the pythagorean theorem where a2 + b2 = c2.  This is used to solve for a which would be the 
        z coordinate.  a = sqrt of c2 - b2.  Adding this z to the original x and y gives you the projected point location"""
        b_side = distance(sphere_center, i)
        if b_side <= sphere_radius:
            c_side = sphere_radius
            a_side = math.sqrt(abs(b_side**2 - c_side**2))
            z_new = a_side
            sphere_point = (x, y, z_new)
            sphere_points.append(sphere_point)
        else:
            sphere_points.append(i)
    
    return sphere_points
    





def grid_vault(start_point, radius, max):
    rs.EnableRedraw(False)
    size = 20
    grid_start = start_point
    
    points = grid(grid_start , size, size,  1)
    cx, cy, cz = grid_start
    grid_center = (cx + size/2, cy + size/2, 0)
    #rs.AddPoints(points)
    new_points = project_to_sphere(points, radius, grid_center)
    #rs.AddPoints(new_points)
    line_points = chunk_list(new_points, size)
    poly_lines = []
    for i in line_points:
        color_point = i[0]
        color = ct.point_to_rgb(color_point, 0, max)
        poly = rs.AddPolyline(i)
        ct.assign_material_color(poly, color)
        poly_lines.append(poly)
    #loft = rs.AddLoftSrf(poly_lines)


  

def main():
    
    points = grid((0,0,0), 20, 20, 20)
    max = 10 * 20
    for i in points:
        random_radius = random.uniform(8, 10)
        grid_vault(i, random_radius, max)

main()