def check_palindrome(x):
    str_number = str(x)
    reverse_number = str_number[::-1]
    if str_number == reverse_number:
        return True
    else:
        return False
x=0
y=0
bigest_polindrom = 0
for i in range(100,1000):
    for j in range(100,1000):
        if check_palindrome(i*j) and i*j > bigest_polindrom:
            x = i
            y = j
            bigest_polindrom = i*j

print(bigest_polindrom)
print(x,y)