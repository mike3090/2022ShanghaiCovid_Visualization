# -*- coding: utf-8 -*-

import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


class TopicKeywords:
    """
    主题发现
    """
    def __init__(self, train_data, n_components=10, n_top_words=50, max_iter=50):
        """
        :param train_data: 训练数据
                      格式：   ["张三在中国移动工作", "你是谁？"]
        :param n_components:  主题数目
        :param n_top_words:  每个主题提取的主题词数目
        :param max_iter:  迭代次数
        """
        self.train_data = [" ".join(jieba.lcut(data)) for data in train_data]
        self.n_components = n_components
        self.n_top_words = n_top_words
        self.max_iter = max_iter

    def print_top_words(self, model, feature_names, n_top_words):
        ret = {}
        for topic_idx, topic in enumerate(model.components_):
            key = "topic_{}".format(topic_idx)
            val = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
            ret[key] = val
        return ret

    def analysis(self):
        tf_vectorizer = CountVectorizer()
        tf_idf_vectorizer = TfidfVectorizer()
        tf = tf_idf_vectorizer.fit_transform(self.train_data)
        lda = LatentDirichletAllocation(n_components=self.n_components, max_iter=self.max_iter,
                                        learning_method='online',
                                        learning_offset=50.,
                                        random_state=0)
        lda.fit(tf)
        tf_feature_names = tf_idf_vectorizer.get_feature_names()
        x=tf.toarray()
        return self.predict_to_data_frame(lda,x),self.print_top_words(lda, tf_feature_names, self.n_top_words)

    def predict_to_data_frame(self,model: LatentDirichletAllocation, X: np.ndarray) -> pd.DataFrame:
        matrix = model.transform(X)
        columns = [f'P(topic {i+1})' for i in range(len(model.components_))]
        df = pd.DataFrame(matrix, columns=columns)
        return df
