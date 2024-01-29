import numpy as np
import cv2
 
img = cv2.imread("assests/1.jpg",0)
template = cv2.imread("assests/4.jpg",0)
h, w = template.shape

methods = [cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val , max_val , min_loc ,max_loc = cv2.minMaxLoc(result)
    if method in[cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        loaction = min_loc
    else:
        location = max_loc 
    bottom_right = (location[0]+w,location[1]+h)
    cv2.rectangle(img2,location,bottom_right,255,5)
    cv2.imshow("Match",img2)
    if cv2.waitKey(0) == ord('r'):
        break
cv2.destroyAllWindows()

# img = cv2.imread("assests/1.jpg")
# template = cv2.imread("assests/3.jpg")
# h,w = template.shape

# methods = [cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

# for method in methods:
#     if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
