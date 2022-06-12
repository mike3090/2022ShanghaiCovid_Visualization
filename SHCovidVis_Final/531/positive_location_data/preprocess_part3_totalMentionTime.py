import csv

fRr=open("position_count.csv","r",encoding="utf-8",errors='ignore')
fRw=open("position_count.csv","w",encoding="utf-8",errors='ignore')
reader0=csv.reader(fRr)
posCount={}
result=[]
for row in reader0:
    if(row!=[]):
        posCount[row[0]]=row[1]

#0306-0309

for i in range(6,10):
    f0=open("processed2/030"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            if(posCount.get(row[0],-1)==-1):
                posCount[row[0]]=1
            else:
                posCount[row[0]]=posCount[row[0]]+1

    f0.close()




#0310-0331
for i in range(10,32):
    f0=open("processed2/03"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            if(posCount.get(row[0],-1)==-1):
                posCount[row[0]]=1
            else:
                posCount[row[0]]=posCount[row[0]]+1

    f0.close()

#0401-0409
for i in range(1,10):
    f0=open("processed2/040"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            if(posCount.get(row[0],-1)==-1):
                posCount[row[0]]=1
            else:
                posCount[row[0]]=posCount[row[0]]+1

    f0.close()

#0410-0426
for i in range(10,27):
    f0=open("processed2/04"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            if(posCount.get(row[0],-1)==-1):
                posCount[row[0]]=1
            else:
                posCount[row[0]]=posCount[row[0]]+1

    f0.close()
#'''
#0427-0430
for i in range(27,31):
    f0=open("processed2/04"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            if(posCount.get(row[0],-1)==-1):
                posCount[row[0]]=1
            else:
                posCount[row[0]]=posCount[row[0]]+1

    f0.close()


#0501-0510
for i in range(1,10):
    f0=open("processed2/050"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            if(posCount.get(row[0],-1)==-1):
                posCount[row[0]]=1
            else:
                posCount[row[0]]=posCount[row[0]]+1

    f0.close()

#0510-

for i in range(10,13):
    f0=open("processed2/04"+str(i)+".csv",'r',encoding="utf-8",errors='ignore')
    reader=csv.reader(f0)
    for row in reader:
        if(row!=[] and row!=['position', 'lng', 'lat']):
            if(posCount.get(row[0],-1)==-1):
                posCount[row[0]]=1
            else:
                posCount[row[0]]=posCount[row[0]]+1

    f0.close()
#'''




for key,value in posCount.items():
    result.append([key,value])
for i in range(len(result)):
    result[i].append(0)
    result[i].append(0)

writer=csv.writer(fRw)
writer.writerow(["position","count","lng","lat"])
for i in result:
    writer.writerow(i)

fRw.close()
fRr.close()

