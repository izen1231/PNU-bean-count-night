import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
import datetime as dt

def get_a_area(img_path, res_l):
    src=cv2.imread(img_path)
    rc = (975, 909, 2555, 999)
    src = src[rc[1]:rc[1]+rc[3], rc[0]:rc[0]+rc[2]]
    dst = src
    src_hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

        # dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
    dst1 = cv2.inRange(src_hsv, (16, 13, 0), (80, 250, 255))
    dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)

    kernel = np.ones((6, 6), np.uint8)
    closing = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE,kernel, iterations = 15)
    bg = cv2.dilate(closing, kernel, iterations = 1)
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
    res_l.append(sum(sum(fg)))

start = time.time() 
f1_l = "./Open"
f2_l = [f"/t{i}" for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09"] + [i for i in range(10, 31)]]
f3_l = [f"/{i}.jpg" for i in range(1,6)]

pf_l = [f1_l+i for i in f2_l]
f_l_5 = [i+f3_l[4] for i in pf_l]
print(f_l_5)
res_l_5 = []
for i in f_l_5:
    get_a_area(i, res_l_5)

f = open("./01/System/data/count_open.txt", 'r')
line = f.readline()
count = line.split()
f.close()

x = res_l_5
y = [int(i) for i in count]

linear_model=np.polyfit(x,y,3)
linear_model_fn=np.poly1d(linear_model)

f1_l = "./Hidden"
f2_l = [f"/t{i}" for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09"] + [i for i in range(10, 31)]]
f3_l = [f"/{i}.jpg" for i in range(1,6)]

pf_l = [f1_l+i for i in f2_l]
f_l_5 = [i+f3_l[4] for i in pf_l]

res_l_5 = []
for i in f_l_5:
    get_a_area(i, res_l_5)

new_x = res_l_5
y_new = linear_model_fn(new_x)

d = dt.datetime.now()

f = open("./01/Out/Kong_01.txt", 'w')
f.write("Team  PongPongLab\n")
date = "Date  " + f"{d.month}-{d.day}-{d.hour}-{d.minute}-{d.second}"+"\n"
f.write(date)
t = "Time  "+str(round(time.time() - start,2))+"\n"
f.write(t)
c = "Cases "+str(len(res_l_5))+"\n"
f.write(c)
for i in range(len(y_new)):
    data = y_new[i]
    f_d = str(f2_l[i][1:])+"  "+str(round(data,3))+"\n"
    f.write(f_d)
f.close()

f = open("./01/System/data/count_hidden.txt", 'r')
line = f.readline()
count = line.split()
f.close()
y = [int(i) for i in count]

n = len(y_new)
err1 = [(100*abs(y_new[i]-y[i])/y[i])**2 for i in range(n)]
print(sum(err1)) 
err2 = [100*abs(y_new[i]-y[i])/y[i] for i in range(n)]
print(sum(err2))
 

