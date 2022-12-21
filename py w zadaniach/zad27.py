import time

czas = int(input("Wpisz czas jaki chcesz przeznaczyc na ten program: "))
if czas <= 10 and czas > 0:
    print("Okej, mozemy poczekac!")
    time.sleep(czas)
if 10 < czas or czas == 0:
    print("Byku wez nie przesadzaj")