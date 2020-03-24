#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
from pandasql import sqldf
from sqlalchemy import create_engine


# In[40]:


#Pandas Setting
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199
pd.set_option('display.max_columns', 1000)
pd.options.display.max_colwidth = 1000
pd.set_option('display.expand_frame_repr', False)
# pandas_bokeh.output_notebook()
# pandas_bokeh.output_file("InteractivePlot.html")
# pd.set_option('plotting.backend', 'pandas_bokeh')
disk_engine = create_engine('sqlite:///COVID-19.db')


# In[41]:


#Load Data
countries_aggregated = pd.read_csv("data/countries-aggregated.csv", delimiter=',',keep_default_na=False)
time_series_19_covid_combined = pd.read_csv("data/time-series-19-covid-combined.csv", delimiter=',',keep_default_na=False)
world_population_2019 = pd.read_csv("data/world_population_2019.csv", delimiter=',',keep_default_na=False)


# In[42]:


dataset1 = pd.merge(time_series_19_covid_combined, world_population_2019, left_on='Country/Region',right_on='Location', how='left')


# In[43]:


dataset2= dataset1[["Date",'Country/Region','Province/State',"Lat","Long","Confirmed","Recovered","Deaths","PopMale","PopFemale","PopTotal"]]


# In[44]:


dataset2['Country']= dataset2[['Country/Region','Province/State']].apply(lambda x : '{} - {}'.format(x[0],x[1]), axis=1)


# In[45]:


dataSet = dataset2[["Date","Country","Lat","Long","Confirmed","Recovered","Deaths","PopMale","PopFemale","PopTotal"]]
del dataset2 
del dataset1


# In[46]:


dataSet.head()


# In[47]:


#Save data into sqlite3
dataSet.to_sql('covid019', disk_engine, if_exists='append')
#Save data into excel
dataSet.to_excel("covid019.xlsx")
#Save data into csv
dataSet.to_csv("covid019.csv")


# In[35]:





# In[37]:





# In[ ]:




