import numpy as np
import cv2
import urllib.request

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        my_color = np.zeros((255, 255, 3), np.uint8)
        my_color[:] = [blue, green, red]
        cv2.imshow('my Color', my_color)

# Load image from internet
url = 'URL_OF_YOUR_IMAGE'
resp = urllib.request.urlopen(url)
image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
