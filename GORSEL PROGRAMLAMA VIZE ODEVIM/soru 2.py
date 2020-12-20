# Öğrencinin Adı - Soyadı : Bünyamin ÖKTEM
# Öğrenci Numarası : 192855080

# Soru : 2
# Girilen bir string ifadenin URL olup olmadığını doğrulayan python kodunu string metodları kullanmadan yazınız.

URL = input('Bir URL adresi girin : ').split(".")
if URL[0] == "www" and URL[2] == ("com"):
    print("Girilen URL Adresi Doğru")
else:
    print("Girilen URL Adresi Yanlış! Lütfen Programı Tekrar Çalıştırıp Geçerli Bir URL Adresi Girin.")

# input : kullanıcıdan giriş komutu isteyen bir kod
# if : eğer
# else : başka
# split : ayırma komut anahtarı (parantez içinde çift tırnak arasına yazılan ifadeye göre karakterleri ayırır)
# [0] ve [2] : python karakter dizisi 0 dan başlar ilk karakter 0 ve " . " (nokta) dan sonra 3. karakteri ifade eder ikisi bir arada varsa doğrular
# [1] : neden yok? : kullanıcı tarafından girilecek string ya da intiger karakteri url'ye uyarlamak için
