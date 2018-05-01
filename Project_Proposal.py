
# coding: utf-8

# In[ ]:


get_ipython().system('gzip Parking_Violations_Issued_-_Fiscal_Year_2018.csv')


# In[1]:


import pandas as pd

import time
t0 = time.time()

# Takes about 6 minutes to load into memory, 
# most of that time is due to datetime parsing
df = pd.read_csv(
    'Parking_Violations_Issued_-_Fiscal_Year_2018.csv.gz', 
    low_memory=True,
    parse_dates=['Issue Date']
)

df.info()


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

plt.rcParams["figure.figsize"] = (10, 5)


# In[7]:


df['weekday'] = df['Issue Date'].dt.dayofweek


# In[29]:


temp1 = df.groupby('weekday')


# In[11]:


temp1.plot.bar(figsize = (15,10))


# In[61]:


groups = df.groupby('weekday')
out = {}
for name, group in groups:
    temp = group['Violation Code'].value_counts()
    out[name] = temp
df1 = pd.DataFrame(out)



# In[71]:


df1.plot.bar(figsize=(15,20), title='Variation of violation across different days', fontsize=15, width = 1.5)

##


# In[70]:


df['Violation County'].hist(edgecolor='white',
    color='lightgreen')


# In[68]:


county = df.groupby('Violation County')['Summons Number'].count()
county.plot.bar(figsize=(15,10))


# In[69]:


df['Violation Code'].hist(edgecolor='white',
    color='lightgreen')

