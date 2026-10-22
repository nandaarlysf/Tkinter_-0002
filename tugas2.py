import tkinter as tk

top = tk.Tk()
top.title("Prediksi Prodi Pilihan")
top.geometry("400x470")

# Fungsi tombol: apapun inputnya, hasilnya selalu Teknologi Informasi
def hasilPrediksi():
    L_hasil.config(text="Teknologi Informasi")

