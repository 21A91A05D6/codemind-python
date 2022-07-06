n=int(input())
a=list(map(int,input().split()))
c=0
for j in range(0,n):
    r=a[j]
    if r==1:
        continue
    for i in range(2,(r//2)+1):
        if r%i==0:
           break
    else:
        c+=1
print(c)
        