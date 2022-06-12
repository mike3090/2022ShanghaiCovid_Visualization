import os
import csv

current_path = os.path.dirname(os.path.abspath(__file__))
with open(current_path + '\\Rt.csv') as f:
    freader = csv.reader(f)
    arrtmp = []
    for i in freader:
        arrtmp.append(i)
    arrtmp1 = [['date', 'district', 'rt']]
    for i in range(1, len(arrtmp), 1):
        for j in range(1, len(arrtmp[0]), 1):
            arrtmp1.append([i, arrtmp[0][j], arrtmp[i][j]])
    print(len(arrtmp), len(arrtmp[0]), len(arrtmp1))

with open(current_path + '\\Rt_transformed.csv','w',newline='') as f:
    #for i in arrtmp2:
        #i.pop(1)
    f_csv = csv.writer(f)
    f_csv.writerows(arrtmp1)
    print(arrtmp[0])