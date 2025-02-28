import math

asal_sayilar = []
count = 0

def asal_kontrol(x):
    asal_mı = True
    if x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                asal_mı = False
                break
        return asal_mı

i = 2

while True:
    if asal_kontrol(i):
        count += 1
    if count == 10001:
        print(i)
        break
    i += 1