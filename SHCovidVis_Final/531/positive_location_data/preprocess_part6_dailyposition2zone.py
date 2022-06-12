import csv
import json
fD=open('processed3_2_gridInfo/dataJsonOnlyName.json','r',encoding='utf-8',errors='ignore')
#fC=open('position_count2.csv','r',encoding='utf-8',errors='ignore')#for 0306-0426
fC=open('position2_partNew.csv','r',encoding='utf-8',errors='ignore')#for 0427-0512
data=json.load(fD)
#print(data)
dataVal=list(data.values())
dataKeys=list(data.keys())

reader0=csv.reader(fC)
totalList=[]
for row in reader0:
    if(row!=[] and row!=['position', 'lng', 'lat']):
        totalList.append(row)

#print(dataVal)
def getZone(s):
    for i in range(len(dataVal)):
        if (s in dataVal[i]):
            return dataKeys[i]

def getLngLat(s):
    for i in range(len(totalList)):
        if (s in totalList[i]):
            return (totalList[i][2],totalList[i][3])

#print(getZone('金山区九龙村'))
'''
#0306-0309
for i in range(6,10):
    f0=open("processed2/030"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    fR=open("processed3_1_position2zone/3_"+str(i)+".csv",'w',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    writer=csv.writer(fR)
    writer.writerow(['position','zone','lng','lat'])
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            res=getZone(row[0])
            LngLat=getLngLat(row[0])
            lng=LngLat[0]
            lat=LngLat[1]
            if(res!=None):
                writer.writerow([row[0],res,lng,lat])

    f0.close()
    fR.close()

#0310-0331
for i in range(10,32):
    f0=open("processed2/03"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    fR=open("processed3_1_position2zone/3_"+str(i)+".csv",'w',encoding="utf-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','zone','lng','lat'])
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            res=getZone(row[0])
            LngLat=getLngLat(row[0])
            if(res!=None and LngLat!=None):
                lng=LngLat[0]
                lat=LngLat[1]
                writer.writerow([row[0],res,lng,lat])

    f0.close()
    fR.close()

#0401-0409
for i in range(1,10):
    f0=open("processed2/040"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    fR=open("processed3_1_position2zone/4_"+str(i)+".csv",'w',encoding="utf-8",errors='ignore')
    writer=csv.writer(fR)
    
    writer.writerow(['position','zone','lng','lat'])
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            res=getZone(row[0])
            LngLat=getLngLat(row[0])
            if(res!=None and LngLat!=None):
                lng=LngLat[0]
                lat=LngLat[1]
                writer.writerow([row[0],res,lng,lat])

    f0.close()
    fR.close()

#0410-0426
for i in range(10,27):
    f0=open("processed2/04"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    fR=open("processed3_1_position2zone/4_"+str(i)+".csv",'w',encoding="utf-8",errors='ignore')
    writer=csv.writer(fR)
    
    writer.writerow(['position','zone','lng','lat'])
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            res=getZone(row[0])
            LngLat=getLngLat(row[0])
            if(res!=None and LngLat!=None):
                lng=LngLat[0]
                lat=LngLat[1]
                writer.writerow([row[0],res,lng,lat])

    f0.close()
    fR.close()
'''
#0427-0430
for i in range(27,31):
    f0=open("processed2/04"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    fR=open("processed3_1_position2zone/4_"+str(i)+".csv",'w',encoding="utf-8",errors='ignore')
    writer=csv.writer(fR)
    
    writer.writerow(['position','zone','lng','lat'])
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            res=getZone(row[0])
            LngLat=getLngLat(row[0])
            if(res!=None and LngLat!=None):
                lng=LngLat[0]
                lat=LngLat[1]
                writer.writerow([row[0],res,lng,lat])

    f0.close()
    fR.close()

#0501-0509
for i in range(1,10):
    f0=open("processed2/050"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    fR=open("processed3_1_position2zone/5_"+str(i)+".csv",'w',encoding="utf-8",errors='ignore')
    writer=csv.writer(fR)
    
    writer.writerow(['position','zone','lng','lat'])
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            res=getZone(row[0])
            LngLat=getLngLat(row[0])
            if(res!=None and LngLat!=None):
                lng=LngLat[0]
                lat=LngLat[1]
                writer.writerow([row[0],res,lng,lat])

    f0.close()
    fR.close()

#0510-0512
for i in range(10,13):
    f0=open("processed2/05"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    fR=open("processed3_1_position2zone/5_"+str(i)+".csv",'w',encoding="utf-8",errors='ignore')
    writer=csv.writer(fR)
    
    writer.writerow(['position','zone','lng','lat'])
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            res=getZone(row[0])
            LngLat=getLngLat(row[0])
            if(res!=None and LngLat!=None):
                lng=LngLat[0]
                lat=LngLat[1]
                writer.writerow([row[0],res,lng,lat])

    f0.close()
    fR.close()





fD.close()
fC.close()