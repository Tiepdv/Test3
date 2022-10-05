#!/usr/bin/env python
# coding: utf-8

# In[3]:


# pip install streamlit
# Check with with pyarrow 3.0.0 or similar stuffs which is removed or updated.....to avoid conflict


# In[1]:


import streamlit as st
import pandas as pd
import numpy as np

st.write("""# My first app 
Hello *world!*""")

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)


# In[ ]:




