import cv2
import numpy as np
from matplotlib import pyplot as plt

input_img1 = "./Open/t01/5.jpg"

src = cv2.imread(input_img1, cv2.IMREAD_GRAYSCALE)

cv2.imshow(input_img1, src)
cv2.waitKey(0)
cv2.destroyAllWindows()
