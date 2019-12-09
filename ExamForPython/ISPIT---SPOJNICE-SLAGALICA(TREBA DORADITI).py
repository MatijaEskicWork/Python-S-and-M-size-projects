import random
import os


def Igraj(kraj,trenutno,objasnjenje,za_pogadjanje,glavni,pomoc):
    while not(kraj):
        pogadjanje = int(input('Unesite indeks koji pogadjate(1-8):'))
        if za_pogadjanje[pogadjanje-1] == pomoc[trenutno]:
            za_pogadjanje[pogadjanje-1] = za_pogadjanje[pogadjanje-1] + '+'
        trenutno += 1
        if trenutno>7:
            kraj = True
            break
        IspisTokomIgre(trenutno,objasnjenje,za_pogadjanje,glavni,pomoc)
    return kraj


def IspisTokomIgre(trenutno,objasnjenje,za_pogadjanje,glavni,pomoc):
    os.system('cls')
    print(objasnjenje)
    for i,elem in enumerate(za_pogadjanje):
        if i==trenutno:
            print('->',glavni[i],'  ',elem)
        else:
            print(glavni[i],'  ',elem)


def SamoIspis(objasni,slucajno,ovi_prvi,ovi_drugi):
    os.system('cls')
    broj = len(objasni)
    ludi_broj = random.randint(0,broj-1)
    glavni = ovi_prvi[8*ludi_broj:8*ludi_broj+8]
    pomoc = ovi_drugi[8*ludi_broj:8*ludi_broj+8]
    za_pogadjanje = slucajno[8*ludi_broj:8*ludi_broj+8]
    objasnjenje = objasni[ludi_broj]
    print(objasnjenje)

    for i,elem in enumerate(za_pogadjanje):
        if i == 0:
            print('->',glavni[i],'  ',elem)
        else:
            print(glavni[i],'  ',elem)
    trenutno = 0
    return trenutno,objasnjenje,za_pogadjanje,glavni,pomoc





def FormirajNovuSpojnicu(objasni,slucajno,ovi_prvi,ovi_drugi):
    fajl = open('spojnice.txt','a')
    description = input ('Unesite objasnjenje:')
    objasni.append(description)
    description = '\n' + description + '\n'
    fajl.write(description)
    kopija2 = []
    for i in range (8):
        line = input('Unesite par broj {}:'.format(i+1))
        line = line + '\n'
        fajl.write(line)
        niz = line.split('*')
        ovi_prvi.append(line[0])
        kopija2.append(line[1])
        ovi_drugi.append(line[1])
    random.shuffle(kopija2)
    for elem in kopija2:
        slucajno.append(elem)
    return objasni,slucajno,ovi_prvi,ovi_drugi
    fajl.close()


def ProcitajFajl(ime):
    fajl = open(ime,'r')
    objasnjenja = []
    randomsi = []
    kopija2 = []
    originali = []
    originali2 = []
    for i,linija in enumerate(fajl):
        broj = i // 9
        broj = broj
        if i % 9==0:
            linija = linija.strip()
            objasnjenja.append(linija)
            kopija2 = []
        else:
            niz = linija.split('*')
            originali.append(niz[0])
            niz[1] = niz[1].rstrip('\n')
            kopija2.append(niz[1])
            originali2.append(niz[1])
            if i % 9 == 8:
                random.shuffle(kopija2)
                for elem in kopija2:
                    randomsi.append(elem)
    fajl.close()
    return objasnjenja,randomsi,originali,originali2


string = ''
igramo = True
string = input('Hocete li igrati(nova), dodati spojnicu(dodaj) ili izaci(kraj): ')
string = string.lower()
objasni = []
slucajno = []
ovi_prvi = []
ovi_drugi = []

objasni,slucajno,ovi_prvi,ovi_drugi = ProcitajFajl('spojnice.txt')
if string == 'kraj':
    igramo = False
while igramo:
    glavni = []
    pomoc = []
    za_pogadjanje = []
    objasnjenje = ''
    if string == 'dodaj':
        objasni,slucajno,ovi_prvi,ovi_drugi = FormirajNovuSpojnicu(objasni,slucajno,ovi_prvi,ovi_drugi)
    else:
        kraj = False
        trenutno,objasnjenje,za_pogadjanje,glavni,pomoc = SamoIspis(objasni,slucajno,ovi_prvi,ovi_drugi)
        kraj = Igraj(kraj,trenutno,objasnjenje,za_pogadjanje,glavni,pomoc)
    string = input('Hocete li igrati(nova), dodati spojnicu(dodaj) ili izaci(kraj)')
    if string =='kraj':
        break











