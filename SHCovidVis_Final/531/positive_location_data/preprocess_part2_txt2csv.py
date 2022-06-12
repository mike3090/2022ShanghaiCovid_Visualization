import csv
'''
#0306

f0=open("processed/0306.txt",'r',encoding="UTF-8",errors='ignore')
f=f0.readlines()
Lf=len(f)

fR=open("processed2/0306.csv",'w',encoding="UTF-8",errors='ignore')
writer=csv.writer(fR)
writer.writerow(['position','lng','lat'])
for j in range(0,Lf):
    writer.writerow((f[j][0:len(f[j])-1],0,0))
f0.close()
fR.close()

#0307-0309

for i in range(7,10):
    f0=open("processed/030"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    f=f0.readlines()
    Lf=len(f)
    
    fR=open("processed2/030"+str(i)+".csv",'w',encoding="UTF-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','lng','lat'])
    for j in range(0,Lf):
        writer.writerow((f[j][0:len(f[j])-1],0,0))
    f0.close()
    fR.close()

#0310-0331

for i in range(10,32):
    f0=open("processed/03"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    f=f0.readlines()
    Lf=len(f)
    #print(i)
    fR=open("processed2/03"+str(i)+".csv",'w',encoding="UTF-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','lng','lat'])
    for j in range(0,Lf):
        writer.writerow((f[j][0:len(f[j])-1],0,0))
    f0.close()
    fR.close()


#0401-0409

for i in range(1,10):
    f0=open("processed/040"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    f=f0.readlines()
    Lf=len(f)
    
    fR=open("processed2/040"+str(i)+".csv",'w',encoding="UTF-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','lng','lat'])
    for j in range(0,Lf):
        writer.writerow((f[j][0:len(f[j])-1],0,0))
    f0.close()
    fR.close()

#0410-0426

for i in range(10,27):
    f0=open("processed/04"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    f=f0.readlines()
    Lf=len(f)
    #print(i)
    fR=open("processed2/04"+str(i)+".csv",'w',encoding="UTF-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','lng','lat'])
    for j in range(0,Lf):
        writer.writerow((f[j][0:len(f[j])-1],0,0))
    f0.close()
    fR.close()

'''

#0427-

for i in range(27,31):
    f0=open("processed/04"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    f=f0.readlines()
    Lf=len(f)
    #print(i)
    fR=open("processed2/04"+str(i)+".csv",'w',encoding="UTF-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','lng','lat'])
    for j in range(0,Lf):
        writer.writerow((f[j][0:len(f[j])-1],0,0))
    f0.close()
    fR.close()

for i in range(1,10):
    f0=open("processed/050"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    f=f0.readlines()
    Lf=len(f)
    
    fR=open("processed2/050"+str(i)+".csv",'w',encoding="UTF-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','lng','lat'])
    for j in range(0,Lf):
        writer.writerow((f[j][0:len(f[j])-1],0,0))
    f0.close()
    fR.close()

for i in range(10,13):
    f0=open("processed/05"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    f=f0.readlines()
    Lf=len(f)
    #print(i)
    fR=open("processed2/05"+str(i)+".csv",'w',encoding="UTF-8",errors='ignore')
    writer=csv.writer(fR)
    writer.writerow(['position','lng','lat'])
    for j in range(0,Lf):
        writer.writerow((f[j][0:len(f[j])-1],0,0))
    f0.close()
    fR.close()