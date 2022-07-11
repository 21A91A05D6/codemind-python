n=int(input())
a=list(map(int,input().split()))
c=0
max=0
for i in a:
    r=a.count(i)
    if r==1:
        c+=1
        if i>max:
            max=i
if c>0:
    print(max)       
if c==0:
    print("-1")