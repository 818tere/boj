s = input()
l = []
for i in range(len(s)):
    l.append(s[i:]) # s[i:] == s[i:len(s)]
    
l.sort()
for i in l:
    print(i)