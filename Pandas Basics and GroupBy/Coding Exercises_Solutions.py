
# coding: utf-8

# # Coding Exercises

# ### Welcome to the instructed and interactive Coding Exercises!

# Now, you will have the opportunity to further analyze our Titanic and Olympic Medals datasets on your own. <br>
# There are __three different levels of difficulty__, starting from the gentle Beginner Level to the more tricky Expert Level.<br>
# __Follow the instructions__ and insert your own code! You are either requested to 
# - Complete the Code and __Fill in the gaps__. Gaps are marked with "__---__" and are __placeholders__ for your code fragment. (Beginner Level)
# - Write Code completely __on your own__ (Expert Level)

# In some exercises, you will find questions that can only be answered, if your code is correct and returns the right output! The correct answer is provided below your coding cell. There you can check whether your code is correct. 

# If you need some further help or if you want to check your code, you can also watch the __solutions videos__ or check the __solutions notebook__.

# ### Have Fun!

# ------------------------------------------------------------------------------

# ## Beginner Level

# First of all, __import pandas__ and use the standard abbreviation __pd__. <br>
# __Fill in the gaps!__

# In[1]:


import pandas as pd #hint: pandas might be the correct placeholder!


# Next, __import__ the csv-file __titanic.csv__ with __pd.read_csv()__ and save the DataFrame in the variable __titanic__. <br>
# __Fill in the gaps!__

# In[2]:


titanic = pd.read_csv("titanic.csv")


# Let´s inspect the __first 10__ rows with the method __head()__.<br>
# __Fill in the gaps!__

# In[4]:


titanic.head(10)


# Now, select the __fare column__ and save it in the __variable fare__. <br>
# __Fill in the gaps!__

# In[5]:


fare = titanic.fare


# Inspect the __first 7 elements__ of fare with the __head()__ method.<br>
# __Fill in the gaps!__

# In[6]:


fare.head(7)


# __Sort__ fare with the __sort_values()__ method from __high to low__.<br>
# __Fill in the gaps!__

# In[7]:


fare.sort_values(ascending = False)


# Now, let´s __visualize__ fare with a __histogramm__ to get the __frequency distribution__ of all fares.<br>
# But first of all, we need to __import matplolib.pyplot__ with the standard abbreviation __plt__.<br><br>
# __Fill in the gaps!__

# In[8]:


import matplotlib.pyplot as plt
plt.style.use("seaborn")


# Next, we create a plot with the __plot()__ method and pass the argument __"hist"__ to the parameter __kind__. <br>
# __Figsize__ should be __(12,8)__. The __fontsize__ for the __axis labels__ shall be __13__. Insert the title __Titanic Ticket Price (Frequency Distribution)__.<br><br>
# 
# __Fill in the gaps!__

# In[9]:


fare.plot(kind = "hist", bins = 100, figsize = (12,8), fontsize = 13)
plt.xlabel("Ticket Price", fontsize = 13)
plt.ylabel("Frequency", fontsize = 13)
plt.title("Titanic Ticket Price (Frequency Distribution)", fontsize = 15)
plt.show()


# Now, we want to calculate the __average/mean passenger age__ for all three __passenger classes__. <br>
# Therefore, we need to __split titanic__ by the key __pclass__ with the __groupby()__ method and apply the __mean()__ method on the __age column__.<br><br>
# __Fill in the gaps!__<br><br>
# What was the average age in the 3rd class?

# In[10]:


titanic.groupby("pclass").age.mean()


# The average passenger age in the __3rd class__ was ... __25.14__ years!

# ## Well done!

# ------------------------------------------------------------------------

# ## Intermediate Level

# In[11]:


import pandas as pd


# Let´s __import__ the csv-file __summer.csv__ and store the DataFrame in the __variable summer__.

# In[13]:


summer = pd.read_csv("summer.csv")


# Inspect the __first 5 rows__.

# In[14]:


summer.head()


# Get some __meta information__ on the summer DataFrame with the __info()__ method.

# In[15]:


summer.info()


# In total we have... __31.165 rows__ and... __9 columns__. 

# As we are only interested in the __columns "Year", "Sport", "Athlete", "Country", "Gender" and "Medal"__, we __slice__ our DataFrame summer with the __loc operator__ and __overwrite our variable summer__.<br><br>
# __Fill in the gaps!__

# In[16]:


summer = summer.loc[:,["Year", "Sport", "Athlete", "Country", "Gender", "Medal"]]


# Let´s again __inspect__ summer with the __head()__ method. Now, we have only __6 columns__, right?

# In[17]:


summer.head()


# Lets´get some more information on the __Athlete Column__ with the __describe()__ method. <br>
# Who is the __most successful Athlete__ of all times and __how many medals__ has she/he won? 

# In[19]:


summer.Athlete.describe()


# ... it´s __Michael Phelps__ with ... __22 medals__

# Now, we want to determine for __each country__: The __Year/Edition__ when the __very first Medal__ was awarded to an Athlete from this Country. For example 1896 for USA.<br><br>
# Therefore, __split__ the summer DataFrame __by Country__ and determine the __minimum value in the Year Column__ for each group/Country. Then, __sort__ the result in a __descending order__, starting with all countries that won the very first Medal in 2012. <br><br>
# __How many__ countries had their Medal debut in __2012__?

# In[22]:


summer.groupby("Country").Year.min().sort_values(ascending = False)


# ... __9__ countries!

# ## Well Done!

# ----------------------------------------------------------

# ## Expert Level

# In[23]:


import pandas as pd


# Let´s __import summer.csv__ with the columns __"Year", "City", "Sport", "Athlete", "Country", "Gender" and "Medal"__ (parameter __usecols__!) and save the DataFrame in the variable __summer__.

# In[25]:


summer = pd.read_csv("summer.csv", usecols = [ "Year", "City", "Sport", "Athlete", "Country", "Gender", "Medal"])


# __Inspect__ the DataFrame.

# In[26]:


summer.head()


# We want to create a __new column "Medals_in_Ed"__ with the __number of Medals__ that the __respective Athlete__ won in the __respective Edition/Year__.<br>
# In a first step, __split__ summer __by "Year" and "Athlete"__ and __count__ the __number of Medals__ for each group. 

# In[27]:


summer.groupby(["Year", "Athlete"]).Medal.count()


# Now, __instead__ of using the the __count() method directly__ on our Groupby Object, let´s __pass "count"__ as an argument for the __transform()__ method. <br>
# By doing so, we are creating a __new Pandas Series__ which we then add as __new column "Medals_in_Ed"__ to our Dataframe. <br><br>
# __Fill in the gap!__

# In[28]:


summer["Medals_in_Ed"] = summer.groupby(["Year", "Athlete"]).Medal.transform("count")


# __Inspect__ the summer Dataframe with the additional column.

# In[29]:


summer.head(10)


# Now, we want to know for each __combination of Year and Gender__ (e.g. 1904 Men), the __maximum number of medals__.<br>
# For example, the __most successful Men in the Edition 1904 won 6 Medals__ and the __most successful Women in 1904 won 3 Medals__, and so on...<br><br>
# How many Medals did the most successful male and female Athlete win in the Edition 2012?

# In[30]:


summer.groupby(["Year", "Gender"]).Medals_in_Ed.max()


# ...<br>
# Best Man in 2012: 6 Medals <br>
# Best Woman in 2012: 5 Medals

# Last but not least, we want to know for __each combination of Year and Gender__ the __three most successful athletes__ by __name, Country and Sport__.<br><br>
# The user-defined Function __best_athletes()__ has already been defined. Simply __run__ the cell!

# In[37]:


def best_athletes(group):
    return group[["City", "Athlete", "Country", "Sport", "Medals_in_Ed"]].drop_duplicates("Athlete").nlargest(3, columns = "Medals_in_Ed" )


# __Apply best_athletes__ on the appropriate Groupby object! <br>
# 
# Who was the __second most successful male__ Athlete in 2012?

# In[38]:


summer.groupby(["Year", "Gender"]).apply(best_athletes)


# ... it was ... Ryan Lochte (USA) with 5 Medals in Aquatics.

# ## Well Done! Looking forward to seeing you in the BONUS Section!
