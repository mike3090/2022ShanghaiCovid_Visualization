#0306
'''
f=open("raw/20220306.txt",'r',encoding='UTF-8')
fR=open("processed/0306.txt",'w',encoding="UTF-8")
L=f.readlines()
print(L)
#print(L[2][1])
lenL=len(L)
resultList=[]
lenHead=len("居住地为")
for i in range(lenL):
    if L[i].count("居住地为")!=0:
        while L[i].count("居住地为")!=0:
            begi=L[i].find("居住地为")
            ending=L[i].find("，",begi)
            
            resultList.append(L[i][begi+lenHead:ending]+'\n')
            L[i]=L[i][begi+1:len(L[i])]
            #print(L[i])
print(resultList)
#for i in range(len(resultList)):
#    fR.write(resultList[i])
fR.writelines(resultList)

fR.close()
f.close()
'''



#0307-0321
'''
for i in range(7,10):
    f=open("raw/2022030"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    fR=open("processed/030"+str(i)+".txt",'w',encoding="UTF-8",errors='ignore')
    L=f.readlines()
    print(L)
    lenL=len(L)
    resultList=[]
    lenHead=len("居住于")
    for i in range(lenL):
        if L[i].count("居住于")!=0:
            while L[i].count("居住于")!=0:
                begi=L[i].find("居住于")
                ending=min(L[i].find("，",begi),L[i].find("。",begi))
                resultList.append(L[i][begi+lenHead:ending]+'\n')
                L[i]=L[i][begi+1:len(L[i])]
                
    print(resultList)
    fR.writelines(resultList)
    fR.close()
    f.close()

for i in range(10,32):
    f=open("raw/202203"+str(i)+".txt",'r',encoding="UTF-8",errors='ignore')
    fR=open("processed/03"+str(i)+".txt",'w',encoding="UTF-8",errors='ignore')
    L=f.readlines()
    print(L)
    lenL=len(L)
    resultList=[]
    lenHead=len("居住于")
    for i in range(lenL):
        if L[i].count("居住于")!=0:
            while L[i].count("居住于")!=0:
                begi=L[i].find("居住于")
                ending=min(L[i].find("，",begi),L[i].find("。",begi))
                resultList.append(L[i][begi+lenHead:ending]+'\n')
                L[i]=L[i][begi+1:len(L[i])]
                
    print(resultList)
    fR.writelines(resultList)
    fR.close()
    f.close()
'''
#0322-0426

'''
data=""
with open('raw/20220426.txt','r',encoding='UTF-8') as f:
    text=f.readline()
    if text[0]!='居':
        text=f.readline()
    while text:
        text=list(text)
        del text[0:3]
        del text[-2:-1]
        text="".join(text)
        data+=text
        text=f.readline()
with open('processed/0426.txt',"w",encoding="UTF-8") as fR:
    fR.write(data)
'''

#0427-
'''
for i in range(27,31):
    f=open("raw/202204"+str(i)+".txt",'r',encoding='UTF-8')
    fR=open("processed/04"+str(i)+".txt",'w',encoding="UTF-8")
    L=f.readlines()
    lenL=len(L)
    resultList=[]
    for j in range(lenL):
        if(L[j]!="\n"):
            if(L[j][-2]=="，" or L[j][-2]=="、" or L[j][-2]=="。"):
                resultList.append(L[j][0:len(L[j])-2]+"\n")
            elif(L[j][-1]=="，" or L[j][-1]=="、" or L[j][-1]=="。"):
                resultList.append(L[j][0:len(L[j])-1])
            else:
                resultList.append(L[j])
    fR.writelines(resultList)
    f.close()
    fR.close()


for i in range(1,10):
    f=open("raw/2022050"+str(i)+".txt",'r',encoding='UTF-8')
    fR=open("processed/050"+str(i)+".txt",'w',encoding="UTF-8")
    L=f.readlines()
    lenL=len(L)
    resultList=[]
    for j in range(lenL):
        if(L[j]!="\n"):
            if(L[j][-2]=="，" or L[j][-2]=="、" or L[j][-2]=="。"):
                resultList.append(L[j][0:len(L[j])-2]+"\n")
            elif(L[j][-1]=="，" or L[j][-1]=="、" or L[j][-1]=="。"):
                resultList.append(L[j][0:len(L[j])-1])
            else:
                resultList.append(L[j])
    fR.writelines(resultList)
    f.close()
    fR.close()

for i in range(10,13):
    f=open("raw/202205"+str(i)+".txt",'r',encoding='UTF-8')
    fR=open("processed/05"+str(i)+".txt",'w',encoding="UTF-8")
    L=f.readlines()
    lenL=len(L)
    resultList=[]
    for j in range(lenL):
        if(L[j]!="\n"):
            if(L[j][-2]=="，" or L[j][-2]=="、" or L[j][-2]=="。"):
                resultList.append(L[j][0:len(L[j])-2]+"\n")
            else:
                resultList.append(L[j])
    fR.writelines(resultList)
    f.close()
    fR.close()
'''