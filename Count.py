def counteo(arr,arr_size):
    ec=0
    oc=0
    for i in range(arr_size):
        if(arr[i]&1==1):
            oc+=1
        else:
            ec+=1
    print(ec,oc)
n=int(input())
arr=list(map(int,input().split()))
counteo(arr,n)