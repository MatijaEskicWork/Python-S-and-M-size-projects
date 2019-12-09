# Matija Eskic 18/0253

def suma(broj):
    if broj==1:
        return 1
    return suma(broj-1)+1/broj

try:
    N = int(input("Unesite ceo broj, veci od nule:"))
    if N<0:
        print("Uneta duzina niza je van opsega")
    else:
        print("{}-ti harmonijski broj je {:0.4f}.".format(N,suma(N)))


except ValueError:
    print("Niste uneli ceo broj.")
    pass