# streamlit_app.py

import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

col1, col2,col3 = st.columns(2)

with col1:
   st.image("images.png", width=80)

with col2:
   st.title("📊 IAB dataset")
with col2:
   st.write('')

option = st.selectbox(
    'Please choose the dataset',
    ('WEB', 'APP'))

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

if option=='WEB':
	query="SELECT * FROM `showheroes-bi.bi.bi_adstxt_join_sellerjson_with_count_domains` limit 10"

elif option=='APP':
	query="SELECT * FROM `showheroes-bi.bi.bi_appadstxt_join_sellersjson_with_count_domains` limit 10"


query_job = client.query(query)
df=client.query(query).to_dataframe()
st.table(df)
