#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(palette='muted', color_codes=True)

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


pd.options.display.float_format='{:,.2f}'.format


# In[3]:


df=pd.read_csv("survey_results_public.csv")


# In[4]:


print(df.head(5))


# In[5]:


df.shape


# In[ ]:


df=df.loc[:,['Hobby','FormalEducation','DevType','YearsCoding','JobSatisfaction','CareerSatisfaction','JobSearchStatus','ConvertedSalary','Gender','Dependents']]


# In[6]:


df


# In[7]:


df.dropna(axis=1, how='all')


# In[8]:


df


# In[ ]:


df


# In[ ]:


#df['Hobby']=df['Hobby'].astype('category')


# In[ ]:


#df['FormalEducation']=df['FormalEducation'].astype('category')


# In[ ]:


#df['DevType']=df['DevType'].astype('category')


# In[ ]:


#df['JobSatisfaction']=df['JobSatisfaction'].astype('category')


# In[ ]:


#df['CareerSatisfaction']=df['CareerSatisfaction'].astype('category')


# In[ ]:


#df['CareerSatisfaction']=df['CareerSatisfaction'].astype('category')


# In[ ]:


#df['CareerSatisfaction']=df['CareerSatisfaction'].astype('category')


# In[ ]:


#df['Gender']=df['Gender'].astype('category')


# In[ ]:


#df['Dependents']=df['Dependents'].astype('category')


# In[ ]:


X=df.drop(columns='ConvertedSalary')
Y=df.ConvertedSalary


# In[ ]:


print(X['Gender'].head(5))


# In[ ]:


#use to get_dummies in pandas
X=pd.get_dummies(['Hobby','Gender','FormalEducation','DevType','YearsCoding','JobSatisfaction','CareerSatisfaction','JobSearchStatus','Dependents'])


# In[ ]:


print(pd.get_dummies(['FormalEducation']).head(10))


# 'Hobby','FormalEducation','DevType','YearsCoding','JobSatisfaction','CareerSatisfaction','JobSearchStatus','ConvertedSalary','Gender','Dependents'

# In[ ]:


X


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')

def plot_histogram(X):
    plt.hist(X,color='gray',alpha=0.5)
    plt.title("Histogram of '{var_name}'".format(var_name=X.name))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


# In[ ]:


plot_histogram(X['Gender'])
plot_histogram(X['YearsCoding'])
#plot_histogram(Y)


# In[ ]:


#df= df.where((pd.notnull(df)), None)


# In[ ]:


plot_histogram(X['Gender'])


# In[ ]:


#How much of your data is missing
X.isnull().sum().sort_values(ascending=False).head()


# In[ ]:


#pd.isna(Y)


# In[ ]:


#Y=df.dropna(axis=1, how='all')


# In[ ]:


Y=df.dropna(axis=1, how='all')


# In[ ]:


Y


# In[ ]:


#from sklearn import preprocessing
#from sklearn.preprocessing import Imputer
#imp=Imputer(missing_values='NaN', strategy='median',axis=0)
#imp.fit(Y)
#Y=pd.DataFrame(data=imp.transform(Y),columns=X.columns)


# In[ ]:


from sklearn.linear_model import LogisticRegression    


# In[ ]:


#reg=LogisticRegression().fit(X,Y)hg


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




