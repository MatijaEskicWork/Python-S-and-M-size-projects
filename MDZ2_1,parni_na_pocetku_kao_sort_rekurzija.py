# Matija Eskic 18/0253

def zameni(niz1,broj1,broj2):
    niz1[broj1],niz1[broj2]=niz1[broj2],niz1[broj1]

def uredi(niz,pocetak,kraj):
    if pocetak>=kraj:
        return niz
    if lista[pocetak] % 2 == 0:
        return uredi(niz,pocetak+1,kraj)
    if lista[kraj] % 2 == 1:
        return uredi(niz,pocetak,kraj-1)
    zameni(niz,pocetak,kraj)
    return uredi(niz,pocetak+1,kraj-1)


try:
    N = int(input("Unesite ceo broj(duzinu niza) veci od nule:"))
    if N<=0:
        print("Uneta duzina niza je van opsega")
    else:
        lista = []
        for i in range(0,N):
            x = int(input("Unesite element niza,ceo broj:"))
            lista.append(x)
        print(uredi(lista,0,N-1))


except ValueError:
    print("Niste uneli ceo broj.")
    pass
