import math
import functools

def gcd(x,y):
    return math.gcd(x,y)

def lcm(x,y):
    return (x*y) // gcd(x,y)

list = range(1,21)

result = functools.reduce(lcm,list)

print(result)
