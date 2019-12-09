

string = '01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010'
niz = string.split()


novi = []
for el in niz:
    rec = el
    stepen = len(rec)-1
    ukupno = 0
    for element in rec:
        broj = int(element)
        ukupno = ukupno + broj*(2**stepen)
        stepen -= 1
    novi.append(ukupno)


for el in novi:
    print(chr(el),end='')
print(' ')
hexstring = '6170706c65'
hexstring = hexstring.upper()
set1 = {'0','1','2','3','4','5','6','7','8','9'}

new = []
ukupno = 0
for j,elem in enumerate(hexstring):

    if elem in set1:
        broj = int(elem)
        if j % 2 == 0:
            ukupno = ukupno + broj*16
        else:
            ukupno = ukupno + broj
            ukupno = chr(ukupno)
            new.append(ukupno)
            ukupno = 0
    else :
        broj = ord(elem) - 55
        if j % 2 == 0:
            ukupno += broj*16
        else:
            ukupno += broj
            ukupno = chr(ukupno)
            new.append(ukupno)
            ukupno = 0

for el in new:
    print(el,end='')
print(' ')

octstring = '163 164 151 164 143 150'
niz = octstring.split()
novi = []
for elem in niz:
    rec = elem
    stepen = len(rec)-1
    ukupno = 0
    for element in rec:
        broj = int(element)
        ukupno = ukupno + broj*(8**stepen)
        stepen -= 1

    novi.append(chr(ukupno))

for elem in novi:
    print(elem,end='')

