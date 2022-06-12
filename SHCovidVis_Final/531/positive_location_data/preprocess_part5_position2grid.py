import csv
import json
f0=open('position_count2.csv','r',encoding='utf-8',errors='ignore')
reader0=csv.reader(f0)
tmpList=[]#let it be 123*90
'''
j:90 columns

   j
[ [] [] ] i: 123 rows
[ [] [] ]
[ [] [] ]
[ [] [] ]
each one: [i][j]
[0][0]: left-down
[123][0]: left-up
'''
tmpList_copy=[]
tmpList0=[]
x1=120.864463
y1=30.697938
xList=[x1]
yList=[y1]
tmpList1=[]
tmpList2=[]

for k in range(90):
    tmpList0.append([])
    tmpList2.append([])
    xList.append(x1+(k+1)*0.0126)#similarly x2.
for k in range(123):
    tmpList1.append([])#store 123 rows
    tmpList.append(tmpList0)
    tmpList_copy.append(tmpList0)
    yList.append(y1+(k+1)*0.0096)#y2=31.878739 instead of 31.878740. Thus using []<lat<=[].



for row in reader0:
    if(row!=[] and row!=['position','count','lng','lat']):
        lng=float(row[2])
        lat=float(row[3])
        #print(lat)
        #print(lng)
        for i in range(123):
            if (yList[i]<lat and lat<yList[i]+0.0096):
                tmpList1[i].append(row)
        for j in range(90):
            if (xList[j]<lng and lng<xList[j]+0.0126):
                tmpList2[j].append(row)



for i0 in range(123):
    
    if(len(tmpList1[i0])!=0):
        for k in (tmpList1[i0]):
            lng=float(k[2])
            lat=float(k[3])
            for j in range(90):
                if(xList[j]<lng and lng<xList[j]+0.0126 and yList[i0]<lat and lat<yList[i0]+0.0096):
                    tmpList[i0][j].append(k)

                 
def access(i,j):
    res =[]
    for k in tmpList[i][j]:
        lng=float(k[2])
        lat=float(k[3])
        if(xList[j]<lng and lng<xList[j]+0.0126 and yList[i]<lat and lat<yList[i]+0.0096):
            res.append(k)
    return res
#傻逼bug修不好，绕开吧。bug：尝试直接输出tmpList[i][j]就知道了。

print(access(30,30))

def accessName(i,j):
    res =[]
    for k in tmpList[i][j]:
        lng=float(k[2])
        lat=float(k[3])
        if(xList[j]<lng and lng<xList[j]+0.0126 and yList[i]<lat and lat<yList[i]+0.0096):
            res.append(k[0])
    return res

finalDict={}
finalDictOnlyName={}
for i in range(123):
    for j in range(90):
        #If you need to output csv, then de-comment these lines.
        '''
        fR=open('processed3_2_gridInfo/'+str(i)+"_"+str(j)+".csv",'w',encoding='utf-8',errors='ignore')
        writer=csv.writer(fR)
        writer.writerow(['position','count','lng','lat'])
        writer.writerows(access(i,j))
        fR.close()
        '''
        finalDict[str(i)+"_"+str(j)]=access(i,j)
        finalDictOnlyName[str(i)+"_"+str(j)]=accessName(i,j)
print(finalDict["30_30"])



fJson=open('processed3_2_gridInfo/dataJson.json','w',encoding='utf-8',errors='ignore')
json_res=json.dump(finalDict,fJson)
f0.close()
fJson.close()

fJson2=open('processed3_2_gridInfo/dataJsonOnlyName.json','w',encoding='utf-8',errors='ignore')
json_res=json.dump(finalDictOnlyName,fJson2)
fJson2.close()