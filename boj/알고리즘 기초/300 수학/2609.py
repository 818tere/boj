x, y = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y) # Euclidean algorithm
print(gcd(x, y))
print(x*y//gcd(x, y)) # lcms