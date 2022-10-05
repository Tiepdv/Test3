# streamlit_app.py

import streamlit as st
# import os
#from google.cloud.bigquery.client import Client
# from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

sql = "SELECT AdvertisingSystem, PubAccId FROM `showheroes-bi.bi.bi_appadstxt_join_sellersjson` LIMIT 10"

df = client.query(sql).to_dataframe()

# Print results.
st.table(df)
