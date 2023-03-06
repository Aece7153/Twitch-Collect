import PIL.ImageGrab
import PIL.Image
import mouse
import time

# COLOR = 0, 219, 132
# Press here = -245,1004
time.sleep(3)
while True:
    cropRect = (-244,1003, -243,1005)
    im = PIL.ImageGrab.grab(all_screens=True, bbox=cropRect)
    px = im.load()
    #print(px[0,0])
    if px[0,0] == (0, 219, 132) or px[0,0] == (92, 255, 190):
        mouse.move(-245,1004)
        mouse.click('left')

