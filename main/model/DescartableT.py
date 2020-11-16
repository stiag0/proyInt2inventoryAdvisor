def splitByProv(dataset,colY):
    idProvs = dataset.idProveedor.unique()
    #nombreProducto = dataset.nombreProducto.loc[,]
    for i in range(0,len(idProvs)):
        idProv = idProvs[i]          
        df = dataset[dataset['idProveedor'] == idProv]
        df = df.reset_index(drop = True)
        #conteo = df.index.values[i]
        nombreProducto = df.loc[0,'nombreProducto']
        idProve = df.loc[0,'idProveedor']
        #print("nombre %s" % nombreProducto)
        #df.to_csv('resultados/discriminados/%s.csv' % idProducto)
        ganNet = df.ganNet.mean()
        #cantidadVend = df.cantidadVendida.mean()
        if (ganNet > 0.8):
            #print ("largo ", nombreProducto)
            arrX = df.idPedido
            arraY = df["costoProd"] 
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
            plt.title("%s "%idProve)
            plt.show()