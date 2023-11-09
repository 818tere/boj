t = int(input())
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y) # Euclidean algorithm
    
for _ in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))

