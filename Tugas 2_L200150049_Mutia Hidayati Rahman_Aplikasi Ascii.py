for Nomor in range(5): ##membuat looping menggunakan for, program melakukaan looping 10 kali
    Karakter = raw_input("Masukkan sebuah karakter berupa huruf, angka, maupun simbol : ")
                ## meminta input yang hasilnya disimpan di variabel Karakter
    Nomor = ord(Karakter) ##melakukan konversi dari input yang disimpan di variabel Karakter ke kode ascii
    print("Kode dari karakter "+ Karakter + " adalah "+ str(Nomor)+"\n") ##menampilkan hasil
print ("Terimakasih") ##menampilkan text terimakasih
 
