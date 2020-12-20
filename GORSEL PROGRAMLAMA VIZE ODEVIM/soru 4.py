# Öğrencinin Adı - Soyadı : Bünyamin ÖKTEM
# Öğrenci Numarası : 192855080

# Soru : 4
# Üç basamaklı rakamları birbirinden farklı kaç tane sayı olduğunu bulan ve bu sayıları ekrana yazdıran python kodunu yazınız.

a=0
for i in range(100,999):
    x=str(i)[0]
    y=str(i)[1]
    z=str(i)[2]

    if x!=y and x!=z and y!=z:
        a = a+1
        print(i)

print("Rakamları birbirinden farklı 3 basamaklı sayı adedi = "+str(a))

# a : değişken
# for : için
# in : içinde anlamında 
# range : aralık
# str : string kısaltması
# i : herhangi bir üç basamaklı sayıyı gösterir karakter
# x : i'nin 1. karakteri
# y : i'nin 2. karakteri
# z : i'nin 3. karakteri
