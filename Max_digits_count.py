n=int(input())
a=list(map(int,input().split()))
count=0
c=0
l=[]
for i in range(0,n):
    k=a[i]
    while k>0:
        d=k%10
        count+=1
        k=k//10
    l.append(count)
    count=0
b=max(l)
for i in range(0,n):
    if l[i]==b:
        c+=1
print(c)