class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        m = len(nums)
        if len(nums)==0:
            res.append(nums[0])
            return res
        arrmult=1
        zeroc=0
        for n in nums:
            if n == 0:
                zeroc+=1
                if zeroc==2:
                    return [0]*m
            else:
                arrmult*=n
        for i in range(m):
            if zeroc ==1:
                if nums[i]!=0:
                    res.append(0)
                else:
                    res.append(arrmult)
            else:
                res.append(arrmult//nums[i])
        return res
            
        