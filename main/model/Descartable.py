from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import json

dfPedidos = pd.read_csv('resultados/pedidos.csv', error_bad_lines=False)
dfProductp =pd.read_csv('resultados/productosPedidos.csv',error_bad_lines= False)
dfUsuer =pd.read_csv('resultados/usuarios.csv',error_bad_lines= False)
dfProv = pd.read_csv('resultados/proveedores.csv',error_bad_lines= False)

def splitByCos(dataset,colY):
    idProductos = dataset.idProducto.unique()

    for i in range(0,len(idProductos)):
        idProducto = idProductos[i]        
        df = dataset[dataset['idProducto'] == idProducto]
        df = df.reset_index(drop = True)
        #conteo = df.index.values[i]
        nombreProducto = df.loc[0,'nombreProducto']

        cantidadVend = df.cantidadVendida.mean()
        if (cantidadVend > 5):
            
            arrX = df.idPedido
            arraY = df[colY] 
            X_train, X_test, y_train, y_test = train_test_split(arrX, arraY)
            
            #creando modelo lineal
            LR = LinearRegression()
            LR.fit(X_train.values.reshape(-1,1), y_train.values)
            
            #use model to predict on TEST data
            prediction = LR.predict(X_test.values.reshape(-1,1))
            
            
            plt.figure(figsize=(9,6))
            #plt.scatter(X_train, y_train, label = 'training Data', color = 'black', alpha = 0.5)
            #plt.scatter(X_test, y_test, label = 'test Data', color = 'g',alpha = 0.5 )
            # Error Cuadrado Medio
            print("Mean squared error: %.2f" % mean_squared_error(y_train, y_test))
            # Puntaje de Varianza. El mejor puntaje es un 1.0
            print('Variance score: %.2f' % r2_score(y_train, y_test))
            
            #plot prediction line against actual test data
            plt.plot(X_test, prediction, label = 'linear Regresion', color = 'b')
            plt.scatter(X_test, y_test, label = 'test Data', color = 'g', alpha = 0.6)
            plt.legend()
            plt.title("%s "%nombreProducto)
            plt.show()
            
splitByCos(dfProductp,"cantidadVendida")