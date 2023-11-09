l = [int(input()) for _ in range(3)] #세 개를 한줄씩 입력받아
if sum(l) != 180: 
    print("Error")
elif l[0] == l[1] == l[2]:
    print("Equilateral")
elif l[0] == l[1] or l[1] == l[2] or l[2] == l[0]:
    print("Isosceles")
else:
    print("Scalene")