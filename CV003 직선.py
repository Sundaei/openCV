import cv2
import numpy as np

src=cv2.imread("./image/Mahjong2.jpg",flags=cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("src",flags=cv2.WINDOW_AUTOSIZE)
cv2.imshow("src",src)
cv2.waitKey(0)
cv2.destroyWindow("src")

#cv2.line(
# img(파일명),
# pt1(시작좌표 비트 값),
# pt2(도착좌표 비트 값),
# color(BGR 형식),
# thickness=None(설정된 두께),
# lineType=None(연결성 선택?),
# shift=None(실숫값으로 처리할 좌표의 비트 값))