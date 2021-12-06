import cv2
import numpy as np
from matplotlib import pyplot as plt

input_img1 = "./Open/t01/5.jpg"

src=cv2.imread(input_img1,cv2.IMREAD_GRAYSCALE)
dx=cv2.Sobel(src,cv2.CV_32F,1,0)
print(dx.shape)
dy=cv2.Sobel(src,cv2.CV_32F,0,1)
mag=cv2.magnitude(dx,dy)
mag=np.clip(mag,0,255).astype(np.uint8)
dst=np.zeros(src.shape[:2],np.uint8)
dst[mag>120]=255
_,dst=cv2.threshold(mag,120,255,cv2.THRESH_BINARY)

# # erasing noise
# cnt1, _ = cv2.connectedComponents(dst)
# print("cnt1: ", cnt1)
# dst2 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, None)
# cnt2, _ = cv2.connectedComponents(dst2)
# print("cnt2: ", cnt2)

# cv2.imshow(input_img1, dst2)
cv2.imshow(input_img1, dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
