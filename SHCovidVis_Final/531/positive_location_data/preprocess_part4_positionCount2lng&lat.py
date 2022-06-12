import json
import requests
import csv
from urllib.parse import urlencode

requests.adapters.DEFAULT_RETRIES=5
'''
fRr=open("position_count.csv","r",encoding="utf-8",errors='ignore')
fRw=open("position_count2_new.csv","w",encoding="utf-8",errors='ignore')
reader0=csv.reader(fRr)
tmpList=[]
i=0
for row in reader0:
    
    if(row!=[] and row!=['position','count','lng','lat']):
        print(row)
        print('-2')
        url = "https://api.map.baidu.com/geocoding/v3/"
        params={'address':row[0],'output':'json','ak':'Q9qEZOG1OpVy6iNLU1DdAhVPc8KLSuce'}
        res=requests.get(url,params)
        jd=json.loads(res.text)
        if(jd['status']==0):
            print("-1")
            lng=jd['result']['location']['lng']
            lat=jd['result']['location']['lat']
            tmpList.append([row[0],row[1],lng,lat])
        else:
            print(i)
            i=i+1
    else:
        print('nope')

writer=csv.writer(fRw)
writer.writerow(["position","count","lng","lat"])
for i in tmpList:
    writer.writerow(i)


fRw.close()
fRr.close()
'''

fRr=open("position_count.csv","r",encoding="utf-8",errors='ignore')
fRw=open("position_count2_new.csv","w",encoding="utf-8",errors='ignore')
#fRw=open("position2_partNew.csv","w",encoding="utf-8",errors='ignore')
fR_ref=open("position_count2_until0426.csv","r",encoding="utf-8",errors='ignore')
refReader=csv.reader(fR_ref)
reader0=csv.reader(fRr)
refList=[]
i=0
writer=csv.writer(fRw)
writer.writerow(["position","count","lng","lat"])
header0 = {'Connection':'close'}
for row in refReader:
    if(row!=[] and row!=['position','count','lng','lat']):
        refList.append(row[0])
for row in reader0:
    if(row!=[] and row!=['position','count','lng','lat']):
        print(row)
        if(row!=[] and row!=['position','count','lng','lat']):
            print('-2')
            
            s = requests.session()
            s.keep_alive = False

            url = "https://api.map.baidu.com/geocoding/v3/?"
            params={'address':row[0],'city':"上海市",'output':'json','ak':'Q9qEZOG1OpVy6iNLU1DdAhVPc8KLSuce'}
            #par=urlencode(params)
            #url=url0+par
            #url0=url+"?address="+row[0]+"&city=上海市&output=json&ak=Q9qEZOG1OpVy6iNLU1DdAhVPc8KLSuce"
            #print(url0 )
            
            #res=requests.get(url,params)
            try:
                res=s.get(url,params=params,headers=header0,timeout=100)
            except requests.exceptions.RequestException as e:
                print(e)
            jd=json.loads(res.text)
            if(jd['status']==0):
                print("-1")
                lng=jd['result']['location']['lng']
                lat=jd['result']['location']['lat']
                #print(lng)
                #print(lat)
                #tmpList.append([row[0],row[1],lng,lat])
                writer.writerow([row[0],row[1],lng,lat])
            else:
                print(i)
                i=i+1
        else:
            print('nope')





'''
    if(row!=[] and row!=['position','count','lng','lat']):
        if row[0] not in refList:
            tmpList=[]
            print(row)
            if(row!=[] and row!=['position','count','lng','lat']):
                #print('-2')
                
                url = "https://api.map.baidu.com/geocoding/v3/"
                params={'address':"上海市"+row[0],'output':'json','ak':'Q9qEZOG1OpVy6iNLU1DdAhVPc8KLSuce'}
                #url0=url+"?address="+row[0]+"&city=上海市&output=json&ak=Q9qEZOG1OpVy6iNLU1DdAhVPc8KLSuce"
                #print(url0 )
                res=requests.get(url,params)
                
                jd=json.loads(res.text)
                if(jd['status']==0):
                    print("-1")
                    lng=jd['result']['location']['lng']
                    lat=jd['result']['location']['lat']
                    print(lng)
                    print(lat)
                    #tmpList.append([row[0],row[1],lng,lat])
                    writer.writerow([row[0],row[1],lng,lat])
                else:
                    print(i)
                    i=i+1
            else:
                print('nope')
    

'''

#for i in tmpList:
    #writer.writerow(i)

fRw.close()
fRr.close()
fR_ref.close()
