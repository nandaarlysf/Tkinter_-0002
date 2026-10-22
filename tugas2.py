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

entri = []
for i in range(10):
    L = tk.Label(frame, text=mapel[i], anchor="w", width=18)
    E = tk.Entry(frame, bd=3, width=10, justify="center")
    L.grid(row=i, column=0, padx=5, pady=3)
    E.grid(row=i, column=1, padx=5, pady=3)
    entri.append(E)

# 1 button
B = tk.Button(top, text="Hasil Prediksi", command=hasilPrediksi,
              bg="green", fg="white", width=15)
B.pack(pady=15)

# 1 label luaran hasil prediksi
L_hasil = tk.Label(top, text="", font=("Arial", 14, "bold"), fg="blue")
L_hasil.pack()

top.mainloop()