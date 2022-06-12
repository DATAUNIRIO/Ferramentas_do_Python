# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:33:51 2020

@author: Hp
"""

#%% importando as bibliotecas
# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
# import seaborn
import seaborn as sns
# %matplotlib inline


#%% LER A BASE DE DADOS CARROS
data_url = 'https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/carprice.csv'
# read data from url as pandas dataframe
carros = pd.read_csv(data_url)
print(carros.head(3))

# FILTRO PARA CARRO GRANDE
carro_grande = carros[carros['Type']=='Large']
print(carro_grande.head(3))
carro_grande.shape

#%% LER A BASE DE DADOS EXCEL

data_url2 = 'https://github.com/DATAUNIRIO/Base_de_dados/raw/master/Familias.xls'
Familia = pd.read_excel(data_url2)
print(Familia.head(3))
Familia.dtypes

#%% LER A BASE DE DADOS TITANIC
data_url3 = 'https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/titanic3.csv'
# read data from url as pandas dataframe
df = pd.read_csv(data_url3)
print(df.head(3))
df.dtypes

#%% LER A BASE DE DADOS TITANIC
import pandas_profiling 
pandas_profiling.ProfileReport(df, title="Meu relatorio Pandas")

profile = pandas_profiling.ProfileReport(df, title='Pandas Profiling Report', explorative=True)

profile = df.profile_report(title='Pandas Profiling Report', plot={'histogram': {'bins': 8}})
profile.to_file("meuoutputpandas.html")