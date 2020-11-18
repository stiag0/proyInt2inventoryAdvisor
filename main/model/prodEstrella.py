from os import listdir
from os.path import isfile, join
import glob
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, confusion_matrix
import sklearn as skl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import json

def metricasD( X_train, X_test, y_train, y_test,clf):
  #  features_train, labels_train, features_test, labels_test = makeTerrainData()
    # return X_train, y_train, X_test, y_test

    y_train_true = y_train
    y_train_pred = clf.predict(X_train.values.reshape(-1,1))

    y_test_true = y_test
    y_test_pred = clf.predict(X_test.values.reshape(-1,1))

    print('Accuracy')
    print('TRAIN: {:.2f}, TEST: {:.2f}'.format(accuracy_score(y_train_true, y_train_pred.round()), accuracy_score(y_test_true, y_test_pred.round())))

    print('Precision')
    print('TRAIN: {:.2f}, TEST: {:.2f}'.format(precision_score(y_train_true, y_train_pred.round(),average = 'weighted'), precision_score(y_test_true, y_test_pred.round(),average = 'weighted')))

    print('Recall')
    print('TRAIN: {:.2f}, TEST: {:.2f}'.format(recall_score(y_train_true, y_train_pred.round(),average = 'weighted'), recall_score(y_test_true, y_test_pred.round(),average = 'weighted')))

    print('F1-SCORE') 
    train = f1_score(y_train_true, y_train_pred.round(),average = 'weighted')
    test =  f1_score(y_test_true, y_test_pred.round(),average = 'weighted')
    print('TRAIN: {:.4f}, TEST: {:.4f}'.format(f1_score(y_train_true, y_train_pred.round(),average = 'weighted'), f1_score(y_test_true, y_test_pred.round(),average = 'weighted')))
    return  train, test;

def predictor(dataset,colY):
    idProductos = dataset.idProducto.unique()
    #nombreProducto = dataset.nombreProducto.loc[,]
    predNextSell = []
    for i in range(0,len(idProductos)):
        idProducto = idProductos[i]        
        df = dataset[dataset['idProducto'] == idProducto]
        df = df.reset_index(drop = True)
        nombreProducto = df.loc[0,'nombreProducto']
        cantidadVend = df.cantidadVendida.sum()
        if (cantidadVend > 30):
            arrX = df.idPedido
            arraY = df[colY] 
            X_train, X_test, y_train, y_test = train_test_split(arrX, arraY)
            
            #creando modelo lineal
            LR = LinearRegression()
            LR.fit(X_train.values.reshape(-1,1), y_train.values)
            
            #use model to predict on TEST data
            prediction = LR.predict(X_test.values.reshape(-1,1))
            
            train, test = metricasD( X_train, X_test, y_train, y_test,LR)
            
            if(train < 0.85 or test < 0.85 ):
                print("regresion lineal no suficinete paso a random forest")
                #try random forest 
                regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
                regressor.fit(arrX.values.reshape(-1,1), arraY)
                dato_pred = regressor.predict([[1602824759775]])[0]
                print (dato_pred)
            else:
                plt.figure(figsize=(9,6))

                dato_pred = LR.predict(np.array([[1602824759775]]))[0]
                print(dato_pred)
                
                plt.plot(X_test, prediction, label = 'linear Regresion', color = 'b')
                plt.scatter(X_test, y_test, label = 'test Data', color = 'g', alpha = 0.6)
                plt.legend()
                plt.title("%s "%nombreProducto) 
                plt.show()
                        
            predNextSell.append(dato_pred)  
    print(predNextSell)  