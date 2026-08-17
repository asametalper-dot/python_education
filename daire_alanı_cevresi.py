'''
çok satırlı yorum satırı
Daire Alanı ve Çevresi Hesaplama
matematikte dairenin alanı ve çevresi için kullanılan formüller:
Dairenin Alanı = pi * r^2
Dairenin Çevresi = 2 * pi * r

'''
# tek satırlı yorum satırı
Alan=0# dairenin alanını saklamak için değişken
Cevre=0# dairenin çevresini saklamak için değişken
pi=3.141518# pi sayısını saklamak için değişken 
print("yarıçapı giriniz: ")# kullanıcıdan yarıçap girişi isteme 
Yaricap=float(input())# kullanıcıdan girilen yarıçapı float tipine çevirme
Alan=round(pi*Yaricap**2, 2)# dairenin alanını hesaplama ve 2 ondalık basamağa yuvarlama
Cevre=round(2*pi*Yaricap, 2)# dairenin çevresini hesaplama ve 2 ondalık basamağa yuvarlama
print("Dairenin Alanı: " + str(Alan))# dairenin alanını ekrana yazdırma 
print("Dairenin Çevresi: " + str(Cevre))# dairenin çevresini ekrana yazdırma
print(Cevre)# çevreyi ekrana yazdırma
print(Alan)# alanı ekrana yazdırma  

