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

def pixel_color_name(r, g, b):
    """This funcion breaks the HSL colorwheel into 6 segments
    and returns a name for each."""
    #convert an rgb value to and h, l, s value. 
    h, s, v = rgb_to_hsv(r, g, b)
    h_degrees = h
    print(h_degrees)
    #specifiy the color breaks
    if 330 <= h_degrees or h_degrees<= 30:
        return "red"
    if 30 <= h_degrees <= 90:
        return "yellow"
    if 90 <= h_degrees <= 150:
        return "green"
    if 150 <= h_degrees <= 210:
        return "cyan"
    if 210 <= h_degrees <= 270:
        return "magenta"
    if 270 <= h_degrees <= 330:
        return "blue"
    if h_degrees >= 360:
        return "red"

def rgb_to_hsv(r, g, b):
    #source https://www.w3resource.com/python-exercises/math/python-math-exercise-77.php
    r, g, b = r/255.0, g/255.0, b/255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    
    diff = max_val - min_val
    
    if max_val == min_val:
        h = 0
    elif max_val == r:
        h = (60 * ((g-b)/diff) + 360)%360
    elif max_val == g:
        h = (60 * ((b-r)/diff) + 120)%360
    elif max_val == b:
        h = (60 * ((r-g)/diff) + 240)%360
    if max_val == 0:
        s = 0
    else:
        s = (diff/max_val)*100
    v = max_val*100
    
    return h, s, v

def hsv_to_rgb(h, s, v):
    # https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.)
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    v = clamp(int(v), 0, 255)
    t = clamp(int(t),  0, 255)
    p = clamp(int(p),  0, 255)
    q = clamp(int(q),  0 , 255)
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)

def assign_material_color(object, color):
    rh_color = rs.CreateColor(color)
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, rh_color)
    rs.ObjectColor(object, rh_color)