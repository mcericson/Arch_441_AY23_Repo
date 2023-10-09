import rhinoscriptsyntax as rs


def remap(value, source_min, source_max, target_min, target_max):
    """maps a set of values to to a new domain
    example:  remmap( 180, 0, 360, 0.0, 1.0)
    This would remap the value of 180 to domain of 0.0 to 1.0. 
    The remapped value in this case is 0.5"""
    
    source = source_max - source_min
    target = target_max - target_min
    value_less = value - source_min
    
    new_value = float(target * value_less / float(source)) + target_min
    return new_value
    
def clamp(value, floor, ceiling):
    """this clamps a value to a domain. It will not return a value higher
    than the ceiling"""
    if value < floor:
        return floor
    if value > ceiling:
        return ceiling
    else:
        return value

def point_to_rgb(point, min, max):
    """This converts the x, y, and z cooridinates to r, g, and
    b values in a three dimensional cube defined by a min and max"""
    
    x, y, z = point
    
    r = clamp(remap(x, min, max, 0, 255), 0, 255)
    g = clamp(remap(y, min, max, 0, 255), 0, 255)
    b = clamp(remap(z, min, max, 0, 255), 0, 255)
    
    return r, g, b

def random_color(object):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = rs.CreateColor(r,g,b)
    rs.ObjectColor(object, color)