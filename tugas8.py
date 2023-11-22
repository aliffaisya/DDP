def data_diri(nama,alamat,gender,umur,hobby):
    print("Nama saya adalah", nama)
    print("Tempat tinggal saya di", alamat)
    print("Saya berkelamin", gender)
    print("Saya berumur", umur)
    print("Saya memiliki hobby", hobby)

data_diri("aliffaisya", "lenteng agung", "perempuan", "19", "menonton")

#2
def nilai_kelulusan(nilai):
    if nilai <= 60:
        return "Gagal", 60
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "nilai tidak valid"
    
print(nilai_kelulusan (nilai=60))

#3
def ganjil(nilai):
    for i in range (nilai + 1):
        if i % 2 != 0 :
            print(i)
ganjil(100)            





