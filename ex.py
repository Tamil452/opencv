import numpy as np
import cv2
import random

# img = cv2.imread("assests/chessboard.png")
# img = cv2.resize(img,(0,0),fx=0.75,fy=0.75)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
# corners =np.intp(corners)

# for corner in corners:
#     x,y = corner.ravel()
#     cv2.circle(img,(x,y),5,(255,0,0),-1)

# for i in range(len(corners)):
#     for j in range(i+1,len(corners)):
#         corner1 = tuple(corners[i][0])
#         corner2 = tuple(corners[j][0])
#         color = tuple(map(lambda x : int(x),np.random.randint(0,255,size=3)))
#         cv2.line(img, corner1, corner2, color, 1)

# cv2.imshow("Image",img)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()
# import random
# img = cv2.imread('assests/download.jpg')
# img = cv2.resize(img,(600,600),fx=1,fy=1)
# img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

# cv2.imwrite('new_image.jpg',img)
# cv2.imshow('Image',img)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
# print(img) # to get the total no of pixel in row format
# print(type(img)) # to get the type of the image
# print(img.shape) # to get no of rows and column

# print(img[0][25:40])

# tag = img[120:160,120:220]
# img[80:120,200:300] = tag


# for i in range(10):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
# cv2.imshow('Image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap =  cv2.VideoCapture(0)

while True:
    res,frane = cap.read()
   
    height = int(cap.get(4))
    width = int(cap.get(3))
    
    hsv = cv2.cvtColor(frane,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([22,93,0])
    Upper_blue = np.array([45,255,255])
    mask = cv2.inRange(hsv,lower_blue,Upper_blue)
    result = cv2.bitwise_and(frane,frane,mask=mask)
#     # img = cv2.line(frane,(0,240),(640,240),(255,0,0),10)
    image = np.zeros(frane.shape,np.uint8)
    
    smaller_frame = cv2.resize(frane,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2] = smaller_frame
    image[height//2:,:width//2] = smaller_frame
    image[:height//2,width//2:] = smaller_frame
    image[height//2:,width//2:] = smaller_frame
    # cv2.imshow("img",mask)
    cv2.imshow("frame",image)
    
    if cv2.waitKey(1) == ord('r'):
        break

cap.release()
cv2.destroyAllWindows()