import rhinoscriptsyntax as rs

def user_settings():
    cube_dim = rs.GetInteger("Provide a dimension for the cube", 
    number=10, minimum=1, maximum=20)
    cursor = rs.GetString("Would you like to rotate the model with your cursor?",
    "No", ["Yes", "No"])
    stop = rs.GetInteger("How many frames would you like the animation to be?",
    number=10, minimum=10, maximum=1000)
    save_animation = rs.GetString("Would you like to save an animation?", "No", ["Yes", "No"])
    return cube_dim, cursor, stop, save_animation

cube_dim, cursor, stop, save_animation = user_settings()

print(cube_dim, cursor, stop, save_animation)