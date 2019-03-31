
# coding: utf-8

# # Pandas Basics

# ## Data Import and First Inspection

# In[1]:


import pandas as pd


# In[2]:


titanic = pd.read_csv("titanic.csv")


# In[3]:


titanic.head(10)


# In[4]:


titanic.tail(3)


# In[5]:


type(titanic)


# In[6]:


titanic.info()


# In[7]:


titanic.columns


# In[8]:


titanic.index


# In[9]:


titanic.describe()


# In[10]:


titanic.mean()


# In[11]:


summer = pd.read_csv("summer.csv")


# In[12]:


summer.head()


# In[13]:


summer.tail()


# In[14]:


summer.info()


# ## Selecting Columns and Rows & Conditional Indexing

# In[15]:


titanic.head()


# In[16]:


titanic.age


# In[17]:


titanic["age"]


# In[18]:


titanic[["age", "fare"]]


# In[19]:


titanic.head(10)


# In[20]:


titanic.iloc[[2, 5, 9]]


# In[21]:


titanic.iloc[[2, 5, 9], [2, 3, 6]]


# In[22]:


titanic.loc[7, "age"]


# In[23]:


titanic[titanic.age < 1]


# In[24]:


titanic.loc[titanic.age < 1, ["survived", "sex", "age"] ]


# ## Analyzing & Visualizing tabular Data

# In[25]:


titanic.head()


# In[26]:


titanic.age.mean()


# In[27]:


titanic.age.value_counts(ascending=True)


# In[28]:


titanic.pclass.nunique()


# In[29]:


titanic.pclass.unique()


# In[30]:


titanic_sorted = titanic.sort_values(by = "age", ascending = False)


# In[31]:


titanic_sorted.head()


# In[32]:


titanic.head()


# In[33]:


titanic.nsmallest(n = 20, columns = "fare")


# In[34]:


import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[35]:


titanic.plot(subplots= True, figsize=(12, 15))
plt.show()


# In[36]:


titanic.age.plot(subplots= True, figsize=(12, 8))
plt.show()


# In[37]:


titanic.age.plot(kind = "hist", figsize=(12, 8), bins = 81)
plt.show()


# In[38]:


titanic.plot(kind = "scatter", x = "age", y = "fare", figsize = (14,8))
plt.xlabel("Age", fontsize = 15)
plt.ylabel("Ticket Price", fontsize = 15)
plt.title("Titanic Passengers (Age vs. Fare)", fontsize = 18)
plt.show()

