# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:29:01 2022

@author: Hp
"""

import pandas as pd
imdb = pd.read_csv("https://raw.githubusercontent.com/curso-r/main-r4ds-1/master/dados/imdb.csv")
print(imdb.head)

%whos
dir(imdb)

imdb_simples = imdb.filter(["titulo","ano"])
imdb_simples.assign(coluna_nova=10)
imdb_simples.assign(coluna_nova=imdb_simples.ano>1945,coluna_texto="a")
imdb_simples.ano.sum()
imdb_simples.ano < 1945

imdb_simples.ano
imdb_simples.titulo.str.count("a")
imdb.receita.s



