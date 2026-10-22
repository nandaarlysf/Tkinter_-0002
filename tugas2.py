import tkinter as tk

top = tk.Tk()
top.title("Prediksi Prodi Pilihan")
top.geometry("400x470")

# Fungsi tombol: apapun inputnya, hasilnya selalu Teknologi Informasi
def hasilPrediksi():
    L_hasil.config(text="Teknologi Informasi")

# 1 label judul
L_judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan",
                   font=("Arial", 14, "bold"))
L_judul.pack(pady=15)

# 10 input nilai mata pelajaran (label + entry), disusun dengan frame + grid
mapel = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
         "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika"]
frame = tk.Frame(top)
frame.pack(pady=5)

