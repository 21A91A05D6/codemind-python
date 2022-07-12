n=int(input())
a=list(map(int,input().split()))
#print(a)
b=[]
for i in range(0,len(a)+1):
    for i in a:
        if i not in b:
            b.append(i)
        #continue
print(*b)