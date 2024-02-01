import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,threshold= cv2.threshold(gray,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("frame",frame)
    cv2.imshow("threshold",threshold)

    if cv2.waitKey(1) == ord('r'):
        break

cap.release()
cv2.destroyAllWindows()