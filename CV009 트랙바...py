import cv2
import numpy as np
import sys

src = cv2.imread('./image/Mahjong4.jpg',flags=cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()
    
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) # BGR -> HSV 로 변경(색상 검출에 효율적)

# 트랙바 콜백 함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst') # 트랙바의 위치를 받아옴 (h_min 값)
    hmax = cv2.getTrackbarPos('H_max', 'dst')
    
    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)
    
cv2.imshow('src', src)
cv2.namedWindow('dst')

# 트랙바 콜백 함수 등록
cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar)
cv2.createTrackbar('H_max', 'dst', 80, 179, on_trackbar)
on_trackbar(0)

cv2.waitKey()

cv2.destroyAllWindows()