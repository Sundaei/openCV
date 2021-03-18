import cv2
import numpy as np

src=cv2.imread("./image/Mahjong1.jpg",flags=cv2.IMREAD_COLOR)
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

cv2.imshow("src",src)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

ROI=cv2.selectROI(gray,False)
img=gray[ROI[1]:ROI[1]+ROI[3],ROI[0]:ROI[0]+ROI[2]]

cv2.imshow("ROI",img)
cv2.waitKey(0)
cv2.destroyAllWindows()