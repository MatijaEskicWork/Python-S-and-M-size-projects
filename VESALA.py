import os
import random


def ModifikujText(text):
    text = text.replace('',' ')
    text = text.lstrip()
    text = text.rstrip()
    return text


def NapraviSkrivenu(text):
    lista = []
    for elem in text:
        if elem!=' ':
            lista.append('_')
        else:
            lista.append(elem)
    lista = ''.join(lista)
    return lista


def Azuriraj(ulaz,text,duz,neuspesni,skrivena,prethodni,brojac,kopija,kopija_teksta):
    if ulaz == '?':
        kopija_teksta = kopija_teksta.replace(' ','')
        lista = list(rec1)
        lista2 = list(skrivena)
        lista1 = list(text)
        random_broj = random.choice(lista)
        while random_broj in lista2:
            random_broj = random.choice(lista)
        for i in range(0,len(lista1)):
            if lista1[i]==random_broj:
                lista2[i] = random_broj
                break
        skrivena = ''.join(lista2)
        brojac = brojac - 1


    elif not(ulaz in text):
        neuspesni = neuspesni + ', ' + kopija
        neuspesni = neuspesni.lstrip(', ')
        brojac = brojac - 1
    else:
        lista = list(text)
        lista2 = list(skrivena)
        if ulaz == text:
            skrivena = ulaz
        else:
            for i in range(0,len(lista)):
                if lista[i]==ulaz:
                    lista2[i] = ulaz
            skrivena = ''.join(lista2)
    prethodni = prethodni + ', ' + kopija
    prethodni = prethodni.lstrip(', ')
    return neuspesni,skrivena,prethodni,brojac


def ProveriPobeda(skrivena,text,text1):
    gotovo = False
    if skrivena == text:
        print('Pogodili ste rec/recenicu {} ! Pobedaa!!!'.format(text1))
        gotovo = True
    return gotovo


##pocetak
print('Unesite recenicu:')
word = input()
word = word.lower()
rec1 = word
broj_pokusaja = max(len(word)*6 // 10,5)
word = ModifikujText(word)
skrivena_rec = ''
skrivena_rec = NapraviSkrivenu(word)
prethodni_pokusaji = ''
neuspesni_pokusaji = ''
rec = word
os.system('cls')
pobeda = False
while (broj_pokusaja>0) and not(pobeda) :
    print('Prethodni pokusaji: {}'.format(prethodni_pokusaji))
    print('Neuspesni pokusaji: {}'.format(neuspesni_pokusaji))
    print('Broj preostalih pokusaja: {}'.format(broj_pokusaja))
    print('Ukucajte ?(znak pitanja) i pritisnite enter ako zelite pomoc ali gubite jedan pokusaj.')
    print(skrivena_rec)
    print('Unesite slovo ili recenicu:')
    unos = input()
    kopija = unos
    unos = ModifikujText(unos)
    duzina = len(unos)
    neuspesni_pokusaji,skrivena_rec,prethodni_pokusaji,broj_pokusaja = Azuriraj(unos,rec,duzina,neuspesni_pokusaji,skrivena_rec,prethodni_pokusaji,broj_pokusaja,kopija,rec1)
    pobeda=ProveriPobeda(skrivena_rec,rec,rec1)
if not(pobeda):
    print('Obeseni ste!!!')