for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if c*c == a*a + b*b:
            print(a*b*c)
            print(f"Üçgendeki sayılar: {a},{b},{c}")
