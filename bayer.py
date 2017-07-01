import time
import picamera
import picamera.array
import numpy as np

var = 0
n = 0

with picamera.PiCamera() as camera: 
    with picamera.array.PiBayerArray(camera) as stream:
        try:
            while var == 0:
                n += 1
                camera.capture(stream, 'jpeg', bayer=True)
                output = (stream.demosaic() >> 2).astype(np.uint8)
                time.sleep(1)  
                with open('/media/pi/7806-7969/Python/'+'%d' % (n),'wb') as f:
                    output.tofile(f)
        except IOError as err:
            print('hello')
