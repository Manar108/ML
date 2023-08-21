
import cv2
import datetime

cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret,frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX #type of font 

        text = 'Width = '+str(cap.get(3))+' Height = '+str(cap.get(4))

        date_time = str(datetime.datetime.now())

        #frame = cv2.putText(frame, text, (10,50), font, 1, (0,0,0), 2)

        frame = cv2.putText(frame, date_time, (10,50), font, 1, (0,0,0), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()



