a=int(input())
s=list(map(str,input().strip().split()))[:a]
d=''
for i in s:
    d+=i
d=int(d)
d+=1
d=str(d)
print(*d)