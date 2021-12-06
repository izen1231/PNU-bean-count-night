import cv2
import numpy as np
from matplotlib import pyplot as plt

input_img1 = "./Open/t01/5.jpg"

src=cv2.imread(input_img1,cv2.IMREAD_GRAYSCALE)
dst=cv2.Canny(src,20,150)
plt.imshow(dst)

# erasing noise
# cnt1, _ = cv2.connectedComponents(dst)
# print("cnt1: ", cnt1)
# dst2 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, None)
# cnt2, _ = cv2.connectedComponents(dst2)
# print("cnt2: ", cnt2)

# cv2.imshow(input_img1, dst2)

cv2. imshow(input_img1, dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
