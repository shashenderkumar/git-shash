#!/usr/bin/env python
# coding: utf-8

# In[5]:


print('Lets make better world...')


# In[ ]:





# In[14]:


## LIST

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print(list2[2])
print ("list1[0]:", list1[1:4])
print ("list1[-1]:", list1[1:])
print ("list2[1:5]: ", list2[1:5])
list1[0]=500
print(list1)


# In[15]:


list1.append('added')
print (list1[0:])


# In[19]:


## TUPLES

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
tup1[0]=500
print(tup1)


# In[21]:


## DICTIONARY

dict = {'NAme': 'Zara', 'Age': 7, 'Class': 'First','Class': 'second'}
print ("dict['Name']: ", dict['NAme'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Age']: ", dict['Class'])


# In[9]:


#print(dict['Zara'])


# In[24]:


var = 100
if ( var != 100 ) :
    print ("Value of expression is 100")
    print ("Welcome to ML world")
else:
    print('In else')


# In[11]:


## VARIABLES

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)


# In[12]:


mystring = 'hello'
print(mystring)
mystring = "he'llo"
print(mystring)


# In[13]:


a, b = 3,4.5
print(a,b)


# In[14]:


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


# In[28]:


for k , v in dict.items():
    #print(k)
    print(v)


# In[15]:


var = 100
if ( var == 100 ) : 
    print ("Value of expression is 100")


# In[89]:


import pandas as pd

# Read the data from file
# file is as same locaton where python file is
data = pd.read_csv("house.csv")


# In[90]:


data.head(10)


# In[91]:


# Information about data structure
data.info()


# In[19]:


# Print out country column as Pandas Series
print(data['Square_Feet'])

# Print out country column as Pandas DataFrame
print(data[['Square_Feet']])

# Print out DataFrame with country and drives_right columns
print(data[['Square_Feet', 'Price']])


# In[20]:


# Top 10 rows
data.head(2)


# In[ ]:





# # Heaeding
# and here goes the text

# In[21]:


data.describe()


# In[22]:


import numpy as np
import pandas as pd
#Create a DataFrame
d = {
    'Name':['Alisa','Bobby','jodha','jack','raghu','Cathrine',
            'Alisa','Bobby','kumar','Alisa','Alex','Cathrine'],
    'Age':[26,24,23,22,23,24,26,24,22,23,24,24],
      
       'Score':[85,63,55,74,31,77,85,63,42,62,89,77]}
 
df = pd.DataFrame(d,columns=['Name','Age','Score'])
df


# In[23]:


df[df.Score > 70].index


# In[24]:


df.drop(df[df.Score > 70].index,inplace=True)
df


# # Charts - Distribution

# In[25]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


sns.distplot(data.Price)


# # Charts - Boxplot

# In[27]:


sns.boxplot(data.Price)


# In[28]:


sns.scatterplot(data=data)


# In[29]:


g = sns.PairGrid(data)
g = g.map(plt.scatter)


# In[30]:


g = sns.PairGrid(data)
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)


# In[31]:



# read data from url as pandas dataframe
gapminder = pd.read_csv('gapminder-FiveYearData.txt')


# In[32]:


gapminder.head()


# In[33]:


#To select rows whose column value is in list 
years = [1952, 2007]
gapminder.year.isin(years)


# In[34]:


print(gapminder.year.isin(years).index)


# In[35]:


# selecting value which are not in list
continents = ['Asia','Africa', 'Americas', 'Europe']
gapminder_Ocean = gapminder[~gapminder.continent.isin(continents)]
gapminder_Ocean.shape 


# In[36]:


# Multiple conditions
country_filter = gapminder.continent.isin(continents)
year_filter = gapminder.year.isin(years)

gapminder[ ~country_filter & year_filter ]
           


# In[37]:


gapminder[ country_filter | ~year_filter ]


# In[38]:


continents = ['Asia','Africa', 'Americas', 'Europe']
gapminder_Ocean = gapminder[~gapminder.continent.isin(continents)]
gapminder_Ocean.shape 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn import preprocessing
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


# In[51]:


train = pd.read_csv("bank-full.csv",delimiter=';')


# In[52]:


train.head()


# In[53]:


sns.countplot(y="job", data=train)
#plt.show()


# In[54]:


# Combine similar jobs into categiroes
train['job'] = train['job'].replace(['management', 'admin.'], 'admin/manag')
train['job'] = train['job'].replace(['services','housemaid'], 'home/service')
train['job'] = train['job'].replace(['retired', 'student', 'unemployed', 'unknown'], 'unemployed')


# In[60]:


sns.distplot(train.balance)


# In[61]:


sns.boxplot(train.balance)


# In[57]:


sns.scatterplot(x="age", y="balance", data=train)


# In[59]:


sns.scatterplot(x="age", y="balance",hue="marital" ,data=train)


# In[55]:


import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")


# In[45]:


ax = sns.scatterplot(x="age", y="balance", data=tips)


# In[46]:


ax = sns.scatterplot(x="total_bill", y="tip", hue="time",data=tips)


# In[50]:


sns.distplot(gapminder.lifeExp)


# In[67]:


#sns.heatmap(train.corr(),annot=True)


# In[68]:


#f, ax = plt.subplots(figsize=(9, 6))


# In[74]:


f, ax = plt.subplots(figsize=(14, 8))
sns.heatmap(train.corr(),annot=True,ax=ax,linewidths=.2)


# In[70]:


plt.show()


# In[ ]:




