# -*- coding: utf-8 -*-
"""Aula 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qybs1dwpoAhaUC8FV0M0YfsZdOum9s-m
"""

# Revisão

# Funcional X OOB

# Funcional:

# meus_dados <- ler_dados("caminho")
# modelo_estatistico <- constroi_modelo(meus_dados)

# No R...

# objeto_do_tipo_texto = "Fernando"

# stringr::str_count(objeto_do_tipo_texto, "n")

# OOB:

objeto_do_tipo_texto = "Fernando"

objeto_do_tipo_texto.count("n")

# Pacote/Lib Pandas

import pandas as pd

#%whos

objeto_do_tipo_texto.upper()

imdb = pd.read_csv("https://raw.githubusercontent.com/curso-r/main-r4ds-1/master/dados/imdb.csv")

# cada tipo tem seus próprios métodos...

# int, str, float por exemplo
inteiro = 1
texto = "a"
quebrado = 1.2

# como que faz "sacolas" de objetos, que no caso aqui se chamam listas:

lista = [inteiro, texto, quebrado]

#lista + [1,2,3]

# lista não ser pra ser coluna, array é usado:

import numpy as np

coluna = np.array([1,2,3])

coluna + 1

# Pandas

imdb

imdb.describe()

imdb.info()

(imdb
 .query("ano <= 1945")
 # selecionar linhas
 .sort_values(["orcamento"])
 # orderar as linhas da tabela por algum critério 
 .filter(["titulo", "orcamento"]))
 # selecionar colunas

imdb

# Outras funcionalidades do filter

colunas = imdb.columns

imdb.drop(["titulo"], axis = 1)

# (1) ordernar: sort_values 
# (2) selecionar coluna: filter
# (3) selecionar linha: query
# (4) criar colunas: assign

imdb_simples = imdb.filter(["titulo", "ano"])

imdb_simples.assign(
    coluna_nova = imdb_simples.filter(['ano']) < 1945,
    # não é muito recomendado fazer isso ^
    coluna_nova = imdb_simples.ano < 1945,
    # esse é o jeito elgal de criar essa coluna ^
    coluna_texto = imdb_simples.ano-1900)

# atributo: o que um objeto tem ou é. características
# instancia: quando um objeto pertence a uma classe específica, a gente fala que 
# ele é uma instancia dessa classe

#imdb_simples.ano

#imdb_simples.filter(['ano']) < 1945
#imdb_simples.ano < 1945

# perguntas....

# consigo usar uma coluna que acabei de criar???

imdb_com_lucro = imdb.assign(
    lucro = imdb.receita-imdb.orcamento
)

# será que o código abaixo funciona???
#imdb.assign(
#    lucro = imdb.receita-imdb.orcamento,
#    categoria_lucrou = imdb.lucro > 0
#)
# NÃO

imdb_com_lucro.assign(
  categoria_lucrou = imdb_com_lucro.lucro > 0
)

# outra opção

(imdb.assign(
    lucro = lambda x: x.receita-x.orcamento,
    # essa linha é igual a trocar o x. por imdb. e tirar o "lambda x"
    # x. vira imdb., então:  x.receita-x.orcamento vira imdb.receita-imdb.orcamento
    categoria_lucrou = lambda x: x.lucro > 0,
    duracao = imdb.duracao/60
).
 filter(["titulo","ano", "lucro", "duracao", "categoria_lucrou"]))

# tem a mesma filosofia da sintaxe do mutate:
# imdb |>
# mutate(
#   lucro = receita-orcamento,
#   categoria_lucrou = lucro > 0    
#)

# (1) filter do pandas é analogo ao select do dplyr
# (2) assign do pandas é analogo ao mutate do dplyr
# (3) query do pandas é analogo ao filter do dplyr
# (4) sort_values do pandas é analogo ao arrange do dplyr

# qual é o limite do query?

# meu problema é manter todas as linhas que contenham a palavra "amor"

# posso fazer:
(imdb
 .assign(
     e_na = imdb.receita.isna(),
     tem_love = imdb.titulo.str.contains("love"),
     tem_a = imdb.titulo.str.contains("a")
     # esse é um jeito de você acessar métodos mais "básicos" de um objeto
     )
 .query("tem_a | e_na"))

# &
# |
# <= >= < >
# ==
# ~

(imdb
  .assign(
      filme_de_drama = imdb.generos.str.contains("Drama"),
      titulo_em_minuscula = imdb.titulo.str.lower(),
      titulo_em_maiscula = lambda x: x.titulo.str.upper(),
      numero_de_woman = lambda x: x.descricao.str.count("woman")
  )
  .query("filme_de_drama")
  .sort_values("numero_de_woman",  ascending = False)
  .filter(["titulo", "numero_de_woman"]))

# como saber a "dimensão" de um objeto

len(imdb)
# me diz em quantos "pedaços" eu posso quebrar

imdb.shape

# agregação...

# como eu posso fazer pra pegar uma tabela (grande possivelmente) e 
# extrair uns resumos. qual é o summarise do pandas

sumarios = (imdb
 .filter(like = "num")
 .agg(["mean", "count"]))

sumarios

from re import I
# quero que o meu sumário tenha nomes customizados
# mais do que isso quero uma sintaxe no agg
# bem parecida com o summarise do dplyr

# pra isso vamos usar um dicionário:
# dicionario

# as vezes queremos conjuntos que além da posição,
# podem ser identificados pelos nomes

meu_dicionario = {"nome1" : "valor1", "nome2" : "valor2"}

#agg_com_dict = (imdb
# .agg({
#   "duracao":["mean", "count"],
#   "receita": "mean"   
# })
#)

# mas ainda não cheguei aonde eu queria...
# aqui eu só falei pra quais nomes colunas eu queria
# que fosse aplicado cada sumarização

#minha_tupla = (1, 2)

#(imdb.
#  agg(
#     duracao_media = ("duracao", "mean"),
#     desv_pad_duracao = ("duracao", "std"),
#     receita_media = ("receita", "mean")
#  )
#)

# e se eu quisesse fazer a média do log de uma variável???

def minha_media(coluna):
    aux = coluna.mean()

    return aux

resultado = minha_media(imdb.receita)

print(resultado)

objeto = (imdb
 .assign(
     log_receita = np.log(imdb.receita)
 )
 .agg(
     media_log_receita = ("receita", "mean")
 )
)

# ON HOLD

imdb.columns

(imdb
 .groupby(["ano", "pais"])
 .agg(
    duracao_media = ("duracao", "mean"),
    receita_mediana = ("receita", "median") 
 ))

data_frame_original = imdb

type(data_frame_original)

data_frame_agrupado = imdb.groupby("ano")

type(data_frame_agrupado)

nota_media_ano = (imdb
                  .groupby("ano")
                  .agg({"nota_imdb" :  "mean",
                        "titulo": "count"})
    
)

(imdb
 .groupby("ano")
 .agg(
     nota_media = ("nota_imdb", "mean"),
     numero_de_filmes = ("titulo", "count"),
     numero_de_descricoes = ("id_filme", "count")
  )
)

# (1) selecionar linha com o query
# o query vai dificultar quando eu quiser
# aplicar uma função ou tratamento direto na filtragem...
# (2) selecionar coluna com o filter
# (3) criar colunas com o assign
# (4) ordenar as linhas com o sort_values
# (5) sumarizar, com ou sem grupos, usando o agg (e suas notações) + groupby 
# pra fazer sumarizacoes customizadas ou você cria uma coluna por fora
# ou voce cria sua propria função