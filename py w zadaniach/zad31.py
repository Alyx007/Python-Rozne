import time 
czas1 = time.time()
time.sleep(10)
czas2 = time.time()
roznica = czas2 -czas1

if roznica == 10:
    print("Super, rowno 10 sekund!")
else:
    print(roznica)