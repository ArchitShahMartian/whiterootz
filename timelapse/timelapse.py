from picamera import PiCamera
import time
# import logging

# logging.basicConfig(filename="timelapse.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
#
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

TIMELAPSE_DIR = '/home/pi/misc/gitwork/timelapse/timelapse_img_dir'

camera = PiCamera()
camera.resolution = (1280, 720)
camera.capture('/home/pi/misc/gitwork/timelapse/timelapse_img_dir/test_{}.jpg'.format(time.strftime("%Y%m%d-%H%M%S")))
# logger.info('Photo captured test_{}'.format(time.strftime("%Y%m%d-%H%M%S")))
