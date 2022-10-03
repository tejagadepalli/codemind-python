n=int(input())
a=list(map(int,input().split()))
j1=0
i1=0
c=0
for i in range(n):
    c1=0
    c2=0
    for j in range(i,n):
        if a[j]==0:
            c1+=1
        if a[j]==1:
            c2+=1
        if c1==c2:
            if c<j-i:
                c=j-i
                i1=i
                j1=j
if c==0:
    print('-1')
else:
    print(i1,j1)