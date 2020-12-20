# Öğrencinin Adı - Soyadı : Bünyamin ÖKTEM
# Öğrenci Numarası : 192855080

# Soru : 3
# Girilen bir string ifadede aranan bir ifade bulunduğunda bir  ̈onceki ve bir sonraki karakteri ekrana getiren python kodunu yazınız.

ifade= input("haydi birşeyler yazın : ")
arananifade = input("Yazdıklarınız içinde aranacak ifadeyi yazın : ")
ara= arananifade

if ifade.find(ara)>-1:
    indis = ifade.find(ara)
    x=indis-1
    y=indis+len(ara)+1
    print(ifade[x:y])

# find : bulmak
# indis : aranacak dizini gösteren komut ifade.
# x : indis içinde aranan karakterin bir önceki karakterini gösteren komut.
# y : aranan kelimeye ve o kelimeden sonraki ifadeyi gösteren parametre 
# len : bir işlevin öğelerini gösteren komut.
