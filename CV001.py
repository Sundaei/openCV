import cv2
import numpy as np
print(cv2.__version__)

#python OpenCV에서의 이미지 표현: color: 색상 이미지, gray: 그레이스케일 이미지, 크기, 채널 수, 정밀도 표시
#color=np.zeros((height,width,3),np.uint8)
#gray=np.zeros((rows,cols,1),np.uint8)

array=np.array([[1,2,3],[4,5,6]])
print(array.ndim);print(array.shape);print(array.dtype)