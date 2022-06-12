import json
import pandas as pd


for d in range(1,13):
    time=[]
    hot=[]
    title=[]
    emo=[]
    count=[]
    cou=[0,0,0,0,0,0,0,0,0,0,0,0]
    time_str=""
    if(d<10):
        with open('./opinion_data/event_json/2022-05-'+'0'+str(d)+'.json','r',encoding='utf-8') as f:
            data=json.load(f)
            for i in range(len(data)):
                title.append(data[i]["news_title"])
                time_str=data[i]["publish_time"][-5:-3]+data[i]["publish_time"][-2:]
                time.append(int(time_str))
                hot.append(data[i]["sim_count"])
                emo.append(data[i]["news_emotion"])
                cou[int(time_str)//200]+=1
                count.append(cou[int(time_str)//200])
        df=pd.DataFrame({'title':title,'time':time,'hot':hot,'emo':emo,'count':count})
        df.to_csv("./opinion_data/event_csv/2022-05-"+'0'+str(d)+".csv",index=False,sep=',')
    else:
        with open('./opinion_data/event_json/2022-05-'+str(d)+'.json','r',encoding='utf-8') as f:
            data=json.load(f)
            for i in range(len(data)):
                title.append(data[i]["news_title"])
                time_str=data[i]["publish_time"][-5:-3]+data[i]["publish_time"][-2:]
                time.append(int(time_str))
                hot.append(data[i]["sim_count"])
                emo.append(data[i]["news_emotion"])
                cou[int(time_str)//200]+=1
                count.append(cou[int(time_str)//200])
        df=pd.DataFrame({'title':title,'time':time,'hot':hot,'emo':emo,'count':count})
        df.to_csv("./opinion_data/event_csv/2022-05-"+str(d)+".csv",index=False,sep=',')