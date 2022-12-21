import time

czas = time.gmtime()
sekundy = czas[5]
#print(czas)
print(sekundy)
czas_spania = 60 - int(sekundy)
if sekundy < 60:
    time.sleep(czas_spania)

print("Koniec spania")