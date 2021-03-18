import cv2
import numpy as np

src=cv2.imread("./image/Mahjong4.jpg",flags=cv2.IMREAD_COLOR)

dst=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY",dst)

ret,thresh=cv2.threshold(dst,50,255,cv2.THRESH_BINARY_INV)
_,cnt=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)
cv2.drawContours(dst,_,-1,(0,255,0),1)
cv2.imshow("thr",thresh)
cv2.imshow("cnt",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

ker=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3),anchor=(-1,-1))
Mor=cv2.dilate(dst,ker,iterations=2)
cv2.imshow("MOR",Mor)
clo=cv2.erode(Mor,ker,iterations=2)
cv2.imshow("clo",clo)
cv2.waitKey(0)
cv2.destroyAllWindows()