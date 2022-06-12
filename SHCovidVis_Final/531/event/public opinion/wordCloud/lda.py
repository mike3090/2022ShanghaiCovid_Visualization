import os
from os import path
from gensim.models import LdaModel,TfidfModel,LsiModel
from gensim import similarities
from gensim import corpora
import jieba;
jieba.load_userdict(path.join(path.dirname(__file__),'userdict//userdict.txt')) # 导入用户自定义词典

def stopwordslist():
    stopwords=[line.strip() for line in open('doc//hit_stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords

def create_data(corpus_path):#构建数据，先后使用doc2bow和tfidf model对文本进行向量表示
    sentences = []
    sentence_dict={}
    count=0
    stopwords=stopwordslist()
    for line in open(corpus_path,encoding='utf-8'):
        str=""
        jieba_word=jieba.cut(line,cut_all=False)
        for word in jieba_word:
            if word not in stopwords:
                str+=word+" "
        str = str.strip().split('\t')
        sentence_dict[count]=str[0]
        count+=1
        sentences.append(str[0].split(' '))
    #对文本进行处理，得到文本集合中的词表
    dictionary = corpora.Dictionary(sentences)
    #利用词表，对文本进行cbow表示
    corpus = [dictionary.doc2bow(text) for text in sentences]
    #利用cbow，对文本进行tfidf表示
    tfidf=TfidfModel(corpus)
    corpus_tfidf=tfidf[corpus]
    return sentence_dict,dictionary,corpus,corpus_tfidf

def lda_model(sentence_dict,dictionary,corpus,corpus_tfidf,cluster_keyword_lda):#使用lda模型，获取主题分布   
    lda = LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=10)
    f_keyword = open(cluster_keyword_lda, 'w+')
    for topic in lda.print_topics(10,53):
        words=[]
        print(topic)
        for word in topic[1].split('+'):
            word=word.split('*')[1].replace(' ','')
            words.append(word)
        f_keyword.write(str(topic[0])+'\t'+','.join(words)+'\n')
    #利用lsi模型，对文本进行向量表示，这相当于与tfidf文档向量表示进行了降维，维度大小是设定的主题数目  
    corpus_lda = lda[corpus_tfidf]
    for doc in corpus_lda:
        print (len(doc),doc)
    return lda

def lsi_model(sentence_dict,dictionary,corpus,corpus_tfidf,cluster_keyword_lsi):#使用lsi模型，获取主题分布
    lsi = LsiModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=11)
    f_keyword = open(cluster_keyword_lsi, 'w+')
    for topic in lsi.print_topics(11,50):
        print (topic[0])
        words=[]
        for word in topic[1].split('+'):
            word=word.split('*')[1].replace(' ','')
            words.append(word)
        f_keyword.write(str(topic[0])+'\t'+','.join(words)+'\n')
   
    return lsi


if __name__=="__main__":
    corpus_path = "doc//2022-03-01.txt"
    cluster_keyword_lda = './cluster_keywords_lda.txt'
    cluster_keyword_lsi = './cluster_keywords_lsi.txt'
    sentence_dict,dictionary,corpus,corpus_tfidf=create_data(corpus_path)
    lda_model(sentence_dict, dictionary, corpus, corpus_tfidf,cluster_keyword_lda)