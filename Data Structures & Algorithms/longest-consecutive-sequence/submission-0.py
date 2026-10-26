class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if (len(s)==1):
            return 1
        
        n = len(s)
        ot=0
        for i in range(n):
            if len(s)!=0:
                m = min(s)
                s.remove(m)
                ct = 1
            while(m+1 in s):
                s.remove(m+1)
                ct+=1
                m = m+1
            ot = max(ot,ct)
        return ot
        

        