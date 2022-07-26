# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:43:25 2020

@author: steve
"""

# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
# import seaborn
import seaborn as sns 

# %matplotlib inline


# LER A BASE DE DADOS
data_url = 'http://bit.ly/2cLzoxH'
# read data from url as pandas dataframe
gapminder = pd.read_csv(data_url)
print(gapminder.head(3))

df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})

# graficos para qualitativa
df.plot.pie(y='val', figsize=(5, 5))
df.plot.bar(x='lab', y='val', rot=0)
gapminder.plot.bar("country")

# graficos para quantitativas
gapminder.hist("lifeExp")
gapminder.plot("lifeExp",kind = 'hist')
gapminder.plot("lifeExp", "gdpPercap", kind = "scatter")

# FILTRO DE 2007
gapminder_2007 = gapminder[gapminder['year']==2007]
gapminder_2007.shape

# listando os objetos do python
%whos



# FAZER O BOXPLOT
gapminder_2007.boxplot(by='continent', 
                       column=['lifeExp'], 
                       grid=False)

# Make Boxplot with Seaborn
bplot = sns.boxplot(y='lifeExp', x='continent', 
                 data=gapminder_2007, 
                 width=0.5,
                 palette="colorblind")

# Boxplot with data points using Seaborn

# make boxplot with Seaborn
bplot=sns.boxplot(y='lifeExp', x='continent', 
                 data=gapminder_2007, 
                 width=0.5,
                 palette="colorblind")
 
# add stripplot to boxplot with Seaborn
bplot=sns.stripplot(y='lifeExp', x='continent', 
                   data=gapminder_2007, 
                   jitter=True, 
                   marker='o', 
                   alpha=0.5,
                   color='black')

# Adjust x-axis and y-axis label font sizes

bplot.axes.set_title("2007: Life Expectancy Vs Continent",
                    fontsize=16)
 
bplot.set_xlabel("Continent", 
                fontsize=14)
 
bplot.set_ylabel("Life Expectancy",
                fontsize=14)
 
bplot.tick_params(labelsize=10)

#How to Save the Boxplot as jpg file?
# output file name
plot_file_name="boxplot_and_swarmplot_with_seaborn.jpg"
 
# save as jpeg
bplot.figure.savefig(plot_file_name,
                    format='jpeg',
                    dpi=100)



# Python and R Tips
# Catplot Python Seaborn: One Function to Rule All Plots With Categorical Variables
# Catplot is a relatively new addition to Seaborn that simplifies plotting that involves categorical variables. In Seaborn version v0.9.0 that came out in July 2018, changed the older factor plot to catplot to make it more consistent with terminology in pandas and in seaborn.
The new catplot function provides a new framework giving access to several types of plots that show relationship between numerical variable and one or more categorical variables, like boxplot, stripplot and so on. Catplot can handle 8 different plots currently available in Seaborn. catplot function can do all these types of plots and one can specify the type of plot one needs with the kind parameter.
The default kind in catplot() is “strip”, corresponding to stripplot(). 
Here are the list of different type of plots, involving categorical variables
Categorical scatterplots with catplot

    stripplot() – with kind=”strip”
    swarmplot() – with kind=”swarm”

Categorical distribution plots with catplot

    boxplot() – with kind=”box”
    violinplot() – with kind=”violin”
    boxenplot() – with kind=”boxen”

Categorical estimate plots with catplot

    pointplot() – with kind=”point”
    barplot() – with kind=”bar”
    countplot() – with kind=”count”
	
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
	
data_url = 'http://bit.ly/2cLzoxH'
gapminder = pd.read_csv(data_url)
gapminder.head(n=3)

#How To Make Stripplot with jitter using Seaborn catplot?
	
sns.catplot(x='continent', y='lifeExp', 
            data=gapminder,jitter='0.25')
	
sns.catplot(x='continent', y='lifeExp', 
            data=gapminder,
            jitter=False,
            height=4, aspect=1.5)

	
sns.catplot(x='continent', y='lifeExp', 
            data=gapminder,
            kind='box',
            height=4, aspect=1.5)
#How to Make Boxplot with Catplot in Seaborn?
#Seaborn Catplot: Boxplot
#How To Make Boxplot with Original Data points with Seaborn catplot?

#In Seaborn, we can make letter-value plot or boxen plot using kind=’boxen’ argument.
	
sns.catplot(x='continent', y='lifeExp', 
            data=gapminder,height=4,
                aspect=1.5,
           kind='boxen')

sns.catplot(x='continent', y='lifeExp', 
            data=gapminder,
            height=4,aspect=1.5,
            kind='violin')

sns.catplot(x="continent", kind="count", data=gapminder)

# https://stackoverflow.com/questions/53645882/pandas-merging-101
