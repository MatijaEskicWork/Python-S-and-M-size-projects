import re

def ResiExp(niz_broj,niz_znaci):
    kopija_niz = niz_znaci
    pom = 0
    brojac = len(kopija_niz)-1
    for elem in reversed(kopija_niz):
        if elem == '^':
            pom = niz_broj[brojac]**niz_broj[brojac-1]
            niz_broj[brojac-1] = pom
        brojac = brojac - 1
    return pom


def ResiPutaPodeljeno(niz_broj,niz_znaci,prethodno):
    kopija_niz = niz_znaci
    pom = prethodno
    for brojac,elem in enumerate(kopija_niz):
        if elem == '*':
            pom = niz_broj[brojac]*niz_broj[brojac+1]
            niz_broj[brojac+1] = pom
        elif elem == '/':
            pom = niz_broj[brojac]*niz_broj[brojac+1]
            niz_broj[brojac+1] = pom
    return pom

def ResiPlusMinus(niz_broj,niz_znaci,prethodno):
    pom = prethodno
    kopija_niz = niz_znaci
    for brojac,elem in enumerate(kopija_niz):
        if elem == '+':
            pom = niz_broj[brojac]+niz_broj[brojac+1]
            niz_broj[brojac+1] = pom
        if elem == '-':
            pom = niz_broj[brojac]-niz_broj[brojac+1]
            niz_broj[brojac+1] = pom
    return pom

izraz = input()
cifre = {'1','2','3','4','5','6','7','8','9','0'}
prviminus = False
znaci = {'+','-','*','/','^'}
if izraz[0]=='-' :
    prviminus = True
    del(izraz[0])
resenje = 0
cifra = False
brojevi = []
znak = []
broj = ''
neki = ''
for elem in izraz:
    if not(cifra) and elem in cifre :
        cifra = True
        broj = broj + elem
    elif cifra and elem in cifre:
        broj = broj + elem
    elif cifra and not(elem in cifre):
        nesto = int(broj)
        brojevi.append(nesto)
        broj = ''
    if elem in znaci:
        neki = elem
        znak.append(neki)
if prviminus:
    pom = -brojevi[0]
    brojevi[0] = pom
nesto = int(broj)
brojevi.append(nesto)
print(brojevi,' ',znak)
resenje = ResiExp(brojevi,znak)
resenje = ResiPutaPodeljeno(brojevi,znak,resenje)
resenje = ResiPlusMinus(brojevi,znak,resenje)
print(resenje)






