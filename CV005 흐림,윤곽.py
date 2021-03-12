import cv2
import numpy as np

src=cv2.imread("./image/Rainbow.webp",flags=cv2.IMREAD_COLOR)
cv2.imshow("src",src)
#단순 흐림
dst=cv2.blur(src,(15,15),anchor=None,borderType=None)

cv2.imshow("blur",dst)

#가우시안 흐림
dst=cv2.GaussianBlur(src,(15,15),0,sigmaY=None,borderType=None)

cv2.imshow("Gau",dst)

#양방향 필터
dst=cv2.bilateralFilter(src,5,75,75)
cv2.imshow("bilateral",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()