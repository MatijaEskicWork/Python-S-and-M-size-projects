## Matija Eskic 18/0253

def Provera(upis):
    skup_dozvoljenih_karaktera = {'1','2','3','4','5','6','7','8','9','0','+','-','*','/','^'}
    skup_operacija = {'+','-','*','/','^'}
    skup_cifara = {'1','2','3','4','5','6','7','8','9','0'}
    bila = False
    OK = True
    for i,elem in enumerate(upis):
        if  elem not in skup_dozvoljenih_karaktera:
            OK = False
            break
        elif i == len(upis)-1 and elem in skup_operacija:
            OK = False
            break
        elif i == 0 and elem in skup_operacija and elem != '-':
            OK = False
            break
        else:
            if elem in skup_operacija and bila == True:
                OK = False
                break
            elif elem in skup_operacija and bila == False:
                bila = True
            elif elem in skup_cifara and bila == True:
                bila = False
    return OK

izraz = input()
DOBRO = Provera(izraz)
while DOBRO == False:
    print("Pogresan unos. Probajte ponovo:")
    izraz = input()
    DOBRO = Provera(izraz)

niz = []
if izraz[0] == '-':
    niz.append(-1)
string = ''
for i,elem in enumerate(izraz):
    if i == 0 and izraz[0] == '-':
        nesto = 0
    elif  elem == '*' or elem == '+' or elem == '/' or elem == '-' or elem == '^':
        int(string)
        niz.append(string)
        string = ''
    elif elem != '*' and elem != '+' and elem != '/' and elem != '-' and elem != '^' :
        string = string + elem
int(string)
niz.append(string)
if niz[0] == -1:
    niz[0] = -int(niz[1])
    del niz[1]

znakovi = []
for i,elem in enumerate(izraz):
    if (elem == '*' or elem == '+' or elem == '/' or elem == '-' or elem == '^') and i!=0:
        znakovi.append(elem)
duzina = len(znakovi)
brojac1 = duzina-1
brojac2 = duzina
while brojac1>-1:
    if znakovi[brojac1]=='^':
        broj1 = int(niz[brojac1])
        broj2 = int(niz[brojac2])
        niz[brojac1]=broj1**broj2
        del niz[brojac2]
        del znakovi[brojac1]
        brojac2-=1
        brojac1-=1
    else:
        brojac2-=1
        brojac1-=1

brojac1 = 0
brojac2 = 0
duzina = len(znakovi)-1

while duzina>=brojac1:
    if znakovi[brojac1]=='*':
        niz[brojac2+1]=int(niz[brojac2])*int(niz[brojac2+1])
        del niz[brojac2]
        del znakovi[brojac1]
        duzina-=1
    elif znakovi[brojac1]=='/':
        niz[brojac2+1]=int(niz[brojac2])/int(niz[brojac2+1])
        del niz[brojac2]
        del znakovi[brojac1]
        duzina-=1
    else:
        brojac2+=1
        brojac1+=1
brojac1 = 0
brojac2 = 0
duzina = len(znakovi)-1

while duzina>=brojac1:
    if znakovi[brojac1]=='+':
        niz[brojac2+1]=int(niz[brojac2])+int(niz[brojac2+1])
        del niz[brojac2]
        del znakovi[brojac1]
        duzina-=1
    elif znakovi[brojac1]=='-':
        niz[brojac2+1]=int(niz[brojac2])-int(niz[brojac2+1])
        del niz[brojac2]
        del znakovi[brojac1]
        duzina-=1
    else:
        brojac2+=1
        brojac1+=1
resenje = niz[brojac2]
print(resenje)







