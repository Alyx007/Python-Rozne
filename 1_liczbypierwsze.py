n = 10000
def pierwsza(n):
    a = []
    for i in range(2, n):
        for j in range(i+1, n):
            if j % i == 0:
                a[j] = 0
            else:
                a[j] = 1
    return a

