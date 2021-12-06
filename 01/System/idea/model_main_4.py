import numpy as np
import cv2

def get_s_area(img_path, res_l):
    src = cv2.imread(img_path)
    rc = (975, 909, 2555, 999)
    src = src[rc[1]:rc[1]+rc[3], rc[0]:rc[0]+rc[2]]
    dst = src
    src_hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

    # dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
    dst1 = cv2.inRange(src_hsv, (16, 13, 0), (80, 250, 255))
    dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)

    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE,kernel, iterations = 15)
    bg = cv2.dilate(closing, kernel, iterations = 1)
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
    res_l.append(sum(sum(fg)))

def get_a_area(img_path, res_l):
    src=cv2.imread(img_path)
    rc = (975, 909, 2555, 999)
    src = src[rc[1]:rc[1]+rc[3], rc[0]:rc[0]+rc[2]]
    dst = src
    src_hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

        # dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
    dst1 = cv2.inRange(src_hsv, (16, 13, 0), (80, 250, 255))
    dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)

    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE,kernel, iterations = 15)
    bg = cv2.dilate(closing, kernel, iterations = 1)
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
    res_l.append(sum(sum(fg)))

f1_l = "./Open"
f2_l = [f"/t{i}" for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09"] + [i for i in range(10, 31)]]
f3_l = [f"/{i}.jpg" for i in range(1,6)]

pf_l = [f1_l+i for i in f2_l]
f_l_1 = [i+f3_l[0] for i in pf_l]
f_l_2 = [i+f3_l[1] for i in pf_l]
f_l_3 = [i+f3_l[2] for i in pf_l]
f_l_4 = [i+f3_l[3] for i in pf_l]
f_l_5 = [i+f3_l[4] for i in pf_l]

res_l_1 = []
for i in f_l_1:
    get_s_area(i, res_l_1)

res_l_2 = []
for i in f_l_2:
    get_s_area(i, res_l_2)

res_l_3 = []
for i in f_l_3:
    get_s_area(i, res_l_3)

res_l_4 = []
for i in f_l_4:
    get_s_area(i, res_l_4)

res_l_5 = []
for i in f_l_5:
    get_a_area(i, res_l_5)

# res_count = pd.read_excel("./Open/Kong_Open_True.xlsx", skiprows=1)
f = open("count.txt", 'r')
line = f.readline()
count = line.split()
f.close()

x = [res_l_1[i]+res_l_2[i]+res_l_3[i]+res_l_4[i]+res_l_5[i] for i in range(len(res_l_1))]
y = [int(i) for i in count]
y.sort
# print(y)
# plt.plot(np.log(x),y,'o')

linear_model=np.polyfit(x,y,3)
f = open("para4.txt", 'w')
for i in range(len(linear_model)):
    data = linear_model[i]
    f.write(str(data)+" ")
f.close()
linear_model_fn=np.poly1d(linear_model)

y_new = linear_model_fn(x)

res = [100*abs(y_new[i]-y[i])/y[i]**2 for i in range(len(x))]
print(sum(res))
