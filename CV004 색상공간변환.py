import cv2
import numpy as np

abc=cv2.imread("./image/TrumpCard.jpg",flags=cv2.IMREAD_COLOR)
dfg=cv2.cvtColor(abc,cv2.COLOR_BGR2HSV)
#HSV: 다중 채널 색상 이미지(Hue(색상),Saturation(채도), Value(명도))
cv2.imshow("dfg",dfg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#채널 분리 함수
mv=cv2.split(abc)

cv2.imshow("abc",abc)
cv2.waitKey(0)
cv2.destroyAllWindows()

#채널 병합 함수
dst=cv2.merge(mv)
dst=cv2.merge([mv[0],mv[1],mv[2]])

abc=cv2.imread("./image/TrumpCard.jpg")
dgf=cv2.cvtColor(abc,cv2.COLOR_BGR2HSV)

d,g,f=cv2.split(dgf)
d_red=cv2.inRange(d,0,5)
dst=cv2.bitwise_and(dgf,dgf,mask=d_red)
dst=cv2.cvtColor(dst,cv2.COLOR_HSV2BGR)

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

d,g,f=cv2.split(dgf)

orange=cv2.inRange(dgf,(160,100,100),(179,255,255))
blue=cv2.inRange(dgf,(110,100,100),(130,255,255))
mix_color=cv2.addWeighted(orange,1.0,blue,1.0,0.0)

dst=cv2.bitwise_and(dgf,dgf,mask=mix_color)
dst=cv2.cvtColor(dst,cv2.COLOR_HSV2BGR)

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
