#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np  

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera not opened.")
    exit()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    if not _:
        print("Error: Frame not read.")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if (hue_value >= 0 and hue_value < 15) or (hue_value >= 165 and hue_value <= 180):
        color = "RED"
    elif hue_value >= 15 and hue_value < 30:
        color = "ORANGE"
    elif hue_value >= 30 and hue_value < 60:
        color = "YELLOW"
    elif hue_value >= 60 and hue_value < 90:
        color = "GREEN"
    elif hue_value >= 90 and hue_value < 135:
        color = "CYAN"
    elif hue_value >= 135 and hue_value < 165:
        color = "BLUE"
    elif hue_value >= 165 and hue_value < 180:
        color = "VIOLET"
    elif hue_value >= 0 and hue_value < 8:
        color = "RED"
    elif hue_value >= 8 and hue_value < 22:
        color = "ORANGE"
    elif hue_value >= 22 and hue_value < 38:
        color = "YELLOW"
    elif hue_value >= 38 and hue_value < 75:
        color = "GREEN"
    elif hue_value >= 75 and hue_value < 120:
        color = "CYAN"
    elif hue_value >= 120 and hue_value < 160:
        color = "BLUE"
    elif hue_value >= 160 and hue_value < 175:
        color = "VIOLET"
    elif hue_value >= 175 and hue_value < 180:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    text_size = cv2.getTextSize(color, cv2.FONT_HERSHEY_SIMPLEX, 3, 5)[0]
    rect_width = text_size[0] + 40  
    
    cv2.rectangle(frame, (cx - rect_width // 2, 10), (cx + rect_width // 2, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - text_size[0] // 2, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (b, g, r), 5)
    
    triangle_points = [(cx - rect_width // 2 - 20, 100), (cx - rect_width // 2 - 20, 80), (cx - rect_width // 2 - 40, 90)]
    cv2.fillConvexPoly(frame, np.array(triangle_points), (b, g, r))

    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




