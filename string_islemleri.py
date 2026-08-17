Ad="Abdulsamet"# adı
Soyad="Alper"# soyadı
Mesaj="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod " \
" temp or incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, " \
" quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat." \
"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
"fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt iculpa" \
" qui officia deserunt mollit anim id est laborum." # mesaj
Uzunluk=len(Mesaj)# mesajın uzunluğunu alma
Karakter =Mesaj[15]# mesajın 15. karakterini alma
Karakter_Sondan=Mesaj[-2]# mesajın sondan 2. karakterini alma
Kesit=Mesaj[15:300] # mesajın 15-300. karakterleri
Kesit_2=Mesaj[:300]# mesajın 0-300. karakterleri
Ters=Mesaj[::-1]  # mesajın tersini alma
print("Ad: ",Ad)# adı ekrana yazdırma
print("Soyad: ",Soyad)# soyadı ekrana yazdırma
print(Ad+" "+Soyad)# ad ve soyadı birleştirerek ekrana yazdırma
print("Mesaj: ",Mesaj)# mesajı ekrana yazdırma
print("Mesaj Uzunluğu: ",Uzunluk)# mesajın uzunluğunu ekrana yazdırma
print("Mesajın 15. Karakteri: ",Karakter)# mesajın 15. karakterini ekrana yazdırma
print("Mesajın 15-300. Karakterleri: ",Kesit)# mesajın 15-300. karakterlerini ekrana yazdırma
print("Mesajın 0-300. Karakterleri: ",Kesit_2)# mesajın 0-300. karakterlerini ekrana yazdırma
print("Mesajın Sondan 2. Karakteri: ",Karakter_Sondan)# mesajın sondan 2. karakterini ekrana yazdırma
print("Mesajın Tersi: ",Ters)# mesajın tersini ekrana yazdırma

