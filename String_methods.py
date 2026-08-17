msg="lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
print(msg)# mesajı ekrana yazdırma
print(len(msg))# mesajın uzunluğunu ekrana yazdırma
print(msg.upper())# mesajı büyük harflerle ekrana yazdırma
print(msg.isupper())# mesajın büyük harflerle yazılıp yazılmadığını kontrol etme
print(len(msg))# mesajın uzunluğunu ekrana yazdırma
print(msg.lower())# mesajı küçük harflerle ekrana yazdırma
print(msg.islower())# mesajın küçük harflerle yazılıp yazılmadığını kontrol etme
print(len(msg))# mesajın uzunluğunu ekrana yazdırma
print(msg.title())# mesajın her kelimesinin ilk harfini büyük yaparak ekrana yazdırma
print(len(msg))# mesajın uzunluğunu ekrana yazdırma
print(msg.capitalize())# mesajın ilk harfini büyük yaparak ekrana yazdırma
print(len(msg))# mesajın uzunluğunu ekrana yazdırma
print(msg.strip())# mesajın başındaki ve sonundaki boşlukları kaldırarak ekrana yazdırma
print(msg.split())# mesajı bşluklardan ayırarak diziye çevirerek ekrana yazdırma
print(len(msg.split()))# mesajın kaç kelimeden oluştuğunu ekrana yazdırma
Varmi=msg.find("samet")# mesajın içinde "samet" kelimesinin olup olmadığını kontrol etme
print(Varmi)# mesajın içinde "samet" kelimesinin olup olmadığını ekrana yazdırma
Degistir=msg.replace("lorem","alper")# mesajın içindeki "lorem" kelimesini "alper" kelimesi ile değiştirme
print(Degistir)# değiştirilmiş mesajı ekrana yazdırma
Yidizli_msg=Degistir.replace(" ","*")# mesajın içindeki boşlukları yıldız işareti ile değiştirme
print(Yidizli_msg)# değiştirilmiş mesajı ekrana yazdırma

