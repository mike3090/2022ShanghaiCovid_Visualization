import csv
import os

current_path = os.path.dirname(__file__)
file = open(current_path + '/../district_data/Shanghai_region_data_T.csv', 'r')
with file as f:
    freader = csv.reader(f)
    arrtmp = []
    for i in freader:
        arrtmp.append(i)
    #print(arrtmp)
    arrtmp1 = []
    for i in range(len(arrtmp[0])):
        arrtmp1.append([])
        for j in range(len(arrtmp)):
            if j != 0 and i != 0:
                arrtmp1[i].append(int(arrtmp[j][i]))
            else:
                arrtmp1[i].append(arrtmp[j][i])
    arrtmp2 = []
    arrtmp2.append(arrtmp1[0])
    print(arrtmp1)

with open(current_path + '/../district_data/city_dist_unmerged_date.csv','w',newline='') as f:
    #for i in arrtmp2:
        #i.pop(1)
    f_csv = csv.writer(f)
    f_csv.writerows(arrtmp1)
    '''
    for i in range(1, (len(arrtmp1) // 2), 1):
        arrtmp2.append([])
        for j in range(len(arrtmp1[0])):
            if j == 0:
                arrtmp2[i].append(arrtmp1[2 * i][j].split('_')[j])
            else:
                arrtmp2[i].append(arrtmp1[2 * i][j] + arrtmp1[2 * i - 1][j])
    
with open(current_path + '/../district_data/Shanghai_merged_day.csv','w',newline='') as f:
    arrtmp3 = []
    for i in range(len(arrtmp2)):
        arrtmp3.append([])
        arrtmp3[i].append(arrtmp2[i][0])
        arrtmp3[i].append(arrtmp2[i][1])
    f_csv = csv.writer(f)
    f_csv.writerows(arrtmp3)

with open(current_path + '/../district_data/city_dist_merged_date.csv','w',newline='') as f:
    #for i in arrtmp2:
        #i.pop(1)
    f_csv = csv.writer(f)
    f_csv.writerows(arrtmp2)
    '''

