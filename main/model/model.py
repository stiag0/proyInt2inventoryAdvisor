from os import listdir
from os.path import isfile, join
import glob
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, confusion_matrix
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier

import sklearn as skl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import json

dfProductp.to_csv('../../dataSet/productosPedidos.csv')

#       modelo integrador

# hidden_layer_sizes=(n,m),
mlp = MLPClassifier(max_iter=1000, activation='relu')
mlp


#X = dfProductp['prodEstrella']
X = dfProductp['idPedido']
Y = dfProductp['Kmeans']
X_train, X_test, y_train, y_test = train_test_split(X,Y)
mlp.fit(X_train.values.reshape(-1,1), y_train)

pred = mlp.predict(X_test.values.reshape(-1,1))
pred