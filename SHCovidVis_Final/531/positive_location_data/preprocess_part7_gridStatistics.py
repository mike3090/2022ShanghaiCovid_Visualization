import json
import csv
'''
tmpList=[]
tmpList0=[]
for i0 in range(90):
    tmpList0.append([])
for i0 in range(123):
    tmpList.append(tmpList0)
#90*123 List
'''
fJson=open('processed3_2_gridInfo/dataJson.json','r',encoding='utf-8',errors='ignore')
data=json.load(fJson)
fJsonR=open('processed3_3_gridDailyStatistics/dailyZoneCount.json','w',encoding='utf-8',errors='ignore')
res={}#zone->date->newCasesThatDay
#eg: zone 30_30 -> date 3_20 -> new cases: xxx
for i in range(0,123):
    for j in range(0,90):
        name='zone'+str(i)+'_'+str(j)
        res[name]={} #"zone30_30"
        for m in range(6,32):
            res[name]['day3_'+str(m)]=0 #"day3_6"
        for n in range(1,31):
            res[name]['day4_'+str(n)]=0
        for l in range(1,13):
            res[name]['day5_'+str(l)]=0
#print(res)

for m in range(6,32):
    f0=open("processed3_1_position2zone/3_"+str(m)+'.csv','r',encoding='utf-8',errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'zone','lng','lat']):
            name='zone'+row[1]
            #print(name)
            res[name]['day3_'+str(m)]+=1
    f0.close()

for m in range(1,31):
    f0=open("processed3_1_position2zone/4_"+str(m)+'.csv','r',encoding='utf-8',errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'zone','lng','lat']):
            name='zone'+row[1]
            res[name]['day4_'+str(m)]+=1
    f0.close()

for m in range(1,13):
    f0=open("processed3_1_position2zone/5_"+str(m)+'.csv','r',encoding='utf-8',errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'zone','lng','lat']):
            name='zone'+row[1]
            res[name]['day4_'+str(m)]+=1
    f0.close()

json_res=json.dump(res,fJsonR)


fJson.close()
fJsonR.close()