class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        sn = list(s)
        if (len(s)==0):
            return 0
        if (len(s)==1):
            return 1
        n = len(sn)
        ot=0
        ni=sn[0]
        for i in range(n):
            ct=1
            if sn[i]-1 in s:
                continue
            else:
                m = sn[i]
                while m+1 in s:
                    ct+=1
                    m +=1
            ot = max(ot,ct)
        return ot

        