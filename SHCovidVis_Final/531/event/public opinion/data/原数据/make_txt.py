import json
for d in range(31,32):
    if d<10:
        f=open('C:\\Users\\Yuxinz\\Desktop\\public opinion\\data\\原数据\\原数据\\微博\\2022-03-0'+str(d)+'.json','r',encoding='UTF-8')
        data=json.load(f)
        txt=""
        for i in range(len(data)):
            txt+=data[i]["title"]
            txt+="\n"
        with open('2022-03-0'+str(d)+'.txt',"w",encoding="utf-8") as f:
            f.write(txt)
    else:
        f=open('C:\\Users\\Yuxinz\\Desktop\\public opinion\\data\\原数据\\原数据\\微博\\2022-03-'+str(d)+'.json','r',encoding='UTF-8')
        data=json.load(f)
        txt=""
        for i in range(len(data)):
            txt+=data[i]["title"]
            txt+="\n"
        with open('2022-03-'+str(d)+'.txt',"w",encoding="utf-8") as f:
            f.write(txt)