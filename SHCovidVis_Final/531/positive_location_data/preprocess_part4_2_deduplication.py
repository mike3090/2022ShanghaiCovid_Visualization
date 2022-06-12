import json
import requests
import csv

fR=open("position2_partNew.csv","r",encoding="utf-8",errors='ignore')
fW=open("position_count2.csv","w",encoding="utf-8",errors='ignore')
fRef=open("position_count2_new_save.csv","r",encoding="utf-8",errors='ignore')
readerRef=csv.reader(fRef)
readerR=csv.reader(fR)


tmpList=[]
for row in readerRef:
    if(row!=[] and row!=['position','count','lng','lat']):
        tmpList.append(row)
flag=0
for row in readerR:
    if(row!=[] and row!=['position','count','lng','lat']):
        for i in tmpList:
            if row[0] in i[0]:
                print((row[0],row[1],i[0],i[1]))
                i[1]=int(i[1])
                row[1]=int(row[1])
                i[1]=row[1]+i[1]
                print(i[1])
                flag=1
                break
        if(flag==0):
            tmpList.append(row) 
        flag=0   

writer=csv.writer(fW)
writer.writerows(tmpList)

fR.close()
fRef.close()
fW.close()