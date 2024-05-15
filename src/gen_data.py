import os, os.path
import cv2

data_path = os.path.dirname(os.path.abspath(__file__))+"/photo_data.js"

imgs = []
path_list = []
travel_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/travel/"
street_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/street/"
macro_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/macro/"
wildlife_path = os.path.dirname(os.path.abspath(__file__))+"/assets/photos/wildlife/"

thumbs = []
thumb_list = []
travel_path_thumb = travel_path+"thumbnails/"
street_path_thumb = street_path+"thumbnails/"
macro_path_thumb = macro_path+"thumbnails/"
wildlife_path_thumb = wildlife_path+"thumbnails/"

paths = [travel_path, street_path, wildlife_path, macro_path]
paths_thumb = [travel_path_thumb, street_path_thumb, wildlife_path_thumb, macro_path_thumb]
valid_images = [".jpg",".JPG"]

for path, thumb in zip(paths, paths_thumb):
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        p = os.path.join(path,f)
        imgs.append(cv2.imread(p))
        path_list.append(p)
    for f in os.listdir(thumb):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        p = os.path.join(thumb,f)
        thumbs.append(cv2.imread(p))
        thumb_list.append(p)

with open(data_path, 'w') as f:

    for i, path in enumerate(path_list):
        f.write(f"import photo{str(i)} from \"{path}\";\n")
    for i, path in enumerate(thumb_list):
        f.write(f"import photo{str(i)}_thumb from \"{path}\";\n")

    f.write("export const photos = [\n")
    for i, img in enumerate(imgs):
        w, h, _ = img.shape
        f.write("{\nsrc: photo" + str(i) + ",\nwidth: " + str(h) +",\nheight: " + str(w) + "\n},\n")
    f.write("]")

    f.write("\nexport const thumbs = [\n")
    for i, img in enumerate(thumbs):
        w, h, _ = img.shape
        f.write(f"{str('{')}\nsrc: photo{str(i)}_thumb,\nwidth: {str(h)},\nheight: {str(w)}\n{str('}')},\n")
    f.write("]")

    f.close()


