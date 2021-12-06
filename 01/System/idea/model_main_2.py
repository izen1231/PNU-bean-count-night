import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_s_area(img_path, res_l):
    src = cv2.imread(img_path)
    rc = (975, 909, 2555, 999)
    src = src[rc[1]:rc[1]+rc[3], rc[0]:rc[0]+rc[2]]
    rc = (100, 0, 2300, 990)
    mask = np.zeros(src.shape[:2], np.uint8)

    cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

    # 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
    mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
    dst = src * mask2[:, :, np.newaxis]
    src_hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

    # dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
    dst1 = cv2.inRange(src_hsv, (16, 13, 0), (80, 250, 255))
    dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)
    res_l.append(sum(sum(dst2)))

f1_l = "./Open"
f2_l = [f"/t{i}" for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09"] + [i for i in range(10, 31)]]
f3_l = [f"/{i}.jpg" for i in range(1,6)]

pf_l = [f1_l+i for i in f2_l]
f_l_1 = [i+f3_l[0] for i in pf_l]

dic = dict()

res_l_1 = []
for i in f_l_1:
    get_s_area(i, res_l_1)

f = open("count.txt", 'r')
line = f.readline()
count = line.split()
f.close()

dic["count"] = count

x = res_l_1
y = count
y.sort
# print(y)
# plt.plot(np.log(x),y,'o')

linear_model=np.polyfit(x,y,3)
f = open("para2.txt", 'w')
for i in range(len(linear_model)):
    data = linear_model[i]
    f.write(str(data)+" ")
f.close()

linear_model_fn=np.poly1d(linear_model)

y_new = linear_model_fn(x)

res = [100*abs(y_new[i]-y[i])/y[i]**2 for i in range(len(x))]
print(sum(res))
