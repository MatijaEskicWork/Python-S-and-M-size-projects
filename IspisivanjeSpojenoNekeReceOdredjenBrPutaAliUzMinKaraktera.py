import collections

T = int(input())

for i in range(T):
    string = list(map(str,input().split()))
    rec = string[0]
    broj_puta = int(string[1])
    kraj = collections.deque(rec)
    kraj.popleft()
    pocetak = collections.deque(rec)
    pocetak.pop()
    print(rec)
    duzina = len(rec)
    print(kraj)
    print(pocetak)
    br_istih = len(kraj)
    while (pocetak != kraj) :
        br_istih -= 1
        if br_istih == 0:
            break
        kraj.popleft()
        print(kraj)
        pocetak.pop()
        print(pocetak)
    print(br_istih)
    resenje = duzina - br_istih
    resenje = duzina + resenje*(broj_puta-1)
    print(resenje)