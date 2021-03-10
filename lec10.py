#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
from datascience import *

# Configure notebook (happens automatically on data8.berkeley.edu)
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Configure for presentation
np.set_printoptions(threshold=50, linewidth=50)
import matplotlib as mpl
mpl.rc('font', size=16)


# In[125]:


top = Table.read_table('top_movies.csv')
top.set_format([2, 3], NumberFormatter).show(30)


# In[127]:


top.barh('Title', 'Gross')


# In[129]:


top.group('Studio').barh('Studio', 'count')


# In[130]:


top.group('Studio').sort('count', descending=True).barh('Studio', 'count')


# In[132]:


top.select([0, 2, 3]).barh('Title')


# ## Histograms

# In[32]:


in_millions = np.round(top.column(3)/1000000, 2)
millions = top.select(['Title', 'Year']).with_column('Millions', in_millions)
millions


# In[33]:


millions.hist('Millions')


# In[45]:


millions.hist('Millions', bins=np.arange(300,2001,100))


# In[55]:


millions.bin('Millions', bins=np.arange(300,2001,100))


# In[81]:


PercentFormatter().format_value(81/millions.num_rows/(400-300))


# In[82]:


millions.hist('Millions', bins=np.arange(300,2001,100), normed=False)


# In[90]:


millions.bin('Millions', bins=[300, 400, 500, 600, 700, 2000])


# In[92]:


millions.hist('Millions', bins=[300, 400, 500, 600, 700, 2000], normed=False)


# In[91]:


millions.hist('Millions', bins=[300, 400, 500, 600, 700, 2000])


# In[104]:


trips = Table.read_table('trip.csv')
trips


# In[124]:


commute = trips.where(trips.column('Duration') < 1800)
commute.hist('Duration')


# In[123]:


commute.hist('Duration', bins=np.arange(60, 1801, 10))

