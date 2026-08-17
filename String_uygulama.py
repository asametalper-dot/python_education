WebSide="https://www.kozlukmtal.com.tr"# kurum veb sitesi   
Bolum="Bilişim Teknolojileri"#bölüm adı
uzunluk=len(WebSide)#web sitesinin uzunluğu
print("Web Sitesi: ",WebSide)#web sitesini ekrana yazdırma
print("Bölüm: ",Bolum)#bölüm adını ekrana yazdırma
print("Web Sitesi Uzunluğu: ",uzunluk)#web sitesinin uzunluğunu ekrana yazdırma
www=WebSide[8:25]#web sitesinin www kısmını alma
print("www: ",www)# web sitesinin www kısmını ekrana yazdırma
com=WebSide[-7:-4]#com kısmını alma
print("com: ",com)# com kısmını ekrana yazdırma
Web_Uzunluk=len(WebSide)#web sitesinin uzunluğunu alma
Bolum_Uzunluk=len(Bolum)#bölüm adının uzunluğunu alma
print("Web Sitesi Uzunluğu: ",Web_Uzunluk)#web sitesinin uzunluğunu ekrana yazdırma
print("Bölüm Uzunluğu: ",Bolum_Uzunluk)#bölüm adının uzunluğunu ekrana yazdırma
print(WebSide[0:15])#web sitesinin ilk 15 karakterini ekrana yazdırma
print(WebSide[15:len(WebSide)-1])#web sitesinin 15. karakterinden son karakterine kadar olan kısmını ekrana yazdırma
print(Bolum [::-1])#bölüm adını ters çevirerek ekrana yazdırma
Selamlama="Hello world"#selamlama mesajı
print(Selamlama)#selamlama mesajını ekrana yazdırma
Selamlama=Selamlama[:6]+"W"+Selamlama[7:]#selamlama mesajının 6. karakterini değiştirme 
print(Selamlama)#selamlama mesajını ekrana yazdırma
msg="abc "
print(msg*3)#mesajı 3 kez ekrana yazdırma
Ad, Soyad,Yas,Meslek="Abdulsamet","Alper",40,"Bilgisayar Mühendisi"#ad, soyad, yaş ve meslek bilgilerini saklamak için değişkenler
print(f"benim adım: {Ad}, soyadım: {Soyad}, yaşım: {Yas}, mesleğim: {Meslek}")#f string formatlama yöntemi ile ekrana yazdırma