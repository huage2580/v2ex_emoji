import os
import cv2
import numpy as np

image_size = 42

def changesize(source_path):
    image_lists=os.listdir(source_path)
    i=0
    for file in image_lists:
        i=i+1
        split=os.path.splitext(file)
        filename,type=split
        image_file = source_path+"\\"+file
        image_source=cv2.imdecode(np.fromfile(image_file,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
        image = cv2.resize(image_source, (image_size, image_size))
        cv2.imencode('.png',image)[1].tofile(image_file)


changesize('emoji')
