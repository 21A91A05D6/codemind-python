#max prodt of 2 
import sys
def findmaximumproduct(a):
    if len(a)<2:
        return
    max_product=-sys.maxsize
    max_i=max_j=-1
    
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if max_product<a[i]*a[j]:
                max_product=a[i]*a[j]
                (max_i,max_j)=(i,j)
    print((a[max_i]-1)*(a[max_j]-1))
if __name__=="__main__":
    a=list(map(int,input().split()))
    findmaximumproduct(a)
