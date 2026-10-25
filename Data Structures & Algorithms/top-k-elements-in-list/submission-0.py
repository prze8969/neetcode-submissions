class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        ot=[]
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for i in range(k):
            maxk = max(freq, key = freq.get)
            ot.append(maxk)
            freq.pop(maxk)
        return ot

        