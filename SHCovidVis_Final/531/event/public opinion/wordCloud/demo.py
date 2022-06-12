# coding:utf-8

from os import path
import chnSegment
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

def generate_wordcloud(text,n):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    
    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images//dzjpg.png")))
    font_path=path.join(d,"font//msyh.ttf")
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=2000, # 词云显示的最大词数  
           mask=alice_mask,# 设置背景图片       
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )

    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    if n<10:
        wc.to_file(path.join(d, "Images//2022-05-0"+str(n)+".png"))
    else:
        wc.to_file(path.join(d, "Images//2022-05-"+str(n)+".png"))

if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    for i in range(1,13):
        if i<10:
            text = open(path.join(d, 'doc//2022-05-0'+str(i)+'.txt'),encoding='UTF-8').read()
        else:
            text = open(path.join(d, 'doc//2022-05-'+str(i)+'.txt'),encoding='UTF-8').read()
        text=chnSegment.word_segment(text)
        generate_wordcloud(text,i)
        print(i)
