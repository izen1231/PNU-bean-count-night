import pandas as pd
res_count = pd.read_excel("./Open/Kong_Open_True.xlsx", skiprows=1)
print(res_count)
count = list(res_count["amount"])
print(count)