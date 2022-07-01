n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,n):
    sum+=a[i]
avg=(sum)/n
#res="{:.2f}".format(avg)
for i in range(0,n):
    if a[i]==int(avg):
        print('True')
        break
else:
    print('False')
    