import random

lista = []
for i in range(15):
    lista.append(random.randint(0, 100))

def sortowanie_szybkie(lista):
    mniejsze = []
    rowne = []
    wieksze = []

    if len(lista) > 1:
        piwot = lista[0]
        for x in lista:
            if x > piwot:
                wieksze.append(x)
            elif x == piwot:
                rowne.append(x)
            else:
                mniejsze.append(x)
        return sortowanie_szybkie(mniejsze) + rowne + sortowanie_szybkie(wieksze)
    else:
        return lista

print(lista)
print(sortowanie_szybkie(lista))

def sortowanie_szybkie2(lista):
    mniejsze = [x for x in lista[1:] if x < lista[0]]
    rowne = [lista[0]]
    wieksze = [x for x in lista[1:] if x > lista [0]]

    if len(lista) > 1:
        return sortowanie_szybkie(mniejsze) + rowne + sortowanie_szybkie(wieksze)
    else:
        return lista

print(lista)
print(sortowanie_szybkie(lista))