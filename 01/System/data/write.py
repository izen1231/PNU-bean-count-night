import pandas as pd

res_count = pd.read_excel("./Hidden/Kong_hidden_True.xlsx", skiprows=1)
count = list(res_count["amount"])
f = open("./01/System/data/count_close.txt", 'w')
for i in range(len(count)):
    data = count[i]
    f.write(str(data)+" ")
f.close()