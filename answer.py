import numpy as np
from PIL import Image

def combine_images(file_paths, output_filename="out.png"):
    if len(file_paths) != 2:
        raise ValueError("Expected exactly two image paths.")

    images = [np.asarray(Image.open(path)) for path in file_paths]

    
    if images[0].shape != images[1].shape:
        raise ValueError("Images must have the same dimensions for addition.")

    combined_data = images[0] + images[1]

    new_image = Image.fromarray(combined_data.astype(np.uint8))
    new_image.save(output_filename, "PNG")

file_paths = ["scrambled1.png", "scrambled2.png"]
combine_images(file_paths)

# or this 😉💀
# from PIL import Image
#import numpy as np
#import os

#file_names = ["scrambled1.png", "scrambled2.png"]
#img_data = [np.asarray(Image.open(f'{name}')) for name in file_names]

#data = img_data[0].copy() + img_data[1].copy()

#new_image = Image.fromarray(data)
#new_image.save("out.png", "PNG")
