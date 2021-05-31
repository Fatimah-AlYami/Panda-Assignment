#!/usr/bin/env python
# coding: utf-8

# ##### Done by Fatimah AlYami

# In[1]:


import pandas as pd


# In[112]:


#First dataset from UCI
#student-performance
    
PATH_CSV="./student-performance.csv"

df_csv=pd.read_csv(PATH_CSV)
df_csv.head()


# --------------------------------------------------------------------------------------------------------------------------

# In[113]:


#Second dataset from UCI
 #bank-additional
    
PATH3_CSV="./bank-additional.csv"

df3_csv=pd.read_csv(PATH3_CSV)
df3_csv.head()


# --------------------------------------------------------------------------------------------------------------------------

# In[126]:


#The Dictionary for automobile
get_ipython().system('curl https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names')


# In[115]:


#Third dataset from UCI
 #automobile_dataset
    
PATH2_URL="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
col2_ls=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]

df2_csv=pd.read_csv(PATH2_URL, names=col2_ls)
df2_csv.head()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# In[116]:


import requests


# In[117]:


#API Address
# API Address with parameters set
#I used the location API
PATH_API = 'https://u50g7n0cbj.execute-api.us-east-1.amazonaws.com/v2/locations?limit=200&page=1&offset=0&sort=desc&radius=1000&country_id=SA&order_by=lastUpdated&dumpRaw=false'
# Make a GET request
r = requests.get(PATH_API)

# Put the data into a pandas DataFrame
pd.DataFrame(r.json()["results"])


# In[118]:


df=pd.DataFrame(r.json()["results"])
df['name']#shows cities that are in the data


# In[119]:


df.shape # shows the number of rows and columns

