import os
import sys
import cv2
import random
import numpy as np

# 디렉토리 파일 모두 읽기
path = "./capture"
file_lst = os.listdir(path)
print(file_lst)

img = cv2.imread(path + '/' + file_lst[0])
if img is None:
    print('Image load failed!')
    sys.exit()

input_image = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21) # 이미지 잡음 제거
print('shape: ', input_image.shape)

height, width = input_image.shape[:2]  # 이미지의 높이와 너비 불러옴, 가로 [0], 세로[1]

img_hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)  # cvtColor 함수를 이용하여 hsv 색공간으로 변환

dst1 = cv2.inRange(input_image, (0, 128, 0), (100, 255, 100))
dst2 = cv2.inRange(img_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', input_image)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
#
# lower_color = (21 - 10, 30, 30)  # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
# upper_color = (21 + 10, 255, 255)
# img_mask = cv2.inRange(img_hsv, lower_color, upper_color)  # 범위내의 픽셀들은 흰색, 나머지 검은색
#
# # 바이너리 이미지를 마스크로 사용하여 원본이미지에서 범위값에 해당하는 영상부분을 획득
# img_result = cv2.bitwise_and(input_image, input_image, mask=img_mask)
#
# cv2.imshow('img_origin', input_image)
# cv2.imshow('img_mask', img_mask)
# cv2.imshow('img_color', img_result)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
