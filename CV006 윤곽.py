from typing import Counter
import cv2
import numpy as np

src=cv2.imread("./image/Mahjong1.jpg",flags=cv2.IMREAD_COLOR)
cv2.imshow("src",src)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Canny
dstv=cv2.Canny(src,100,200,apertureSize=3,L2gradient=True)

cv2.imshow("src",dstv)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst=src.copy()

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
gray=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
ret,binary=cv2.threshold(gray,230,255,cv2.THRESH_BINARY)

image=cv2.bitwise_not(binary)
cv2.imshow("con",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours,hierarchy=cv2.findContours(dstv,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)
cv2.drawContours(dstv,contours,-1,(0,0,255),3)
for i in range(len(contours)):
    cv2.putText(dstv,str(i),tuple(contours[i][0][0]),cv2.FONT_HERSHEY_COMPLEX,0.1,(255,0,0),1)
    print(i,hierarchy[0][i])

cv2.imshow("con",dstv)
cv2.waitKey(0)
cv2.destroyAllWindows()



