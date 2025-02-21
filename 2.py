a = 1
b = 2

toplam = 2

while True:
    c = a + b
    a = b
    b = c

    if c > 4000000:
        break

    if c % 2 == 0:
        toplam += c

print(toplam)



