import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('main_data.csv')

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['month'] = df['order_purchase_timestamp'].dt.to_period('M')

st.title("📊 Dashboard Analisis E-Commerce")

# FILTER
selected_category = st.sidebar.multiselect(
    "Pilih Kategori",
    df['product_category_name'].unique(),
    default=df['product_category_name'].unique()[:5]
)

df_filtered = df[df['product_category_name'].isin(selected_category)]

# METRIC
st.metric("Total Revenue", df_filtered['price'].sum())
st.metric("Total Orders", df_filtered['order_id'].nunique())

# BAR CHART
st.subheader("Penjualan per Kategori")
category_sales = df_filtered.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
category_sales.plot(kind='bar', ax=ax)
st.pyplot(fig)

# LINE CHART
st.subheader("Tren Bulanan")
monthly_sales = df_filtered.groupby('month')['price'].sum()

fig2, ax2 = plt.subplots()
monthly_sales.plot(kind='line', ax=ax2)
st.pyplot(fig2)