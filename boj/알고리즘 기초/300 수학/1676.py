n = int(input())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(len(str(factorial(n)))-len(str(factorial(n)).rstrip('0')))