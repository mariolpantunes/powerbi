## Matplotlib

## Load a python script to have some data
import pandas as pd 
df = pd.DataFrame({ 
    'Name':['Raman','Ramanujam','Chandrasekhar','Sarabhai','Bose','Khorana'], 
    'Age':[82,33,85,52,80,89], 
    'Birthyear': [1888, 1887, 1910, 1919, 1894, 1922], 
    'Deathyear': [1970, 1920, 1995, 1971, 1974, 2011], 
    'Nobel':['Y','N','Y','N','N','Y'], 
    'Field':['Physics','Mathematics','Physics','Space','Physics','Medicine'],
})

## Select name and age
# line chart
import matplotlib.pyplot as plt 
ax = plt.gca() 
dataset.plot(kind='line',x='Name',y='Age',ax=ax) 
plt.show()

# bar plot
import matplotlib.pyplot as plt 
ax = plt.gca() 
dataset.plot(kind='bar',x='Name',y='Age') 
plt.show() 


## Load another dataset
import pandas as pd
df = pd.DataFrame({
'First_name':['Vijay','Eri','Dawn','Abhinav','Alok','Shambhavi','Vipu'],
'Age':[21,34,42,18,24,80,22],
'Weight': [180, 130, 200, 140, 176, 142, 210],
'Gender':['M','F','F','M','M','F','M'],
'State':['Delhi','Oregon','California','Delhi','Banarash','Delhi','Mumbai'],
'Children':[4,1,2,3,10,0,4],
'Pets':[3,2,2,5,0,1,5]})

## Select first_name childern and pets
import matplotlib.pyplot as plt
ax = plt.gca()
dataset.plot(kind='line',x='First_name',y='Children',ax=ax)
dataset.plot(kind='line',x='First_name',y='Pets', color='red', ax=ax)
plt.show()


## Load the Tips dataset

## Select day and total_bill
import matplotlib.pyplot as plt 
import seaborn as sns
sns.violinplot(x='day',y='total_bill',data=dataset)
plt.show()

## Select tip, size and total_bill
import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x='total_bill', y='tip',hue='size', size='size',sizes=(20, 900),data=dataset)
plt.show()

## Select all except smoker
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(dataset,hue='sex')
plt.show()