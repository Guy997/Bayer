import time
import picamera
import picamera.array
import numpy as np
import rawpy
import imageio

n = 0
var = 0

while var == 0:
    n += 1
    with picamera.PiCamera() as camera:
        with picamera.array.PiBayerArray(camera) as stream:
            try:
                camera.capture(stream, 'jpeg', bayer=True)
                time.sleep(1)
                path = '/media/pi/KINGSTON/Python/'+'%d' % (n),'wb'
                with open(path) as f:
                    output.tofile(f)
                with rawpy.imread(path) as raw:
                    rgb = raw.postprocess()
                imageio.imsave('%d' % (n) + '.tiff', rgb)
            except IOError as err:
                print('The Process has Finished.')
                break
