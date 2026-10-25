class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort algorithm
        freq={}
        ot=[]
        for n in nums:
            freq[n] = freq.get(n,0)+1
        bucket = [[] for _ in range(len(nums)+1)]
        for nums,val in freq.items():
            bucket[val].append(nums)
        for i in range(len(bucket)-1,0,-1):
            for v in bucket[i]:
                ot.append(v)
                if len(ot)==k:
                    return ot

        