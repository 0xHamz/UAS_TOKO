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
plt.show()


#pengeluaran
plt.figure(figsize=(8, 6))
plt.bar(data_toko['Nama Barang'], data_toko['Pengeluaran'])
plt.xlabel('Nama Barang')
plt.ylabel('Pengeluaran')
plt.title('Pengeluaran')
plt.xticks(rotation=45)
plt.show()

#Pemasukan
plt.figure(figsize=(8, 6))
plt.bar(data_toko['Nama Barang'], data_toko['Pemasukkan'])
plt.xlabel('Nama Barang')
plt.ylabel('Pemasukkan')
plt.title('Pemasukan')
plt.xticks(rotation=45)
plt.show()

# Membuat DataFrame laba yang hanya berisi 15 data pertama
laba_15_data = data_toko[['Tanggal', 'Laba']][:15]

# Membuat grafik laba untuk 15 data pertama
plt.figure(figsize=(8, 6))
plt.bar(laba_15_data['Tanggal'], laba_15_data['Laba'])
plt.xlabel('Tanggal')
plt.ylabel('Laba')
plt.title('Laba (15 Data Pertama)')
plt.xticks(rotation=45)
plt.show()


# %%
import pandas as pd

# Membuat DataFrame untuk Stok Barang
import pandas as pd

# Membaca data dari file CSV 
data_toko = pd.read_csv('data_toko.csv')


# Menghitung Total Pengeluaran dan Total Pemasukan
total_pengeluaran = data_toko['Pengeluaran'].sum()
total_pemasukan = data_toko['Pemasukkan'].sum()

# Menampilkan data nama barang, stok awal, dan barang terjual
# Fungsi untuk menambahkan "Rp." dan titik (.) setiap 3 angka
def format_rupiah(value):
    return f"Rp. {value:,.0f}"

stok_barang = data_toko[['Nama Barang', 'Stok Awal', 'Barang Terjual']]
# Menghitung Stok Akhir
stok_barang['Stok Akhir'] = stok_barang['Stok Awal'] - stok_barang['Barang Terjual']


laba = data_toko[['Tanggal', 'Pengeluaran', 'Pemasukkan', 'Laba']]
laba['Pengeluaran'] = laba['Pengeluaran'].apply(format_rupiah)
laba['Pemasukkan'] = laba['Pemasukkan'].apply(format_rupiah)
laba['Laba'] = laba['Laba'].apply(format_rupiah)

# Menghitung Stok Akhir
stok_akhir = data_toko['Stok Awal'].sum() - data_toko['Barang Terjual'].sum()

# Menampilkan Stok Barang
print("Stok Barang:")
print(stok_barang)

# Menampilkan 
print("\nLaba:")
print(laba)


# Menampilkan Total Pengeluaran, Total Pemasukan, dan Stok Akhir
print("\nTotal Pengeluaran:", total_pengeluaran)
print("Total Pemasukan:", total_pemasukan)
print("Stok Akhir:", stok_akhir)