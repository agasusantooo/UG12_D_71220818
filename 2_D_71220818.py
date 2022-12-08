print("~~~~~ Table Matematika Nich ~~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
model=int(input("Masukkan model matematika yang diinginkan 1/2 :"))
angkamasuk=int(input("Menampilkan table matematika dari angka:"))
if(model==1) :
    for i in range(1,11)   :
        hasil = (angkamasuk*i)
        print(angkamasuk, "x", i, "=", hasil)

elif(model==2) :
    for i in range(50,66) :
        hasil = (i/angkamasuk)
        print(i, ":", angkamasuk, "=", hasil)
