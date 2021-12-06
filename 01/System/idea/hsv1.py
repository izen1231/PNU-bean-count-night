import sys
import numpy as np
import cv2
import time
start = time.time()  # 시작 시간 저장
 
input_img1 = "./Open/t25/1.jpg"
src = cv2.imread(input_img1)
#src = cv2.imread('candies2.png')
if src is None:
    print('Image load failed!')
    sys.exit()

rc = (975, 909, 2555, 999)
src = src[rc[1]:rc[1]+rc[3], rc[0]:rc[0]+rc[2]]
# rc = (100, 0, 2300, 990)
# mask = np.zeros(src.shape[:2], np.uint8)

# cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# # 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
# mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
# dst = src * mask2[:, :, np.newaxis]
dst = src
src_hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

# dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
dst1 = cv2.inRange(src_hsv, (16, 13, 0), (80, 250, 255))

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

cnt1, _ = cv2.connectedComponents(dst1)
dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)
cnt2, _ = cv2.connectedComponents(dst2)
print(sum(sum(dst2)))
cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
