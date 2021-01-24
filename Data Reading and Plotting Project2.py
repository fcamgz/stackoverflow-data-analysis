#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#reading stackoverflow 2020 survey csv file
df = pd.read_csv("D:\\pandasTutorial\\survey_results_public.csv")


# In[4]:


#reading the schema to see the columns and their descriptions
schema = pd.read_csv("D:\\pandasTutorial\\survey_results_schema.csv")


# In[5]:


pd.set_option('display.max_columns', None)


# In[6]:


#understanding the data
#seeing the num of rows and cols
df.shape
df.describe()
df.head(20)
#seeing column names in  a list
df.columns.tolist()
#seeing columns with descriptions
schema.head(50)
#choosing specific column to see its description
schema.iloc[2]
#cleaning the data
#seeing which cols have na values
df = df[df.isna().any(axis=1)]
#dropping duplicates
df = df.drop_duplicates()
#limiting age less than 80 to get rid of outliars
df = df[df['Age'] < 80]
df["Age"].max()
#filling na convertedComp values to mean values to keep the same mean value
#df["ConvertedComp"].fillna(df["ConvertedComp"].mean())
#grouping by country and seeing annual mean salaries by USD
df.groupby("Country")["ConvertedComp"].mean() 
filt = (df["Age"] > 18) & (df["Age"] < 50)
df.groupby("Age")["ConvertedComp"].mean()
df.groupby("Age")["ConvertedComp"].mean()
#changing type of age to int
df["Age"]= df["Age"].astype(int)
#seeing types of the age
df["Age"].dtypes
#filtering data by an age range
adultsInCanada = (df["Age"] > 18) & (df["Age"] < 50) & (df["Country"] == "Canada")
#Seeing annual mean salaries in canada by adult age group
df.loc[adultsInCanada]["ConvertedComp"].mean()
#seeing the education level in adult age group in canada
df.loc[adultsInCanada]["EdLevel"].value_counts()


# In[7]:


#Seeing employment status of adults in canada
df.loc[adultsInCanada]["JobSeek"].value_counts()
#Creating adult group for people who participated in survey
adults = (df["Age"] > 18) & (df["Age"] < 50)
#Seeing the education level
df[adults]["EdLevel"].value_counts()
#seeing employment status for people who are 30 years or older
youngsters = (df["Age"] > 18) & (df["Age"] <= 30)
#by percantage
df[youngsters]["EdLevel"].value_counts(normalize=True)
#canadians
canadian_youngsters = (df["Age"] > 18) & (df["Age"] <= 30) & (df["Country"] == "Canada")
df[canadian_youngsters]["EdLevel"].value_counts(normalize=True)


# In[8]:


#canadian youngster employment status by percentage
df[canadian_youngsters]["Employment"].value_counts(normalize=True)
#seeing percentage of canadian youngsters who are employed
df[canadian_youngsters]["Employment"].str.contains(pat = "Employed").value_counts(normalize=True)
#percentage of canadian youngsters who know python
df[canadian_youngsters]["LanguageWorkedWith"].str.contains(pat = "Python").value_counts(normalize=True)
#percentage of adult womans who are employed
(df[adults]["Employment"].str.contains("Employed") & (df["Gender"] == "Woman")).value_counts(normalize=True)
#percentage of adult males who are employed
(df[adults]["Employment"].str.contains("Employed") & (df["Gender"] == "Man")).value_counts(normalize=True)
#adult womans in canada who are employed based on canada
(df[adultsInCanada]["Employment"].str.contains("Employed") & (df["Gender"] == "Woman")).value_counts(normalize=True)
#adult males in canada who are employed based on canada
(df[adultsInCanada]["Employment"].str.contains("Employed") & (df["Gender"] == "Man")).value_counts(normalize=True)
#percentage of adults who knows python and are employed in the world
(df[adults]["Employment"].str.contains(pat="Employed") & df[adults]["LanguageWorkedWith"].str.contains(pat ="Python")).value_counts(normalize=True)
#in canada 
(df[adultsInCanada]["Employment"].str.contains(pat="Employed") & df[adultsInCanada]["LanguageWorkedWith"].str.contains(pat ="Python")).value_counts(normalize=True)


# In[48]:





# In[21]:


northAmerica = (df["Country"] == "United States") | (df["Country"] == "Canada") | (df["Country"] == "Mexico")


# In[28]:


#increasing size of the plot
fig, scatter = plt.subplots(figsize = (20,10))
#visualizing age counts of the participants
numberOfParticipants = sns.countplot(data=df, x="Age")
plt.title("Participants")
plt.ylabel("Participant Count")
#plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)


# In[114]:


fig, scatter = plt.subplots(figsize = (40,20))
#visualizing gender counts of participants
numberOfParticipants = sns.countplot(data=df, x="Gender")
#defining yaxis limit to see the gender count better
plt.ylim(0, 40000)
#seeing only two genders man and woman in this case
scatter.set_xlabel("Gender",size=30)
scatter.set_ylabel("Count",size=30)
plt.xlim(-0.5,1.5)


# In[105]:


#visualizing education level counts 
fig, scatter = plt.subplots(figsize = (60,30))
#visualizing gender counts of participants
sns.countplot(data=df, x="EdLevel")
scatter.set_xlabel("Education Level",size=50)
scatter.set_ylabel("Count",size=50)


# In[ ]:





# In[ ]:




