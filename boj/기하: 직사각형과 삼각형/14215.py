l = sorted(map(int,input().split())) #오름차순 정렬
res = l[0] + l[1] + min(l[2], l[0]+l[1]-1) 
print(res)
#min 안에는 삼각형 세 변중 가장 큰값. l[0]+l[1]은 넘기면 안되므로 -1로 최소한 조정