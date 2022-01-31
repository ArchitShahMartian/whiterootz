import cv2
import re
import datetime
from os import listdir, path

""" - Understand cv2 properly
    - timelapse_img_dir make sure it only takes the img and not any other file present in the directory
    - remove hardcoding of frameSize
    - Also make sure that the timelapse.py captures image of a particular size
"""

TIMELAPSE_IMG_DIR = '/home/pi/misc/gitwork/timelapse/timelapse_img_dir/'
time_format = "%Y%m%d-%H%M%S"
regex = re.compile(r"^test_(\d*-\d*)")
frameSize = (1280, 720)
video_out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 20, frameSize)

def get_timestamp(image_file):
    m = regex.search(image_file)
    return datetime.datetime.strptime(m.groups()[0], time_format)

count = 0
for file in sorted(listdir(TIMELAPSE_IMG_DIR), key=get_timestamp):
    if count <=32: # <- remove this
        img = cv2.imread(path.join(TIMELAPSE_IMG_DIR, file))
        video_out.write(img)
        count +=1

video_out.release()
