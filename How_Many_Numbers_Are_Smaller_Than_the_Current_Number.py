class Solution:
    def SmallerThanCrnt(self,nums):
        l=len(nums)
        ans=[]
        c=0
        for i in nums:
            for j in range(l):
                if(nums[j]-i)<0:
                    c+=1
            ans.append(c)
            c=0
        return ans
n=int(input())
nums=list(map(int,input().split()))
ob1=Solution()
a=ob1.SmallerThanCrnt(nums)
print(*a)