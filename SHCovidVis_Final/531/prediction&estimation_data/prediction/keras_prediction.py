# Predict the spread of pandemic using LSTM

from urllib import response
import flask_cors 
import flask
import json
import os
from select import select
import pandas as pd
import keras.models as models
import keras.layers as layers
import keras.callbacks as callbacks
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler


## FOR THE HTTP-CORS ERROR
app = flask.Flask(__name__)
flask_cors.CORS(app)
## load the file

def load_data(district = 'Shanghai', selector = 2) -> list:
    '''
    district: string, the form should be like 'Jinshan', 'Shanghai' or 'PudongNew'
    selector: 2 for the total nuber; 1 for Asymptomatic cases; 0 for confirmed cases.
    '''
    #os.chdir(os.path.abspath(__file__))
    current_path = os.path.dirname(os.path.abspath(__file__))
    data = pd.read_csv(current_path + '/../district_data/city_dist_unmerged_date.csv', usecols=[district])
    stats = data.values
    name = data.columns[0]
    size = stats.size
    stats_p = []
    if selector == 1:
        for j in range(size):
            if (j % 2) == 0: 
                stats_p.append(int(stats[j]))
    elif selector == 0:
        for j in range(size):
            if (j % 2) == 1: 
                stats_p.append(int(stats[j]))
    else:
        for j in range(size):
            if j % 2 == 0:
                stats_p.append(int(stats[j]))
            else:
                stats_p[-1] += int(stats[j])
    data_infecious = np.array(stats_p, dtype='uint32')
    print(data_infecious)
    return [name, data_infecious]

## 滑动窗口
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back):
        a = dataset[i:(i+look_back)]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
    return np.array(dataX), np.array(dataY)

## Build the model

def LSTM_train(f_look_back):
    model = models.Sequential()
    model.add(layers.LSTM(25, input_shape=(1, f_look_back)))
    model.add(layers.Dense(1))
    model.compile(loss="mean_squared_error", optimizer='adam')
    return model

#print(dataset_sc)
#print("Current district:", load[0])

'''
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ
'''

@app.route('/keras_prediction', methods=['POST'])
#@flask_cors.cross_origin()
def main():
    dist = flask.request.get_data()
    dist = json.loads(dist)
    #print(dist)
    load = load_data(dist['district'])
    dataset = load[1]
    #dataset = [dataset]
    #plt.plot(dataset) 
    #plt.show()

    dataset_sc = dataset.reshape(-1, 1) 
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset_sc = scaler.fit_transform(dataset_sc)
    dataset_normalised =[]
    for i in dataset_sc:
        dataset_normalised.append(i[0])
    
    train = dataset_normalised
    look_back = 7
    trainX, trainY = create_dataset(train, look_back)

    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))

    model = LSTM_train(look_back)
    reduce_lr = callbacks.ReduceLROnPlateau(monitor='val_loss', patience=10, mode='max')
    model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2, callbacks=[reduce_lr])
    trainPredict = model.predict(trainX)

    testx = [0.]*(7+look_back)
    testx[0:look_back] = train[-look_back:]
    testx = np.array(testx)
    testPredict = [0]*7
    for i in range(7):
        testxx = testx[-look_back:]
        testxx = np.reshape(testxx, (1, 1, look_back))
        testy = model.predict(testxx)
        testx[look_back+i] = testy
        testPredict[i] = testy

    testPredict = np.array(testPredict)
    testPredict = np.reshape(testPredict,(7,1))

    ## INVERSE
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)

    ## VISUALIZATION
    
    trainPredictPlot = np.reshape(np.array([None]*(len(dataset)+7)),((len(dataset)+7),1))
    trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

    testPredictPlot = np.reshape(np.array([None]*(len(dataset)+7)),((len(dataset)+7),1))
    testPredictPlot[:, :] = None
    testPredictPlot[len(dataset):(len(dataset)+7), :] = testPredict
    '''
    plt.plot(load[1],label='true')
    plt.plot(trainPredictPlot,label='trainpredict')
    plt.plot(testPredictPlot,label='testpredict')
    plt.legend()
    plt.show()
    '''

    info = []
    trainPredictList = []
    testPredictList = []
    for i in trainPredictPlot:
        if i[0] == None:
            trainPredictList.append(0)
        else:
            trainPredictList.append(i[0])
    for i in testPredictPlot:
        if i[0] == None:
            testPredictList.append(0)
        else:
            testPredictList.append(i[0])
    dataset = dataset.tolist()
    for i in range(look_back):
        dataset.append(0)

    days = [i for i in range(len(trainPredictList))]
    for i in range(len(days)):
        info.append(dict())
        info[-1]['date'] = days[i]
        info[-1]['data_origin'] = dataset[i]
        info[-1]['train_predict'] = trainPredictList[i]
        info[-1]['test_predict'] = testPredictList[i]
    
    response = flask.make_response(flask.jsonify(info))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    return response

if __name__ == '__main__':
    flask_cors.CORS(app, supports_credentials=True) 
    app.run(port = '8800')