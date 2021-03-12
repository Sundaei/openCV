import cv2
import numpy as np

src=cv2.imread("./image/Mahjong1.jpg",flags=cv2.IMREAD_COLOR)

dst=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY",dst)

ker=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3),anchor=(-1,-1))
Mor=cv2.dilate(dst,ker,iterations=2)
cv2.imshow("MOR",Mor)
clo=cv2.erode(Mor,ker,iterations=2)
cv2.imshow("clo",clo)
cv2.waitKey(0)
cv2.destroyAllWindows()