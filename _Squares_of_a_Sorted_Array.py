class Solution:
    def sortedSquares(self, A):
        l=len(A)
        ans=[]
        for i in range(l):
            ans.append(A[i]**2)
        ans.sort()
        return ans
n=int(input())
A=list(map(int,input().split()))
ob1 = Solution()
a=ob1.sortedSquares(A)
print(*a)