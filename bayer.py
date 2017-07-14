import time
import picamera
import picamera.array
import numpy as np
import numpy
from PIL import Image

n = 0
var = 0

while var == 0:
    n += 1
    with picamera.PiCamera() as camera:
        with picamera.array.PiBayerArray(camera) as stream:
            try:
                camera.capture(stream, 'jpeg', bayer=True)
                time.sleep(1)
                img = np.asarray(stream.array)
                #print(img)
                path = "/media/pi/KINGSTON/Python/" + '%d' % (n)
                img = Image.fromarray(img, 'RGB')
                img = img.save(path + '.jpeg')
            except IOError as err:
                print('The Process has Finished.')
                break
