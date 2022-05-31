class Solution(object):
    def findnumbers(self,nums):
        str_num=map(str,nums)
        c=0
        for s in str_num:
            if len(s)%2==0:
                c+=1
        return c
n=int(input())
nums=list(map(int,input().split()))
ob1=Solution()
a=ob1.findnumbers(nums)
print(a)
    