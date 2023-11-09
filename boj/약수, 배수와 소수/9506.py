while (1):
    n = int(input())
    if n == -1:
        break
    divisors = []
    for i in range(1,n): #자기 자신은 약수로 제외
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        print(f"{n} = {' + '.join(map(str,divisors))}") #자기 자신을 제외한 약수들의 합 = 자기 자신 (완전수)
    else:
        print(f"{n} is NOT perfect.")