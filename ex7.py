# import numpy as np
# import cv2
# img = cv2.imread('assests/1.jpg',0)
# template = cv2.imread('assests/2.jpg',0)
# h, w = template.shape

# methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

# for method in methods:
#     img2 = img.copy()
#     result = cv2.matchTemplate(img2,template,method)
#     min_val , max_val , min_loc , max_loc = cv2.minMaxLoc(result)
#     if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
#         location = min_loc
#     else:
#         location = max_loc
#     bottom_right = (location[0]+w,location[1]+h)
#     cv2.rectangle(img2,location,bottom_right,255,5)
#     cv2.imshow("Match",img2)
#     if cv2.waitKey(0) == ord('R'):
#         break
# cv2.destroyAllWindows()

import numpy as np
import cv2

img = cv2.imread('assests/chessboard.png')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey,100,0.01,10)
corners = np.intp(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x : int(x),np.random.randint(0,255,size=3)))
        cv2.line(img,corner1,corner2,color,1)
cv2.imshow('frame',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()



