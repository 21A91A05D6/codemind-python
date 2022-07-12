n=int(input())
a=list(map(int,input().split()))
ct=0
for i in range(0,n):
    c=1
    if a[i]>0:
        for j in range(i+1,n):
            if a[i]==a[j]:
                c+=1
                a[j]=-1
        #print(a[i],c)
        if a[i]==c:
            ct+=1
print(ct)