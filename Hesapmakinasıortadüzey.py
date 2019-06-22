
print("""
[1] Toplama İşlemi
[2] Çıkarma İşlemi
[3] Çarpma İşlemi
[4] Bölme İşlemi
[5] Üs Alma İşlemi
[q]Çıkış



""")
print("============================")
giris = input("Seçiminiz: ")
print("============================")
if giris=="1":
    x =input("İlk Sayı: ")
    x =float(x)
    y= input ("İkinci Sayı: ")
    y= float(y)
    
    print("İşlem Sonucu: ", x + y)

elif giris=="2":
    x =input("İlk Sayı: ")
    x =float(x)
    y= input ("İkinci Sayı: ")
    y= float(y)
    
    print("İşlem Sonucu: ", x - y)

elif giris=="3":
    x =input("İlk Sayı: ")
    x =float(x)
    y= input ("İkinci Sayı: ")
    y= float(y)
    
    print("İşlem Sonucu: ", x * y)

elif giris=="4":
    x =input("İlk Sayı: ")
    x =float(x)
    y= input ("İkinci Sayı: ")
    y= float(y)
    
    print("İşlem Sonucu: ", x / y)

elif giris=="5":
     x =input("Taban :")
     x =float(x)
     y= input ("Kuvvet :")
     y= int(y)
     
     print("İşlem Sonucu: ", x **y)

elif giris=="q" or giris=="Q":
    print("Çıkılıyor...")
    quit()

