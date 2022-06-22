x=int(input())
i=1
sum=0
for i in range(1,x+1):
    sum=sum+(1/i)
f="{:.2f}".format(sum)
print(f)