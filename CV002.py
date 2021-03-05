import cv2
import numpy as np

#이미지 입력
src=cv2.imread("./image/Mahjong2.jpg",flags=cv2.IMREAD_COLOR)
#print(src.ndim,src.shape,src.dtype)

cv2.namedWindow("src",flags=cv2.WINDOW_AUTOSIZE)
cv2.imshow("src",src)
cv2.waitKey(0)
cv2.destroyWindow("src")

#동영상 입력
capture=cv2.VideoCapture("./image/video.mp4")

while True:
    ret,frame=capture.read()

    if(capture.get(cv2.CAP_PROP_POS_FRAMES)==capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("./image/video.mp4")
    cv2.imshow("VideoFrame",frame)
    if cv2.waitKey(33)==ord('q'):break

capture.release()
cv2.destroyAllWindows()