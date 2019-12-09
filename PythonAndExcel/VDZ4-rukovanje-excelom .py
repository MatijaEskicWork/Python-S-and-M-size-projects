
br_fajlova = int(input('Unesi broj fajlova: '))
recnik = {}
zaglavlja = []
OK = True
indeksi = []
for i in range(br_fajlova):
    ulaz = input('Unesi broj ime fajla #{}: '.format(i+1))
    fajl = open(ulaz,'r',encoding = 'utf-8-sig')
    nova_zaglavlja = []
    if not(OK):
        break
    poz_indeks = 0
    niz = []
    j = 0
    for linija in fajl:
        string = linija
        string = string.rstrip('\n')
        niz = string.split(',')
        if not(OK):
            print('Nemoguce napraviti fajl.')
            break
        if j == 0:
            for k,elem in enumerate(niz):
                if elem == 'Broj indeksa':
                    poz_indeks = k
                if elem not in zaglavlja:
                    zaglavlja.append(elem)
                nova_zaglavlja.append(elem)
                print(niz)
        else:
            indeks = niz[poz_indeks]
            if indeks not in indeksi:
                indeksi.append(indeks)
            k = 0
            for k,elem in enumerate(niz):
                vrednost = recnik.get(indeks)
                if vrednost == None:
                    recnik[indeks] = recnik.get(indeks, {})
                    recnik[indeks][nova_zaglavlja[k]] = elem
                else:
                    vrednost = recnik[indeks].get(nova_zaglavlja[k])
                    if vrednost == None:
                        recnik[indeks] = recnik.get(indeks, {})
                        recnik[indeks][nova_zaglavlja[k]] = elem
                    else:
                        if recnik[indeks][nova_zaglavlja[k]] != elem:
                            OK = False
                            break
            print(niz)
        j = j + 1
    fajl.close()
if OK:
    izlaz = open('izlaz.csv','w')
    string = ""
    for el in zaglavlja:
        string = string + el + ","
    string = string.rstrip(",")
    string = string + "\n"
    izlaz.write(string)
    for i,el in enumerate(indeksi):
        string = ''
        for j in range(len(zaglavlja)):
            vrednost = recnik.get(el)
            if vrednost == None:
                string = string + ","
            else:
                vrednost = recnik[el].get(zaglavlja[j])
                if vrednost == None:
                    string = string + ","
                else:
                    string = string + recnik[el][zaglavlja[j]] + ","
        string = string + "\n"
        izlaz.write(string)
izlaz.close()







