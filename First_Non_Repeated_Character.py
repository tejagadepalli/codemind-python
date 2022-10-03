n=int(input())
for i in range(n):
    x=int(input())
    s=input()
    c=0
    c1=0
    for i in s:
        c=0
        for j in s:
            if i==j:
                c+=1
        if c==1:
            print(i)
            c1=1
            break
    if c1==0:
        print('-1')