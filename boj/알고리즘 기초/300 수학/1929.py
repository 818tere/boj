m,n = map(int,input().split())

def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5)+1): # 제곱근까지만 확인하면 됨 (제곱근 이후는 중복) 
        if num%i == 0: # 나누어 떨어지면 소수가 아님
            return False
    return True

for i in range(m,n+1):
    if isPrime(i):
        print(i)