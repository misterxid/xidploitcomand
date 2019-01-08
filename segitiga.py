def hitung() :
  pil='y'
  while (pil=='y'):
   print("______________________________________________________")
   print("Pembuat : MR_XiD.")
   print("______________________________________________________")
   print("Whastapp: 083851312460")
   print("===============================")
   print(" Pilih Dengan Cara Ketik Angka ")
   print("===============================")
   print("1. Hitung Luas Segitiga        ")
   print("2. Hitung Keliling Segitiga    ")

   pil="y"
   pilih=int(raw_input("Masukkan Pilihan : "))
   if pilih==1 :
      a=int(raw_input("masukkan Alas (cm) : "))
      t=int(raw_input("Masukkan TInggi (cm) : "))
      l=0.5*a*t
      print(l)
      pil=raw_input("Apakah ingin menghitung kembali ??? y/n: ")
   elif pilih==2 :
      s1=int(raw_input("masukkan sisi Pertama (cm) : "))
      s2=int(raw_input("Masukkan sisi kedua   (cm) : "))
      s3=int(raw_input("Masukkan sisi ketiga  (cm) : "))
      k=s1+s2+s3
      print(k)
      pil=raw_input("Apakah ingin menghitung kembali ??? y/n: ")
hitung ()