import time

czas = time.time()

a = int(input("Wpisz jakas liczbe:"))
b = int(input("Wpisz jakas liczbe:"))
wynik = a * b
czas2 = time.time()
roznica = czas2 - czas
print("Zajelo ci to: ", roznica)