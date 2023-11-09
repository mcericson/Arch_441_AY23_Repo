import os
import cv2
import moviepy.video.io.ImageSequenceClip

def numbered_name(number, name, padding):
    num = str(number) 
    num_pad = num.zfill(padding)
    file_name = num_pad + "_" + name
    return file_name


def image_resize(file_path, width, height, file_name):
    img = cv2.imread(file_path)
    w = int(width)
    h = int(height)
    new_dim = (w, h)
    new_image = cv2.resize(img, new_dim, interpolation = cv2.INTER_AREA )
    image_file = cv2.imwrite(file_name, new_image)
    return file_name
    


def make_movie(fps, width, height, file_name):
    """Makes a movie from a set of images.  Forces images to same size by setting widht and height parameters. """
    
    all_files = os.listdir()
    all_images = []
    
    for i in all_files:
        if i.endswith(".png"):
            all_images.append(i)
    count = 0
    resized_images = []
    for j in all_images:
        count += 1
        file_name = numbered_name(count, 'temp.png', 4)
        re_image = image_resize(j, width, height, file_name)
        resized_images.append(re_image)
        
    
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(resized_images, fps=fps)
    file_path = str(file_name) + ".mp4"
    clip.write_videofile(file_path)
    
    for m in resized_images:
        os.remove(m)
    
               

make_movie(20, 1000, 1000, "rgb_cube")