from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dfPedidos = pd.read_csv('resultados/pedidos.csv', error_bad_lines=False)
dfProductp =pd.read_csv('resultados/productosPedidos.csv',error_bad_lines= False)
dfUsuer =pd.read_csv('resultados/usuarios.csv',error_bad_lines= False)
dfProv = pd.read_csv('resultados/proveedores.csv',error_bad_lines= False)
agrupado = dfProductp.groupby('idProducto').cantidadVendida.sum()

#dfProductp[distancia] = ('idPedido')
dfProductp['ganNet'] = (dfProductp['precioProd']/(dfProductp['costoProd']*dfProductp['cantidadVendida']))-1

vendido = dfProductp.groupby('nombreProducto').cantidadVendida.sum()

agrupadoN = dfProductp.groupby('idProducto').agg(
    nameProduct = ('nombreProducto',lambda x: x.mode().tolist()[0] if len(x.mode().tolist())>0 else np.nan),
    ganNet=('ganNet','mean'),
    cantVend=('cantidadVendida','sum'),
    idProveedor = ('idProveedor',lambda x: x.mode().tolist()[0] if len(x.mode().tolist())>0 else np.nan),
    DTiempo = ('idPedido','mean')
)
dfProductp['cantidadVendida'] = dfProductp.cantidadVendida.astype(int)
agrupadoN = agrupadoN.sort_values(['cantVend','ganNet'],ascending=False)
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
def listas(arreglo):
    val = len(arreglo) 
    for i in range(0,val):
        conteo = arreglo.index.values[i]
        #calificador(agrupadoN['ganNet'],agrupadoN['cantVend'])
        ganNet = arreglo.loc[conteo,'ganNet']
        cantVend = arreglo.loc[conteo,'cantVend']
        califa = calificador(ganNet, cantVend)
        #PropAcierto =
        arreglo.loc[conteo,'aciertoCompra'] = califa
        
def listasBusqueda(arreglo,arreglo2):
    val = len(arreglo) 
    for i in range(0,val):
        conteo = arreglo.index.values[i]
        #calificador(agrupadoN['ganNet'],agrupadoN['cantVend'])
        idProveedor = arreglo.loc[conteo,'idProveedor']
        #print(i," ",idProveedor)
        for j in range(0,len(arreglo2)):
            idProveedor2 = arreglo2.loc[j,'idProve']
            if(idProveedor == idProveedor2 ):
                nombreProv = arreglo2.loc[j,'nombreProv'] 
                arreglo.loc[conteo,'nombreProv'] = nombreProv
            elif(idProveedor == 111 or idProveedor == None ):
                nombreProv = "noFind"
                arreglo.loc[conteo,'nombreProv'] = nombreProv