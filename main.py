# %%
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Membaca data dari file CSV
data_toko = pd.read_csv('data_toko.csv')



# Membuat grafik
# Grafik stok barang
plt.figure(figsize=(8, 6))
plt.bar(data_toko['Nama Barang'], data_toko['Stok Awal'])
plt.xlabel('Nama Barang')
plt.ylabel('Stok Awal')
plt.title('Stok Barang')
plt.xticks(rotation=45)
st.pyplot(plt)


#pengeluaran
plt.figure(figsize=(8, 6))
plt.bar(data_toko['Nama Barang'], data_toko['Pengeluaran'])
plt.xlabel('Nama Barang')
plt.ylabel('Pengeluaran')
plt.title('Pengeluaran')
plt.xticks(rotation=45)
st.pyplot(plt)

#Pemasukan
plt.figure(figsize=(8, 6))
plt.bar(data_toko['Nama Barang'], data_toko['Pemasukkan'])
plt.xlabel('Nama Barang')
plt.ylabel('Pemasukkan')
plt.title('Pemasukan')
plt.xticks(rotation=45)
st.pyplot(plt)

# Membuat DataFrame laba yang hanya berisi 15 data pertama
laba_15_data = data_toko[['Tanggal', 'Laba']][:15]

# Membuat grafik laba untuk 15 data pertama
plt.figure(figsize=(8, 6))
plt.bar(laba_15_data['Tanggal'], laba_15_data['Laba'])
plt.xlabel('Tanggal')
plt.ylabel('Laba')
plt.title('Laba (15 Data Pertama)')
plt.xticks(rotation=45)
st.pyplot(plt)


