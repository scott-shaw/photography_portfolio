import os, os.path
import cv2

data_path = os.path.dirname(os.path.abspath(__file__))+"/photo_data.js"

imgs = []
path_list = []
travel_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/travel/"
street_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/street/"
macro_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/macro/"
wildlife_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/wildlife/"

paths = [travel_path, street_path, wildlife_path, macro_path]
valid_images = [".jpg",".JPG"]

for path in paths:
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        p = os.path.join(path,f)
        imgs.append(cv2.imread(p))
        path_list.append(p)

with open(data_path, 'w') as f:

    for i, path in enumerate(path_list):
        f.write("import photo" + str(i) + " from " + "\"" + path + "\";\n")

    f.write("export const photos = [\n")

    for i, img in enumerate(imgs):
        w, h, _ = img.shape
        f.write("{\nsrc: photo" + str(i) + ",\nwidth: " + str(h) +",\nheight: " + str(w) + "\n},\n")

    f.write("]")
    f.close()


