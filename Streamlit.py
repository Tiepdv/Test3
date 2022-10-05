# streamlit_app.py

import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

query="SELECT AdvertisingSystem, PubAccId FROM `showheroes-bi.bi.bi_appadstxt_join_sellersjson` LIMIT 10"
query_job = client.query(query)

df=client.query(query).to_dataframe()

st.table(df)
