# Öğrencinin Adı - Soyadı : Bünyamin ÖKTEM
# Öğrenci Numarası : 192855080

# Soru : 1
# Girilen bir string ifadenin email adresi olup olmadığını
# doğrulayan python kodunu string metodları kullanmadan yazınız
# Örnek Email : ali.erbey@usak.edu.tr

import re

RegularExpression = '^([a-z0-9]+[\._])*[a-z0-9]+[@](\w+[.])+\w{2,3}$'

def check(eposta):
    if (re.search(RegularExpression, eposta)):
        print("Geçerli bir e-posta adresi")
    else:
        print("Geçersiz bir e-posta adresi")
        
a = input("Bir e-posta adresi giriniz : " )
b = check(a)

# Regular Expression : normal ifade oluturan bir karakter dizisi
# re : RegEx ya da Regular Expression yerine yazılan kısaltma
# def : yalnızca çağırıldığında çalışan bir kod blogu
# check : kontrol anahtarı görevini gören bir kod.
# kapalı parantez : dizin operatörü
# input : kullanıcının manuel giriş yapmasını istediğimiz komut
# print : yazdırma
# if : eğer
# else : başka, yani diğer koşullarda gerçekleşmeyen durumda devreye giren kod