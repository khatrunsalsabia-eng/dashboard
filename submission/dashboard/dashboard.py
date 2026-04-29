import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Menggunakan path yang disarankan reviewer agar tidak error saat di-run
# 'dashboard/main_data.csv' berasumsi Anda menjalankan streamlit dari root folder
try:
    df = pd.read_csv('dashboard/main_data.csv')
except FileNotFoundError:
    # Ini adalah fallback jika Anda menjalankan streamlit dari dalam folder dashboard
    df = pd.read_csv('main_data.csv')

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
# Konversi ke string agar line chart matplotlib tidak error pada beberapa versi
df['month_str'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
st.title("📊 Dashboard Analisis E-Commerce")
st.markdown("Dashboard ini menampilkan hasil analisis data E-Commerce sesuai dengan pertanyaan bisnis.")

# FILTER di Sidebar
st.sidebar.header("Filter Data")
selected_category = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=df['product_category_name'].unique(),
    default=df['product_category_name'].unique()[:5]
)

df_filtered = df[df['product_category_name'].isin(selected_category)]

# METRIC (Menampilkan informasi ringkas)
col1, col2 = st.columns(2)
with col1:
    total_revenue = df_filtered['price'].sum()
    st.metric("Total Revenue", f"R$ {total_revenue:,.2f}")
with col2:
    total_orders = df_filtered['order_id'].nunique()
    st.metric("Total Orders", total_orders)

# BAR CHART (Pertanyaan Bisnis 1)
st.subheader("Top 10 Kategori Produk dengan Penjualan Tertinggi")
category_sales = df_filtered.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 5))
category_sales.plot(kind='bar', color='#636EFA', ax=ax)
ax.set_ylabel("Revenue")
ax.set_xlabel("Kategori")
st.pyplot(fig)

# LINE CHART (Pertanyaan Bisnis 2)
st.subheader("Tren Penjualan Bulanan")
monthly_sales = df_filtered.groupby('month_str')['price'].sum()

fig2, ax2 = plt.subplots(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='#EF553B', ax=ax2)
ax2.set_ylabel("Total Revenue")
ax2.set_xlabel("Bulan")
plt.xticks(rotation=45)
st.pyplot(fig2)

st.caption('Copyright © Khatrunnada Salsabila Zega 2026')