#import modules
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#buat object root dari class Tk
root = ttk.Window(themename= "morph")

#atur title aplikasi
root.title("Aplikasi Perhitungan Harga Berass")

#atur lebar & tinggi
root.geometry('500x500')

#buat teks
ttk.Label(root, text="Aplikasi Penghitung Harga beras", bootstyle=PRIMARY, font=('Times New Roman', 15, 'bold')).pack(pady=15)

ttk.Label(root, text="Pilih Jenis Beras Anda :" ).pack()

#select option
jenis_beras = ttk.Combobox(root, values=["Sania", "Raja", "Hoki", "Topi Koki", "Pulen Wangi"])
jenis_beras.pack()

ttk.Label(root, text="Pilih Berat Beras:" ).pack()

#select option
berat_beras = ttk.Combobox(root, values=["1Kg", "2Kg", "3Kg", "4Kg", "5Kg", "10Kg"])
berat_beras.pack()

#Mengembalika Nilai
result_label = ttk.Label(root, text="")  # Label untuk menampilkan hasil
result_label.pack()

#Fungsi Aplikasi
def hitung():
    jenis = jenis_beras.get()
    berat = berat_beras.get()

    harga = 0

    if jenis == "Sania":
        if berat == "1Kg":
            harga = 14500
        elif berat == "2Kg":
            harga = 29000
        elif berat == "3Kg":
            harga = 43500
        elif berat == "4Kg":
            harga = 58000      
        elif berat == "5Kg":
            harga = 70000
        elif berat == "10Kg":
            harga = 137000
    elif  jenis == "Raja":
        if berat == "1Kg":
            harga = 16500
        elif berat == "2Kg":
            harga = 33000
        elif berat == "3Kg":
            harga = 49500
        elif berat == "4Kg":
            harga = 66000 
        elif berat == "5kg":
            harga = 80000
        elif berat == "10kg":
            harga = 157000 
    elif jenis == "Hoki":
        if berat == "1Kg":
            harga = 14000
        elif berat == "2Kg":
            harga = 28000
        elif berat == "3Kg":
            harga = 42000
        elif berat == "4Kg":
            harga = 56000 
        elif berat == "5kg":
            harga = 55000
        elif berat == "10kg":
            harga = 105000 
    elif jenis == "Topi Koki":
        if berat == "1Kg":
            harga = 13000
        elif berat == "2Kg":
            harga = 26000
        elif berat == "3Kg":
            harga = 39000
        elif berat == "4Kg":
            harga = 52000 
        elif berat == "5kg":
            harga = 50000
        elif berat == "10kg":
            harga = 99000         
    elif jenis == "Pulen Wangi":
        if berat == "1Kg":
            harga = 18000
        elif berat == "2Kg":
            harga = 36000
        elif berat == "3Kg":
            harga = 54000
        elif berat == "4Kg":
            harga = 72000 
        elif berat == "5kg":
            harga = 70000
        elif berat == "10kg":
            harga = 139000 

    hasil = f"Total Harga : Rp.{harga}"
    # tampilkan hasil

    result_label.config(text=hasil)

 #button 
ttk.Button(root, text="Cek Harga", command=hitung).pack(pady=15)
#jalankan aplikasi 
root.mainloop()