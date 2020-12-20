# Öğrencinin Adı - Soyadı : Bünyamin ÖKTEM
# Öğrenci Numarası : 192855080

# Soru : 5
# Girilen ifade aşağıdakilerden biri olabilir.
# 1. receive-23-1-0\n
# 2. send-181-3-0-1\nreceive-170-3-0\n
# 3. receive-150-0-1\n0-4-5-6-\n
# programı çalıştırınca "Lütfen parametreListesi Giriniz:" ifadesinin karşısına yukarıda sıralanan 3 ifadeden birisini giriniz.

veri = input("Lütfen parametreListesi Giriniz:")
uyariMesaji = "Gönderilen parametreList yalnış lütfen kontrol ediniz..."


def parametreListIsleme(dizi):
    for i in range(0, len(dizi)):
        if dizi[i].find("receive") > -1 and dizi[i].find("-") > -1:
            receive = dizi[i].split("-")
            if len(receive) == 4 and receive[0] == "receive":
                cozulenParamete = parametreKontrol(receive)
                if cozulenParamete["parametredoğru"] == True:
                    print("Kod Tipi=Receive-Gelen")
                    print("Sinyal Gücü=", cozulenParamete["sinyalgucu"])
                    print("Cihaz=", cozulenParamete["cihazturu"])
                    print("Durumu=", cozulenParamete["cihazdurum"])
            else:
                print(uyariMesaji)

        elif dizi[i].find("send") > -1 and dizi[i].find("-") > -1:
            send = dizi[i].split("-")
            if len(send) == 5 and send[0] == "send":
                cozulenParamete = parametreKontrol(send)
                if cozulenParamete["parametredoğru"] == True:
                    print("Kod Tipi=Receive-Gelen")
                    print("Sinyal Gücü=", cozulenParamete["sinyalgucu"])
                    print("Cihaz=", cozulenParamete["cihazturu"])
                    print("Durumu=", cozulenParamete["cihazdurum"])
                    print("Cevap=", cozulenParamete["sendcevap"])
            else:
                print(uyariMesaji)
        else:
            print(uyariMesaji)


def parametreKontrol(parametreListesi):
    parametreKarsilik = {
        "parametredoğru": False,
        "sinyalgucu": "",
        "cihazturu": "",
        "cihazdurum": "",
        "sendcevap": ""
    }
    sinyalGucu = ""
    parametreDoğru = True
    cihazTuru = ""
    cihazDurum = ""
    sendCevap = ""
    geciciParametre = int(parametreListesi[1])
    if geciciParametre > -1 and geciciParametre < 51:
        sinyalGucu = str(geciciParametre)+"-Çok Zayıf Sinyal"

    elif geciciParametre > 50 and geciciParametre < 101:
        sinyalGucu = str(geciciParametre)+"-Zayıf Sinyal"

    elif geciciParametre > 100 and geciciParametre < 151:
        sinyalGucu = str(geciciParametre)+"-Orta Sinyal"

    elif geciciParametre > 150 and geciciParametre < 201:
        sinyalGucu = str(geciciParametre)+"-Güçlü Sinyal"

    elif geciciParametre > 200 and geciciParametre < 256:
        sinyalGucu = str(geciciParametre)+"-Çok Güçlü Sinyal"

    else:
        parametreDoğru = False
    parametreKarsilik["sinyalgucu"] = sinyalGucu

    if parametreDoğru:
        geciciParametre = int(parametreListesi[2])
        if geciciParametre == 1:
            cihazTuru = str(geciciParametre)+"-Televizyon"

        elif geciciParametre == 2:
            cihazTuru = str(geciciParametre)+"-Çamaşır Makınesi"

        elif geciciParametre == 3:
            cihazTuru = str(geciciParametre)+"-Buzdolabı"

        elif geciciParametre == 4:
            cihazTuru = str(geciciParametre)+"-Fırın"

        else:
            parametreDoğru = False
        parametreKarsilik["cihazturu"] = cihazTuru
    if parametreDoğru:
        geciciParametre = int(parametreListesi[3])
        if geciciParametre == 1:
            cihazDurum = str(geciciParametre)+"-on"

        elif geciciParametre == 0:
            cihazDurum = str(geciciParametre)+"-off"

        else:
            parametreDoğru = False
        parametreKarsilik["cihazdurum"] = cihazDurum

    if parametreDoğru and parametreListesi[0] == "send":
        geciciParametre = int(parametreListesi[4])
        if geciciParametre == 0:
            sendCevap = str(geciciParametre)+"-Cevap İstenmiyor"

        elif geciciParametre == 1:
            sendCevap = str(geciciParametre)+"-Cevap isteniyor"

        else:
            parametreDoğru = False
        parametreKarsilik["sendcevap"] = sendCevap
    parametreKarsilik["parametredoğru"] = parametreDoğru
    return parametreKarsilik


if veri.count("/n") >= 0 and (veri.find("receive") >= 0 or veri.find("send") >= 0):
    dizi = veri.split("/n")
    print(dizi)
    parametreListIsleme(dizi)

else:
    print(uyariMesaji)
