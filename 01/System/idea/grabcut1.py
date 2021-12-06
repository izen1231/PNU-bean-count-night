import sys
import numpy as np
import cv2


# 입력 영상 불러오기
input_img1 = "./Open/t25/5.jpg"
src = cv2.imread(input_img1) 

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
rc = cv2.selectROI(src)
#(621, 221, 2988, 2624)
print(rc)
mask = np.zeros(src.shape[:2], np.uint8)


cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:, :, np.newaxis]

# 초기 분할 결과 출력
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
