## Matija Eskic 2018/0253

def ubaci_u_set(parametar):
    kao_lista = parametar.split()
    del(kao_lista[0])
    return set(string for string in kao_lista)


try:
    skup = set()
    file_input = open(input(),"r")
    for linija in file_input:
        skup = skup | ubaci_u_set(linija)
    print(skup)


except FileNotFoundError:
    print("Fajl nije nadjen.")
    pass
