class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ot=[]
        n = len(nums)
        premult=[1]*n
        for i in range(1,n):
            premult[i] = premult[i-1]*nums[i-1]
        sufmult=[1]*n
        for j in range(n-2,-1,-1):
            sufmult[j] = sufmult[j+1]*nums[j+1]
        res=[1]*n
        for i in range(0,n):
            res[i] = premult[i]*sufmult[i]
        return res
        