sayi = 600851475143

bolenleri = 2

carpanlar = 0

while bolenleri <= sayi:

    if sayi % bolenleri == 0:

        carpanlar = bolenleri

        sayi //= bolenleri
    else:
        bolenleri += 1

print(f"600851475143 sayısının en büyük böleni: {bolenleri}")