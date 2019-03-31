
# coding: utf-8

# # Pandas GroupBy Operations

# ## Understanding GroupBy objects

# In[1]:


import pandas as pd


# In[2]:


titanic = pd.read_csv("titanic.csv")


# In[3]:


titanic.head()


# In[4]:


titanic.tail()


# In[5]:


titanic.info()


# In[6]:


titanic_slice = titanic.iloc[:10, [2,3]]


# In[7]:


titanic_slice


# In[8]:


titanic_slice.groupby("sex")


# In[9]:


gbo = titanic_slice.groupby("sex")


# In[10]:


type(gbo)


# In[11]:


gbo.groups


# In[12]:


l = list(gbo)


# In[13]:


l


# In[14]:


len(l)


# In[15]:


l[0]


# In[16]:


type(l[0])


# In[17]:


l[0][0]


# In[18]:


l[0][1]


# In[19]:


type(l[0][1])


# In[20]:


l[1]


# In[21]:


titanic_slice.loc[titanic_slice.sex == "female"]


# In[22]:


titanic_slice_f = titanic_slice.loc[titanic_slice.sex == "female"]
titanic_slice_f


# In[23]:


titanic_slice_m = titanic_slice.loc[titanic_slice.sex == "male"]
titanic_slice_m


# In[24]:


titanic_slice_f.equals(l[0][1])


# In[25]:


for element in gbo:
    print(element[1])


# ## Splitting with many Keys

# In[26]:


import pandas as pd


# In[27]:


summer = pd.read_csv("summer.csv")


# In[28]:


summer.head()


# In[29]:


summer.info()


# In[30]:


summer.Country.nunique()


# In[31]:


split1 = summer.groupby("Country")


# In[32]:


l = list(split1)
l


# In[33]:


len(l)


# In[34]:


l[100][1]


# In[35]:


split2 = summer.groupby(by = ["Country", "Gender"])


# In[36]:


l2 = list(split2)
l2


# In[37]:


len(l2)


# In[38]:


l2[104]


# In[39]:


l2[104][0]


# In[40]:


l2[104][1]


# ## split-apply-combine explained

# In[41]:


import pandas as pd


# In[42]:


titanic = pd.read_csv("titanic.csv")


# In[43]:


titanic_slice = titanic.iloc[:10, [2,3]]


# In[44]:


titanic_slice


# In[45]:


list(titanic_slice.groupby("sex"))[0][1]


# In[46]:


list(titanic_slice.groupby("sex"))[1][1]


# In[47]:


titanic_slice.groupby("sex").mean()


# In[48]:


titanic.groupby("sex").survived.sum()


# In[49]:


titanic.groupby("sex")[["fare", "age"]].max()


# In[50]:


new_df = titanic.groupby("sex").mean()


# In[51]:


new_df


# In[52]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[53]:


new_df.plot(kind = "bar", subplots = True, figsize = (8,15), fontsize = 13)
plt.show()


# ## split-apply-combine applied

# In[54]:


import pandas as pd


# In[55]:


summer = pd.read_csv("summer.csv")


# In[56]:


summer.head()


# In[57]:


summer.info()


# In[58]:


medals_per_country = summer.groupby("Country").Medal.count().nlargest(n = 20)
medals_per_country


# In[59]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[60]:


medals_per_country.plot(kind = "bar", figsize = (14, 8), fontsize = 14)
plt.xlabel("Country", fontsize = 13)
plt.ylabel("No. of Medals", fontsize = 13)
plt.title("Summer Olympic Games (Total Medals per Country)", fontsize = 16)
plt.show()


# In[61]:


titanic = pd.read_csv("titanic.csv")


# In[62]:


titanic.head()


# In[63]:


titanic.info()


# In[64]:


titanic.describe()


# In[65]:


titanic.fare.mean()


# In[66]:


titanic.groupby("pclass").fare.mean()


# In[67]:


titanic.survived.sum()


# In[68]:


titanic.survived.mean()


# In[69]:


titanic.groupby("sex").survived.mean()


# In[70]:


titanic.groupby("pclass").survived.mean()


# In[71]:


titanic["ad_chi"] = "adult"


# In[72]:


titanic.loc[titanic.age < 18, "ad_chi"] = "child"


# In[73]:


titanic.head(20)


# In[74]:


titanic.ad_chi.value_counts()


# In[75]:


titanic.groupby("ad_chi").survived.mean()


# In[76]:


titanic.groupby(["sex", "ad_chi"]).survived.count()


# In[77]:


titanic.groupby(["sex", "ad_chi"]).survived.mean().sort_values(ascending = False)


# In[78]:


w_and_c_first = titanic.groupby(["sex", "ad_chi"]).survived.mean().sort_values(ascending = False)


# In[79]:


w_and_c_first.plot(kind = "bar", figsize = (14,8), fontsize = 14)
plt.xlabel("Groups", fontsize = 13)
plt.ylabel("Survival Rate", fontsize = 13)
plt.title("Titanic Survival Rate by Sex/Age-Groups", fontsize = 16)
plt.show()


# In[80]:


titanic.groupby("sex")[["survived", "pclass", "age", "fare"]].agg(["sum", "mean"])


# ## Transformation with transform()

# In[81]:


import pandas as pd


# In[82]:


titanic = pd.read_csv("titanic.csv")


# In[83]:


titanic.head()


# In[84]:


titanic.groupby(["sex", "pclass"]).survived.transform("mean")


# In[85]:


titanic["group_surv_rate"] = titanic.groupby(["sex", "pclass"]).survived.transform("mean")


# In[86]:


titanic.head()


# In[87]:


titanic["outliers"] = abs(titanic.survived-titanic.group_surv_rate)


# In[88]:


titanic[titanic.outliers > 0.85]


# ## Generalizing split-apply-combine with apply()

# In[89]:


import pandas as pd


# In[90]:


titanic = pd.read_csv("titanic.csv", usecols = ["survived", "pclass", "sex", "age", "fare"])


# In[91]:


titanic.head()


# In[92]:


titanic.groupby("sex").mean()


# In[93]:


female_group = list(titanic.groupby("sex"))[0][1]
female_group


# In[94]:


female_group.mean().astype("float")


# In[95]:


def group_mean(group):
    return group.mean()


# In[96]:


group_mean(female_group)


# In[97]:


titanic.groupby("sex").apply(group_mean)


# In[98]:


titanic.nlargest(5, "age")


# In[99]:


def five_oldest_surv(group):
    return group[group.survived == 1].nlargest(5, "age")


# In[100]:


titanic.groupby("sex").apply(five_oldest_surv)


# ## Hierarchical Indexing (MultiIndex) with Groupby

# In[101]:


import pandas as pd


# In[102]:


titanic = pd.read_csv("titanic.csv", usecols = ["survived", "pclass", "sex", "age", "fare"])


# In[103]:


titanic


# In[104]:


summary = titanic.groupby(["sex", "pclass"]).mean()


# In[105]:


summary


# In[106]:


summary.index


# In[107]:


summary.loc[("female", 2), :]


# In[108]:


summary.loc[("female", 2), "age"]


# In[109]:


summary.swaplevel().sort_index()


# In[110]:


summary.reset_index()


# ## stack() and unstack()

# In[111]:


import pandas as pd


# In[112]:


summer = pd.read_csv("summer.csv")


# In[113]:


summer.head()


# In[114]:


medals_by_country = summer.groupby(["Country", "Medal"]).Medal.count()


# In[115]:


medals_by_country


# In[116]:


medals_by_country.loc[("USA", "Gold")]


# In[117]:


medals_by_country.shape


# In[118]:


medals_by_country.unstack(level = -1)


# In[119]:


medals_by_country = medals_by_country.unstack(level = -1, fill_value= 0)


# In[120]:


medals_by_country.head()


# In[121]:


medals_by_country.shape


# In[122]:


medals_by_country = medals_by_country[["Gold", "Silver", "Bronze"]]


# In[123]:


medals_by_country.sort_values(by = ["Gold", "Silver", "Bronze"], ascending = [False, False, False], inplace = True)


# In[124]:


medals_by_country.head(10)


# In[125]:


import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[126]:


medals_by_country.head(10).plot(kind = "bar", figsize = (12,8), fontsize = 13)
plt.xlabel("Country", fontsize = 13)
plt.ylabel("Medals", fontsize = 13)
plt.title("Medals per Country", fontsize = 16)
plt.legend(fontsize = 15)
plt.show()


# In[127]:


medals_by_country.stack().unstack()

