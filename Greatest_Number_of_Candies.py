a=int(input())
s=list(map(int,input().strip().split()))
x=int(input())
y=max(s)
for i in range(a):
    if(s[i]+x>=y):
        print("True",end=' ')
    else:
        print("False",end=' ')