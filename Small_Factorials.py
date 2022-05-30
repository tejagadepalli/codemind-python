n=int(input())
for i in range(0,n):
    a=int(input())
    fact=1 
    for j in range(a,0,-1):
        fact=fact*j 
    print(fact)