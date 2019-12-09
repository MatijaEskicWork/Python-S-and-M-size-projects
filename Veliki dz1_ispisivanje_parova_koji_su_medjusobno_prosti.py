# Matija Eskic 18/0253


def nzd(a,b):
    if b==0:
        return a
    return nzd(b,a % b)

try:
    lista = []
    i = -1
    N = int(input())
    while type(N) == int :
        i = i + 1
        lista.append(N)

        for j in range(0,i):
            if lista[j]>N:
                max1 = lista[j]
                min1 = N
            else:
                max1 = N
                min1 = lista[j]
            gcd = nzd(min1,max1)
            if gcd==1:
                print("({}, {})".format(lista[j],N))
        N = int(input())
except ValueError:
    pass