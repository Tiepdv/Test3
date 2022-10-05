#!/usr/bin/env python
# coding: utf-8

# In[3]:


# pip install streamlit
# Check with with pyarrow 3.0.0 or similar stuffs which is removed or updated.....to avoid conflict


# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
from google.cloud import bigquery
client = bigquery.Client()

sql = """
    SELECT name, SUM(number) as count
    FROM `bigquery-public-data.usa_names.usa_1910_current`
    GROUP BY name
    ORDER BY count DESC
    LIMIT 10
"""

df = client.query(sql).to_dataframe()

st.write("""# My first app 
Hello *world!*""")

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)


# In[ ]:




