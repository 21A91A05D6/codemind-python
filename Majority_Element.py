class Solution:
    def maj_elmnt(self,nums):
        nums=sorted(nums)
        i=0
        for _ in range(len(set(nums))):
            if nums.count(nums[i])>=len(nums)/2:
                return nums[i]
            else:
                i=i+nums.count(nums[i])
n=int(input())
nums=list(map(int,input().split()))
ob1 = Solution()
a=ob1.maj_elmnt(nums)
print(a)