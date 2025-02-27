karelerin_toplami = 0
toplaminin_karesi = 0

toplam = 0

for i in range(0,101):
    toplam += i
    karelerin_toplami += i*i

print((toplam * toplam) - karelerin_toplami)