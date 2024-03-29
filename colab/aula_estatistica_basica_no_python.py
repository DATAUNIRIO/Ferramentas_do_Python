# -*- coding: utf-8 -*-
"""aula_estatistica_basica_no_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/DATAUNIRIO/14ec7fe40d8cf8206b440cdc5c92f895/aula_estatistica_basica_no_r.ipynb
"""

import pandas as pd
import numpy as np
 
QE = pd.read_csv("https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/QE.csv")

carro = pd.read_csv("https://raw.githubusercontent.com/DATAUNIRIO/Base_de_dados/master/Cars93.csv")

# Commented out IPython magic to ensure Python compatibility.
# listar os objetos
# %whos

# diferenças de listas e arrays
# listas
minha_lista = [1,2,3]
minha_lista2 = [4,5,6]
minha_lista + minha_lista2

# diferenças de listas e arrays
# array
vetor1 = np.array([1,2,3])
vetor2 = np.array([3,4,5])
#vetor + 1
vetor1+vetor2

# as 3 primeiras linhas do banco de dados
print(carro.head(3))

carro.info()

"""## VARIÁVEL QUALITATIVA
Vamos fazer:
1. tabela em números absolutos
2. proporções
3. gráfico de pizza
4. gráfico de barras
"""

#fazendo tabelas
tabela_simples = carro.Type.value_counts()
tabela_simples

#fazendo proporções
#tabela_simples/tabela_simples.sum()*100

round(tabela_simples/tabela_simples.sum()*100,2)

# grafico de pizza
tabela_simples.plot.pie()

# grafico de barras
#tabela_simples.plot.bar()
#tabela_simples.plot.bar(color="red")
tabela_simples.plot.bar(color=["red","blue"])

"""# VARIÁVEL QUANTITATIVA
Vamos fazer: 
*   Resumos
*   Histograma


"""

# O ponto (".") pode ser o $ ou ::
# aqui vou usar como $ para selecionar variáveis
carro.Price.describe()

carro.Horsepower.describe()

# histograma
#carro.Price.plot.hist()
carro.Price.plot.hist(color="red")

"""# DUAS VARIÁVEIS QUALITATIVAS
Vamos fazer: 
*   Tabela para duas variáveis (crosstab)
*   barplot para duas variáveis
"""

#tabela = pd.crosstab(carro.Type, carro.AirBags)
tabela = pd.crosstab(carro.Type, carro.AirBags, rownames=['Tipo de Carro'], colnames=['Tipo de AirBag'])
tabela

# soma da coluna (100 na coluna)
round(tabela/tabela.sum()*100,2)

# abordagem melhor: use o normalise
# normalise por total (all), linhas (index), ou colunas (columns).
tabela_linha = pd.crosstab(carro.Type, carro.AirBags, rownames=['Tipo de Carro'], colnames=['Tipo de AirBag'], normalize='index')
tabela_linha

# normalise por colunas (columns).
tabela_coluna = pd.crosstab(carro.Type, carro.AirBags, rownames=['Tipo de Carro'], colnames=['Tipo de AirBag'], normalize='columns')
round(tabela_coluna*100,2)

tabela.plot.bar()

"""# Uma variável qualitativa e uma variável quantitativa
Vamos fazer:
1. Resumo por grupos
2. Boxplot

"""

# parecido com o pipe
#(carro
# .groupby(["Type", "AirBags"])
# .agg(
#    preco_medio = ("Price", "mean"),
#    preco_mediano = ("Price", "median") 
# ))

carro.groupby("Type").agg(preco_medio = ("Price", "mean"),preco_mediano = ("Price", "median"))

carro.groupby("Type").agg(minimo= ("Price","min"),preco_medio = ("Price", "mean"),maximo = ("Price", "max"))

carro.groupby("Type").agg(preco_medio = ("Price", "mean"),desvio_padrao = ("Price", "std"))

carro.boxplot("Price",by='Type',color="red")

"""# DUAS VARIÁVEIS QUANTITATIVAS
1. Diagrama de dispersão
2. Coeficiente de correlação
"""

# Draw a scatter plot
carro.plot.scatter(x = 'Price', y = 'Horsepower', s = 100);

# Draw a scatter plot and here size of dots determined by price
carro.plot.scatter(x = 'Price', y = 'Horsepower', s = 'Price', c = 'red')

# The Pandas Plot Function
#df.plot(
#    x=None,         # Values to use for x axis
#    y=None,         # Values to use for y axis
#    kind='line',    # The type of chart to make
#    title=None,     # The title to use
#    legend=False,   # Whether to show a legend
#    xlabel=None,    # What the x-axis label should be
#    ylabel=None     # What the y-axis label should be
#    c=None,         # The color to use for the dots
#    s=None          # How to size dots (single number or column)
#)

carro.plot.scatter(x = 'Price', y = 'Horsepower', s = 'Price', c = 'red',title="meu gráfico",xlabel="preço do carro",ylabel="HP")

carro.filter(["Price", "Horsepower"]).corr()

carro.corr()

carro.filter(["Price", "Horsepower"]).corr(method='spearman')

# Commented out IPython magic to ensure Python compatibility.
# plot the heatmap
import seaborn as sns
# %matplotlib inline

correlacao = carro.corr() 
sns.heatmap(correlacao)

sns.heatmap(correlacao, cmap="Blues", annot=True)

# posso fazer:
(carro.assign(
     tem_na = carro.Price.isna(),
     tem_audi = carro.Manufacturer.str.contains("Audi")
     # esse é um jeito de você acessar métodos mais "básicos" de um objeto
     ))

# (1) selecionar linha com o query
# (2) selecionar coluna com o filter
# (3) criar colunas com o assign

carro.query("Type=='Small'").Manufacturer

#carro.query("Type !='Small'").Manufacturer

# carro.query("Type == 'Small' | Type == 'Midsize'")

carro.query("Type in ('Small','Midsize')")

carro.columns

len(carro)