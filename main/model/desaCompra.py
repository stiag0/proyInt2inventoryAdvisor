from os import listdir
from os.path import isfile, join
import glob
from sklearn import metrics
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

dfProductp = pd.read_csv('../dataSet/productosPedidos.csv',error_bad_lines= False)


def calificador(Gnet, cantVenta):
    #print(Gnet,cantVenta)
    if (Gnet > 0.8 and cantVenta > 100):
        #print("producto ideal")
        return 0.5
    elif (Gnet > 0.8 and cantVenta > 30):
        #print("desacierto + publicidad")
        return 0.3
    elif (Gnet > 0.8 and cantVenta <=30):
        #print ("precio irreal")
        return 0.1 
    elif ( Gnet > 0.3 and cantVenta > 100):
        #print("bajar mejorar costo")
        return 0.4
    elif (Gnet > 0.3 and cantVenta > 30 ):
        #print(promedio)
        return 0.2
    elif (Gnet <= 0.3 and cantVenta > 30):
        #print("bajar mejorar costo")
        return 0.7    
    else:
        return 0

def agrupador(dfProductp):
    iris = dfProductp
    x = pd.DataFrame(iris, columns = ['cantidadVendida','ganNet'])

    Nc = range(1,10)
    kmeans = [KMeans(n_clusters=i) for i in Nc]
    kmeans
    score = [kmeans[i].fit(x).score(x) for i in range(len(kmeans))]
    score
    iris = dfProductp

    model = KMeans(n_clusters = 6, max_iter = 1000)
    model.fit(x)
    y_labels = model.labels_
    y_kmeans = model.predict(x)
    accuracy = metrics.adjusted_rand_score(iris.cantidadVendida,y_kmeans)
    print(accuracy)
    plt.scatter(x['ganNet'],x['cantidadVendida'], c= y_kmeans, s= 30)
    plt.xlabel('ganancia neta')
    plt.ylabel('cantidad vendida')

