import time
import picamera
import picamera.array
import numpy as np

n = 0
var = 0

while var == 0:
    n += 1
    with picamera.PiCamera() as camera:
        with picamera.array.PiBayerArray(camera) as stream:
            try:
                camera.capture(stream, 'jpeg', bayer=True)
                output = (stream.demosaic() >> 2).astype(np.uint8)
                time.sleep(1)
                with open('/media/pi/KINGSTON/Python/'+'%d' % (n),'wb') as f:
                    output.tofile(f)
            except IOError as err:
                print('The Process has Finished.')
                break

