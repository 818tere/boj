while(1):
    x,y,z = list(map(int,input().split()))
    if x==y==z==0:
        break
    if max(x,y,z) >= sum([x,y,z]) - max(x,y,z): #먼저 invalid 체크해야
        print("Invalid")
    elif x == y == z:
        print("Equilateral")
    elif x == y or y == z or z == x:
        print("Isosceles")
    else:
        print("Scalene")